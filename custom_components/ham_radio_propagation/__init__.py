"""HAM Radio Propagation."""
from __future__ import annotations

import asyncio

from homeassistant import core
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType


async def async_setup(hass: core.HomeAssistant, config: dict) -> bool:
    """Set up the HAM Radio Propagation component."""
    # @TODO: Add setup code.
    return True
