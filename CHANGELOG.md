# Changes

## v1.1.5 (16/05/2023)
* added new solar X-Ray sensors Class and Scale.
   * The **Class** sensor is the modern classification system for solar flares and use letters A, B, C, M, or X, according to the peak flux in watts per square metre (W/m2)
   * The **Scale** sensor is the numerical representation of the Class sensor and can be used to trigger automations and notifications.

### Class to Scale sensor translation example
| Class | Scale | Factor |
|---|---:|---:|
| `A1.1` | 1.1 | x1 |
| `A5.1` | 5.1 | x1 |
| `B1.4` | 14 | x10 |
| `B8.7` | 87 | x10 |
| `C2.5` | 250 | x100 |
| `C7.9` | 790 | x100 |
| `M2.3` | 2300 | x1000 |
| `M5.2` | 5200 | x1000 |
| `M7.3` | 7300 | x1000 |
| `X1.7` | 11000 | x10000 |
| `X3.7` | 37000 | x10000 |
| `X6.9` | 69000 | x10000 |

> This new senors are updated every 10 minutes, others every hour.

## v1.1.4 (10/05/2023)
### What's Changed
* added instructions to restart Home Assistant after HACS installation 
* added traslation (DE - ES - FR - NL - PL - SE)
* added new sensor foF2 and foE from ionosonde


## v1.1.3 (05/05/2023)
### What's Changed
* added Toni as contributor 
* Create pt.json by @ViPeR5000 
* Create it.json 

### New Contributors
* @emics made their first contribution in https://github.com/emics/ham_radio_propagation/pull/4
* @ViPeR5000 made their first contribution in https://github.com/emics/ham_radio_propagation/pull/5
## v1.1.2 (02/05/2023)
New features available:
* Added **foF2** (The highest frequency which the ionosphere will reflect vertically) sensor. [thanks to toni SA6EAL]
* Added notification if the **MUF station configured** don't receive data.

## v1.1.0 (05/04/2023)
In this version we can find small but really interesting improvements.

### Faster
Now the data is cached on my server, the traffic to _hamqsl_ and _kc2g_  API is reduced and the integration update is faster.
### New Station List
Adding a new station is now great, the stations in the list are sorted by the nearest ionsonde according to the location you set in Home Assistant.
### Only Fresh Data
Old Ionosonde are automatically deleted from the list and only stations with data from the last 30 days are displayed and selectable.


## v1.0.0 (24/03/2023)
* New MAJOR RELEASE with a complete refactoring and Config Flow for fastest installation and configuration directly in the Integration Page

   [![Open your Home Assistant instance and start setting up a new integration.](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=ham_radio_propagation)

* Complete Solar info from www.hamqsl.com
* Retrieve multiple MUF data from kc2g.com

### Bug Fix
* Removed DeviceClass attribute for `solar_wind` and `sig_noise_lvl` sensors
* Removed StateClass attribute for `geomag_field` sensor

## v0.1.5 (14/03/2023)
This release is created after HACS Validation.
With this release the validation check from HACS procedure is complete, I have submitted the request and I hope this repository to be included in default repository in the store.

## v0.1.4 (01/03/2023)
First stable release!
* All sensor mapped
