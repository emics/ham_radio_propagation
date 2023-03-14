"""Support for ham_radio_propagation ."""
from __future__ import annotations

from datetime import timedelta
from http import HTTPStatus
import logging
from xml.parsers.expat import ExpatError

import async_timeout
import voluptuous as vol
import xmltodict

from homeassistant.components.sensor import (
    PLATFORM_SCHEMA,
    SensorDeviceClass,
    SensorStateClass,
    SensorEntity,
    SensorEntityDescription,
)
from homeassistant.const import (
    CONF_NAME,
    UnitOfInformation,
)
from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType
from homeassistant.util import Throttle, slugify

from .const import DOMAIN, NAME, MIN_TIME_BETWEEN_UPDATES, REQUEST_TIMEOUT, LOGGER


SENSOR_TYPES: tuple[SensorEntityDescription, ...] = (
    SensorEntityDescription(
        key="solar_flux_index",
        name="Solar Flux Index",
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:weather-sunny-alert",
    ),
    SensorEntityDescription(
        key="solar_sunspots",
        name="Solar Sunspots",
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:weather-sunny-alert",
    ),
    SensorEntityDescription(
        key="solar_a_index",
        name="Solar A-Index",
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:alpha-a",
    ),
    SensorEntityDescription(
        key="solar_k_index",
        name="Solar K-Index",
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:alpha-k",
    ),
    SensorEntityDescription(
        key="solar_bz",
        name="Solar Bz",
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:sun-compass",
    ),
    SensorEntityDescription(
        key="solar_wind",
        name="Solar Wind",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.WIND_SPEED,
        icon="mdi:sun-wireless",
        native_unit_of_measurement="km/s",
    ),
    SensorEntityDescription(
        key="solar_hf_80_40_day",
        name="HF Conditions 80m-40m Day",
        icon="mdi:sine-wave",
    ),
    SensorEntityDescription(
        key="solar_hf_30_20_day",
        name="HF Conditions 30m-20m Day",
        icon="mdi:sine-wave",
    ),
    SensorEntityDescription(
        key="solar_hf_17_15_day",
        name="HF Conditions 17m-15m Day",
        icon="mdi:sine-wave",
    ),
    SensorEntityDescription(
        key="solar_hf_12_10_day",
        name="HF Conditions 12m-10m Day",
        icon="mdi:sine-wave",
    ),
    SensorEntityDescription(
        key="solar_hf_80_40_night",
        name="HF Conditions 80m-40m Night",
        icon="mdi:sine-wave",
    ),
    SensorEntityDescription(
        key="solar_hf_30_20_night",
        name="HF Conditions 30m-20m Night",
        icon="mdi:sine-wave",
    ),
    SensorEntityDescription(
        key="solar_hf_17_15_night",
        name="HF Conditions 17m-15m Night",
        icon="mdi:sine-wave",
    ),
    SensorEntityDescription(
        key="solar_hf_12_10_night",
        name="HF Conditions 12m-10m Night",
        icon="mdi:sine-wave",
    ),
    SensorEntityDescription(
        key="solar_geomag_field",
        name="HF Conditions Geomag Field",
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:compass",
    ),
    SensorEntityDescription(
        key="solar_sig_noise_lvl",
        name="HF Conditions Noise Level",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.SIGNAL_STRENGTH,
        icon="mdi:signal-cellular-2",
    ),
)

SENSOR_KEYS: list[str] = [desc.key for desc in SENSOR_TYPES]

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Optional(CONF_NAME, default=NAME): cv.string,
    }
)


async def async_setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    async_add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    websession = async_get_clientsession(hass)

    ts_data = HamRadioData(hass.loop, websession)
    ret = await ts_data.async_update()
    if ret is False:
        LOGGER.error("Invalid data")
        return

    name = config[CONF_NAME]

    async_add_entities(
        [HamRadioSensor(ts_data, name, description) for description in SENSOR_TYPES],
        True,
    )


class HamRadioSensor(SensorEntity):
    """Representation of hamqsl.com sensor."""

    def __init__(
        self, hamradiodata: HamRadioData, name, description: SensorEntityDescription
    ) -> None:
        """Initialize the sensor."""
        if hamradiodata is None:
            LOGGER.error("Error empty client")
        self.entity_description = description
        self.hamradiodata = hamradiodata
        slug = slugify(description.key.replace("/", "_"))
        self.entity_id = f"sensor.{DOMAIN}_{slug}"
        self._attr_name = f"{description.name}"

    async def async_update(self) -> None:
        """Get the latest data from hamqsl.com and update the state."""
        await self.hamradiodata.async_update()
        sensor_type = self.entity_description.key
        if sensor_type in self.hamradiodata.data:
            self._attr_native_value = self.hamradiodata.data[sensor_type]


class HamRadioData:
    """Get data from hamqsl.com API."""

    def __init__(self, loop, websession):
        """Initialize the data object."""
        self.loop = loop
        self.websession = websession

        # Set unlimited users to infinite, otherwise the cap.
        self.data = {"limit": 0}

    @Throttle(MIN_TIME_BETWEEN_UPDATES)
    async def async_update(self):
        """Get the hamqsl.com data from the web service."""
        LOGGER.debug("Updating hamqsl.com data")
        url = "https://www.hamqsl.com/solarxml.php"
        async with async_timeout.timeout(REQUEST_TIMEOUT):
            req = await self.websession.get(url)
        if req.status != HTTPStatus.OK:
            LOGGER.error("Request failed with status: %u", req.status)
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
