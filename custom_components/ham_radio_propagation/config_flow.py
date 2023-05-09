"""Config flow for Ham Radio Propagation integration."""
from __future__ import annotations

import logging
import json
import async_timeout
import voluptuous as vol
from http import HTTPStatus
from typing import Any

from homeassistant import core, exceptions
from homeassistant.config_entries import ConfigFlow
from homeassistant.const import CONF_NAME
from homeassistant.data_entry_flow import FlowResult
from homeassistant.helpers.selector import selector
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from .const import *

_LOGGER = logging.getLogger(__name__)


async def async_station_list_kc2g(hass: core.HomeAssistant) -> list:
    """Get the kc2g.com station list from the web service."""
    _LOGGER.debug("Get kc2g.com Station list")
    websession = async_get_clientsession(hass)
    lat = hass.config.latitude
    lon = hass.config.longitude
    async with async_timeout.timeout(REQUEST_TIMEOUT):
        req = await websession.get(f"{URL_BASE}{URL_STATIONS}?lat={lat}&lon={lon}")
    if req.status != HTTPStatus.OK:
        _LOGGER.error("Request failed with status: %u", req.status)
        return False
    data = await req.text()
    entries = json.loads(data)

    station_list = []
    for entry in entries:
        station_name: str = ""
        if entry["country"]:
            station_name += entry["country"] + " - "
        if entry["state"]:
            station_name += entry["state"] + " - "
        station_name += entry["city"]
        station_name += " [" + entry["code"] + "]"

        station_list.append(station_name.strip())

    return station_list


async def validate_input(
    hass: core.HomeAssistant, data: dict[str, Any]
) -> dict[str, str]:
    """Validate that the user input is correct.
    Data has the keys from DATA_SCHEMA with values provided by the user.
    """
    if USER_STATION_CODE in data:
        conf_station = data[USER_STATION_CODE]
        station_code = conf_station[
            conf_station.find("[") + len("[") : conf_station.rfind("]")
        ]
        station_name = (
            conf_station.replace("[" + station_code + "]", "").replace(",", "").strip()
        )
        data[STATION_CODE] = station_code
        data[STATION_NAME] = station_name
    else:
        data[STATION_CODE] = ""
        station_name = ENTITY_SOLAR_TITLE

    return {"site_name": station_name}


class HamRadioConfigFlow(ConfigFlow, domain=DOMAIN):
    """Handle a config flow for HAM Radio Propagation integration."""

    VERSION = 1
    _data: dict | None

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle the initial step."""
        only_solar_configured: bool = False
        instances = self._async_current_entries()
        for instance in instances:
            if instance.data[CHOICE] == TYPE_ONLY_SOLAR:
                only_solar_configured = True
                break

        # if self._async_current_entries():
        #    return self.async_abort(reason="single_instance_allowed")

        if only_solar_configured:
            data = {CHOICE: TYPE_ONLY_MUF}
        else:
            data_schema = vol.Schema(
                {
                    vol.Required(CHOICE, default=TYPE_ONLY_SOLAR): vol.In(
                        (
                            TYPE_ONLY_SOLAR,
                            TYPE_ONLY_MUF,
                            # TYPE_ALL,
                        )
                    )
                }
            )
            if user_input is None:
                return self.async_show_form(
                    step_id="user",
                    data_schema=data_schema,
                )
            data = {CHOICE: user_input[CHOICE]}

        if data[CHOICE] != TYPE_ONLY_SOLAR:
            self._data = data
            return await self.async_step_station()

        user_input[CONF_NAME] = ENTITY_SOLAR_TITLE
        await self.async_set_unique_id(f"{user_input[CONF_NAME]}")
        return self.async_create_entry(title=user_input[CONF_NAME], data=user_input)

    async def async_step_station(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle the station step."""
        if user_input is not None:
            info = await validate_input(self.hass, user_input)
            user_input[CONF_NAME] = info["site_name"]
            user_input[CHOICE] = self._data[CHOICE]
            await self.async_set_unique_id(f"{user_input['user_muf_station_code']}")

            return self.async_create_entry(title=user_input[CONF_NAME], data=user_input)

        else:
            station_list = await async_station_list_kc2g(self.hass)

        data_schema = {
            vol.Required(USER_STATION_CODE): selector(
                {
                    "select": {
                        "options": station_list,
                        "mode": "dropdown",
                    }
                }
            )
        }

        return self.async_show_form(
            step_id="station", data_schema=vol.Schema(data_schema)
        )


class CannotConnect(exceptions.HomeAssistantError):
    """Error to indicate we cannot connect."""
