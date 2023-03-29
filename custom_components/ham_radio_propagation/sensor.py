"""Support for ham_radio_propagation ."""
from __future__ import annotations

from datetime import timedelta
from http import HTTPStatus
from xml.parsers.expat import ExpatError

import logging
import async_timeout
import xmltodict
import json

from homeassistant.components.sensor import SensorStateClass, SensorEntity, SensorEntityDescription
from homeassistant.const import CONF_NAME
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.device_registry import DeviceEntryType
from homeassistant.util import Throttle, slugify
from .const import *

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    """async_setup_platform"""
    station_code = ""
    station_name = ""
    name = entry.data.get(CONF_NAME, False)

    if entry.data[CHOICE] == TYPE_ONLY_SOLAR:
        sensor_types_out = SENSOR_TYPES
    else:
        station_code = entry.data.get(STATION_CODE, False)
        station_name = entry.data.get(STATION_NAME, False)
        sensor_type_muf: tuple[SensorEntityDescription, ...] = (
            SensorEntityDescription(
                key="solar_hf_muf_" + station_code,
                name="Solar HF MUF",
                state_class=SensorStateClass.MEASUREMENT,
                icon="mdi:format-wrap-top-bottom",
                native_unit_of_measurement="MHz",
            ),
        )
        if entry.data[CHOICE] == TYPE_ONLY_MUF:
            sensor_types_out = sensor_type_muf
        if entry.data[CHOICE] == TYPE_ALL:
            sensor_types_out = (*SENSOR_TYPES, sensor_type_muf[0])

    websession = async_get_clientsession(hass)

    ts_data = HamRadioData(hass.loop, websession)
    ret = await ts_data.async_data_update(entry.data[CHOICE], station_code)
    if ret is False:
        _LOGGER.error("Invalid data")
        return

    async_add_entities(
        [
            HamRadioSensor(ts_data, name, description, entry, station_code)
            for description in sensor_types_out
        ],
        True,
    )


class HamRadioSensor(SensorEntity):
    """Representation of HamRadioSensor."""

    _attr_has_entity_name = True
    _choice = ""
    _station_code = ""

    def __init__(
        self,
        hamradiodata: HamRadioData,
        name,
        description: SensorEntityDescription,
        entry: ConfigEntry,
        station_code: str
    ) -> None:
        """Initialize the sensor."""
        if hamradiodata is None:
            _LOGGER.error("Error empty client")
        self.entity_description = description
        self.hamradiodata = hamradiodata
        slug = slugify(description.key.replace("/", "_"))
        self.entity_id = f"sensor.{DOMAIN}_{slug}"
        self._attr_name = f"{description.name}"
        self._attr_unique_id = f"{entry.entry_id}_{slug}"
        self._attr_device_info = DeviceInfo(
            name=entry.title,
            identifiers={(DOMAIN, entry.entry_id)},
            configuration_url=CONFIGURATION_URL,
            entry_type=DeviceEntryType.SERVICE,
            manufacturer=MANUFACTURER,
            model=MODEL,
            sw_version=VERSION,
        )
        self._choice = entry.data[CHOICE]
        self._station_code = station_code


    async def async_update(self) -> None:
        """Get the latest data and update the state."""
        await self.hamradiodata.async_data_update(self._choice, self._station_code)
        sensor_type = self.entity_description.key
        if sensor_type in self.hamradiodata.data:
            self._attr_native_value = self.hamradiodata.data[sensor_type]


class HamRadioData:
    """Get data from API."""

    def __init__(self, loop, websession):
        """Initialize the data object."""
        self.loop = loop
        self.websession = websession
        self.data = {}

    @Throttle(MIN_TIME_BETWEEN_UPDATES)
    async def async_data_update(self, choice: str, station_code: str):
        """Get data from the web service."""
        _LOGGER.debug("Updating data")
        if choice == TYPE_ONLY_SOLAR:
            await HamRadioData.async_data_update_hamqsl(self)
        if choice == TYPE_ONLY_MUF:
            await HamRadioData.async_data_update_kc2g(self, station_code)
        if choice == TYPE_ALL:
            await HamRadioData.async_data_update_hamqsl(self)
            await HamRadioData.async_data_update_kc2g(self, station_code)

    async def async_data_update_hamqsl(self):
        """Get the hamqsl.com data from the web service."""
        _LOGGER.debug("Updating hamqsl.com data")
        try:
            async with async_timeout.timeout(REQUEST_TIMEOUT):
                req = await self.websession.get(URL_HAMQSL)
            if req.status != HTTPStatus.OK:
                _LOGGER.error("Request failed with status: %u", req.status)
                return False
        except Exception:
            _LOGGER.error("Error contact hamqsl.com API")
            return False

        data = await req.text()
        try:
            xml_data = xmltodict.parse(data)
        except ExpatError:
            return False

        solar_flux_index = xml_data["solar"]["solardata"]["solarflux"]
        solar_sunspots = xml_data["solar"]["solardata"]["sunspots"]
        solar_a_index = xml_data["solar"]["solardata"]["aindex"]
        solar_k_index = xml_data["solar"]["solardata"]["kindex"]
        solar_bz = xml_data["solar"]["solardata"]["magneticfield"]
        solar_wind = xml_data["solar"]["solardata"]["solarwind"]

        band = xml_data["solar"]["solardata"]["calculatedconditions"]["band"]
        for entry in band:
            if entry["@name"] == "80m-40m":
                if entry["@time"] == "day":
                    solar_hf_80_40_day = entry["#text"]
                else:
                    solar_hf_80_40_night = entry["#text"]
            elif entry["@name"] == "30m-20m":
                if entry["@time"] == "day":
                    solar_hf_30_20_day = entry["#text"]
                else:
                    solar_hf_30_20_night = entry["#text"]
            elif entry["@name"] == "17m-15m":
                if entry["@time"] == "day":
                    solar_hf_17_15_day = entry["#text"]
                else:
                    solar_hf_17_15_night = entry["#text"]
            elif entry["@name"] == "12m-10m":
                if entry["@time"] == "day":
                    solar_hf_12_10_day = entry["#text"]
                else:
                    solar_hf_12_10_night = entry["#text"]

        solar_geomag_field = xml_data["solar"]["solardata"]["geomagfield"]
        solar_sig_noise_lvl = xml_data["solar"]["solardata"]["signalnoise"]

        self.data["solar_flux_index"] = solar_flux_index.strip()
        self.data["solar_sunspots"] = solar_sunspots.strip()
        self.data["solar_a_index"] = solar_a_index.strip()
        self.data["solar_k_index"] = solar_k_index.strip()
        self.data["solar_bz"] = solar_bz.strip()
        self.data["solar_wind"] = solar_wind.strip()
        self.data["solar_hf_80_40_day"] = solar_hf_80_40_day
        self.data["solar_hf_80_40_night"] = solar_hf_80_40_night
        self.data["solar_hf_30_20_day"] = solar_hf_30_20_day
        self.data["solar_hf_30_20_night"] = solar_hf_30_20_night
        self.data["solar_hf_17_15_day"] = solar_hf_17_15_day
        self.data["solar_hf_17_15_night"] = solar_hf_17_15_night
        self.data["solar_hf_12_10_day"] = solar_hf_12_10_day
        self.data["solar_hf_12_10_night"] = solar_hf_12_10_night

        self.data["solar_geomag_field"] = solar_geomag_field.strip()
        self.data["solar_sig_noise_lvl"] = solar_sig_noise_lvl.strip()[1]
        return True

    async def async_data_update_kc2g(self, station_code: str):
        """Get the kc2g.com data from the web service."""
        _LOGGER.debug("Updating kc2g.com data")
        try:
            async with async_timeout.timeout(REQUEST_TIMEOUT):
                req = await self.websession.get(URL_KC2G)
            if req.status != HTTPStatus.OK:
                _LOGGER.error("Request failed with status: %u", req.status)
                return False
        except Exception:
            _LOGGER.error("Error contact kc2g.com API")
            return False

        data = await req.text()
        entries = json.loads(data)
        solar_hf_muf = 0
        for entry in entries:
            if entry["station"]["code"].strip() == station_code:
                solar_hf_muf = round(entry["mufd"], 3)
                break

        if solar_hf_muf == 0:
            _LOGGER.error(
                "Station configured [%s] not found in kc2g.com API data. Select the correct Station Code from web site https://prop.kc2g.com/stations/",
                station_code,
            )
            solar_hf_muf = "No Data Found"
            # VALUE_STATION = ""
        self.data["solar_hf_muf_" + station_code] = solar_hf_muf
        return True
