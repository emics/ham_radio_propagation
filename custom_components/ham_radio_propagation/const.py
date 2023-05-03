"""HAM Radio Propagation."""
from datetime import timedelta
from typing import Final
from homeassistant.const import Platform
from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorStateClass,
    SensorEntityDescription,
)

MIN_TIME_BETWEEN_UPDATES = timedelta(hours=2)
REQUEST_TIMEOUT = 60  # seconds
PLATFORMS: Final = [Platform.SENSOR]

# URL
URL_STATIONS: Final = "https://www.bbgest.cloud/ham_radio_propagation/station_list.php"
URL_API: Final = "https://www.bbgest.cloud/ham_radio_propagation/api.php"

# Base component constants
DOMAIN: Final = "ham_radio_propagation"
NAME = "HAM Radio Propagation"
MANUFACTURER = "hamqsl.com and kc2g.com"
MODEL = "HAM Radio Propagation"
VERSION = "1.1.2"
CONFIGURATION_URL = "https://github.com/emics/ham_radio_propagation#readme"

TYPE_ONLY_SOLAR = "Configure solar data"
TYPE_ONLY_MUF = "Configure MUF from ionosonde data"
TYPE_ALL = "Configure full info available"

STATION_CODE = "station_code"
STATION_NAME = "station_name"
USER_STATION_CODE = "user_muf_station_code"
CHOICE = "choice"

ENTITY_SOLAR_TITLE = "Solar Data"

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
        icon="mdi:compass",
    ),
    SensorEntityDescription(
        key="solar_sig_noise_lvl",
        name="HF Conditions Noise Level",
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:signal-cellular-2",
    ),
    SensorEntityDescription(
        key="solar_fof2",
        name="Solar foF2",
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:format-vertical-align-top",
		native_unit_of_measurement="MHz",
    ),
)
