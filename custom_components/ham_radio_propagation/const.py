"""HAM Radio Propagation."""
from datetime import timedelta
import logging


LOGGER = logging.getLogger(__package__)
MIN_TIME_BETWEEN_UPDATES = timedelta(hours=2)
REQUEST_TIMEOUT = 30  # seconds

# Base component constants
ATTRIBUTION = "Data provided by hamqsl.com"
DOMAIN = "ham_radio_propagation"
NAME = "HAM Radio Propagation"
MANUFACTURER = "emics"
VERSION = "0.1.4"
