"""Platform for sensor integration."""
from __future__ import annotations

from typing import Any
from homeassistant.const import DOMAIN
from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType


SENSOR_TYPES: tuple[SensorEntityDescription, ...] = (
    SensorEntityDescription(
        key="ham_solar_flux_index",
        name="Solar Flux Index",
        icon="mdi:weather-sunny-alert",
    ),
    SensorEntityDescription(
        key="ham_solar_sunspots",
        name="Solar Sunspot",
        icon="mdi:weather-sunny-alert",
    ),
    SensorEntityDescription(
        key="solar_hf_80_40_day",
        name="HF Conditions 80m-40m Day",
        icon="mdi:sine-wave",
    ),
)

def setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None
) -> None:
    """Set up the sensor platform."""
    add_entities([ExampleSensor()])


class ExampleSensor(SensorEntity):
    """Representation of a Sensor."""

    _attr_name = "Example Temperature"
    _attr_native_unit_of_measurement = TEMP_CELSIUS
    _attr_device_class = SensorDeviceClass.TEMPERATURE
    _attr_state_class = SensorStateClass.MEASUREMENT

    def update(self) -> None:
        """Fetch new state data for the sensor.
        This is the only method that should fetch new data for Home Assistant.
        """
        self._attr_native_value = 23

#
#async def async_setup_entry(
#    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
#) -> None:
#    """Set up the HAM sensor."""
#    name = entry.data[CONF_NAME]
#    hole_data = hass.data[DOMAIN][entry.entry_id]
#    sensors = [
#        HamSensor(
#            hole_data[DATA_KEY_API],
#            hole_data[DATA_KEY_COORDINATOR],
#            name,
#            entry.entry_id,
#            description,
#        )
#        for description in SENSOR_TYPES
#    ]
#    async_add_entities(sensors, True)
#	
#class HamSensor(PiHoleEntity, SensorEntity):
#    """Representation of a HAM sensor."""
#
#    entity_description: SensorEntityDescription
#
#    def __init__(
#        self,
#        api: Hole,
#        coordinator: DataUpdateCoordinator,
#        name: str,
#        server_unique_id: str,
#        description: SensorEntityDescription,
#    ) -> None:
#        """Initialize a Pi-hole sensor."""
#        super().__init__(api, coordinator, name, server_unique_id)
#        self.entity_description = description
#
#        self._attr_name = f"{name} {description.name}"
#        self._attr_unique_id = f"{self._server_unique_id}/{description.name}"
#
#    @property
#    def native_value(self) -> Any:
#        """Return the state of the device."""
#        try:
#            return round(self.api.data[self.entity_description.key], 2)
#        except TypeError:
#            return self.api.data[self.entity_description.key]