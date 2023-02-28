"""Platform for sensor integration."""
from __future__ import annotations

from typing import Any

from homeassistant.components.sensor import SensorEntity, SensorEntityDescription
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator


SENSOR_TYPES: tuple[SensorEntityDescription, ...] = (
    SensorEntityDescription(
        key="ham_solarflux",
        name="SolarFLux",
        native_unit_of_measurement="sfi",
        icon="mdi:close-octagon-outline",
    ),
    SensorEntityDescription(
        key="ham_sunspots",
        name="Sunspots",
        native_unit_of_measurement="sn",
        icon="mdi:close-octagon-outline",
    ),
    SensorEntityDescription(
        key="ham_xray",
        name="Xray",
        native_unit_of_measurement="xray",
        icon="mdi:account-outline",
    ),
)

async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    """Set up the HAM sensor."""
    name = entry.data[CONF_NAME]
    hole_data = hass.data[DOMAIN][entry.entry_id]
    sensors = [
        HamSensor(
            hole_data[DATA_KEY_API],
            hole_data[DATA_KEY_COORDINATOR],
            name,
            entry.entry_id,
            description,
        )
        for description in SENSOR_TYPES
    ]
    async_add_entities(sensors, True)
	
class HamSensor(PiHoleEntity, SensorEntity):
    """Representation of a HAM sensor."""

    entity_description: SensorEntityDescription

    def __init__(
        self,
        api: Hole,
        coordinator: DataUpdateCoordinator,
        name: str,
        server_unique_id: str,
        description: SensorEntityDescription,
    ) -> None:
        """Initialize a Pi-hole sensor."""
        super().__init__(api, coordinator, name, server_unique_id)
        self.entity_description = description

        self._attr_name = f"{name} {description.name}"
        self._attr_unique_id = f"{self._server_unique_id}/{description.name}"

    @property
    def native_value(self) -> Any:
        """Return the state of the device."""
        try:
            return round(self.api.data[self.entity_description.key], 2)
        except TypeError:
            return self.api.data[self.entity_description.key]