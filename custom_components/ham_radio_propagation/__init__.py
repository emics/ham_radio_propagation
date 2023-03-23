"""The Ham Radio Propagation component."""
from __future__ import annotations

from collections.abc import Callable
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from .const import PLATFORMS


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up from a config entry."""
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)


async def async_update_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Reload HAM Data Propagation component when options changed."""
    await hass.config_entries.async_reload(entry.entry_id)
