# Changes

## v1.1.2 (02/05/2023)
New feature available:
* Added **foF2** (The highest frequency which the ionosphere will reflect vertically) sensor. [thanks to toni SA6EAL]
* Added notification if the **MUF station configured** don't receive data.

Enjoy 73 de IZ0IJD

## v1.1.0 (05/04/2023)
In this version we can find small but really interesting improvements.

### Faster
Now the data is cached on my server, the traffic to _hamqsl_ and _kc2g_  API is reduced and the integration update is faster.
### New Station List
Adding a new station is now great, the stations in the list are sorted by the nearest ionsonde according to the location you set in Home Assistant.
### Only Fresh Data
Old Ionosonde are automatically deleted from the list and only stations with data from the last 30 days are displayed and selectable.

Enjoy
73 de IZ0IJD

## v1.0.0 (24/03/2023)
* New MAJOR RELEASE with a complete refactoring and Config Flow for fastest installation and configuration directly in the Integration Page

   [![Open your Home Assistant instance and start setting up a new integration.](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=ham_radio_propagation)

* Complete Solar info from www.hamqsl.com
* Retrieve multiple MUF data from kc2g.com

### Bug Fix
* Removed DeviceClass attribute for `solar_wind` and `sig_noise_lvl` sensors
* Removed StateClass attribute for `geomag_field` sensor

Enjoy
73 de IZ0IJD

## v0.1.5 (14/03/2023)
This release is created after HACS Validation.
With this release the validation check from HACS procedure is complete, I have submitted the request and I hope this repository to be included in default repository in the store.

Enjoy
73 de IZ0IJD

## v0.1.4 (01/03/2023)
First stable release!
* All sensor mapped

Enjoy!
73 de IZ0IJD - emics