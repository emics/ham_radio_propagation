"""HAM Radio Propagation API Client."""
from __future__ import annotations

import asyncio
import json
import re
import socket
from datetime import date, datetime, time, timedelta

import aiohttp
import async_timeout


API_URL = "https://www.hamqsl.com/solarxml.php"