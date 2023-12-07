# HAM Radio Propagation for Home Assistant

![Logo](https://raw.githubusercontent.com/emics/ham_radio_propagation/main/assets/brand/logo_wide.png)

[![GitHub Release][releases-shield]][releases]
[![License][license-shield]](LICENSE)
[![GitHub Activity][commits-shield]][commits]

[![hacs][hacsbadge]][hacs]
[![Project Maintenance][maintenance-shield]][user_profile]
[![Community Forum][forum-shield]][forum]

![Active Installations](https://img.shields.io/endpoint?url=https://www.bbgest.cloud/ham_radio_propagation/shield.php&style=for-the-badge)

[![BuyMeCoffee][buymecoffeebadge]][buymecoffee]

[![Telegram][telegram-badge]][telegram-group]

## Introduction
Welcome to my repository Home Assistant - Custom Component for HAM Radio Propagation connected to the [hamqsl.com][hamqsl] and [kc2g.com][kc2g] API.

---

## Installation

### Using HACS [Home Assistant Community Store](https://hacs.xyz/) (recommended)

Click on the button below to automatically navigate to the repository within HACS:

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=emics&repository=ham_radio_propagation&category=integration)

Alternatively, follow the steps below:

1. Go to HACS "Integrations >" section
2. In the lower right click `+ Explore & Download repositories`
3. Search for "HAM Radio" and add it
4. Restart Home Assistant.


### Manual installation

* Using the tool of choice open the directory (folder) for your HA configuration (where you find `configuration.yaml`).
* If you do not have a `custom_components` directory (folder) there, you need to create it.
* In the `custom_components` directory (folder) create a new folder called `ham_radio_propagation`.
* Download file `ham_radio_propagation.zip` from the [latest release section][releases-latest] in this repository.
* Extract _all_ files from this archive you downloaded in the directory (folder) you created.
* Restart Home Assistant.


## Configuration

Click on the button below to add the integration:

  [![Open your Home Assistant instance and start setting up a new integration.](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=ham_radio_propagation)

Alternatively, follow the steps below:

1. Install this integration.
2. Navigate to the Home Assistant Integrations page (Settings --> Devices & Services)
3. Click the `+ ADD INTEGRATION` button in the lower right-hand corner
4. Search for `HAM`

    ![Brand List](https://raw.githubusercontent.com/emics/ham_radio_propagation/main/assets/brand_list.png)

5. Select if you want to start the configuration through 
    * Solar Data
    * MUF from ionosonde data

    ![Step 1](https://raw.githubusercontent.com/emics/ham_radio_propagation/main/assets/config_step_1.png)

6. If your choice is MUF option you can select a Station from the dropdown list. Select the station nearest your location for best result. 

    ![Step 2](https://raw.githubusercontent.com/emics/ham_radio_propagation/main/assets/config_step_2.png)


> You can do this steps as many times as you want and configure multiple MUF Station in the same Integration

![Step 3](https://raw.githubusercontent.com/emics/ham_radio_propagation/main/assets/config_step_3.png)


### Dashboard

You can go in the Device page and at the bottom click `ADD TO DASHBOARD`

![Device Solar](https://raw.githubusercontent.com/emics/ham_radio_propagation/main/assets/device_solar.png)

#### Manual

Add an Entities Card and paste this code.

```yaml
type: entities
entities:
  - entity: sensor.ham_radio_propagation_solar_hf_12_10_day
    name: HF Conditions 12m-10m Day
  - entity: sensor.ham_radio_propagation_solar_hf_12_10_night
    name: HF Conditions 12m-10m Night
  - entity: sensor.ham_radio_propagation_solar_hf_17_15_day
    name: HF Conditions 17m-15m Day
  - entity: sensor.ham_radio_propagation_solar_hf_17_15_night
    name: HF Conditions 17m-15m Night
  - entity: sensor.ham_radio_propagation_solar_hf_30_20_day
    name: HF Conditions 30m-20m Day
  - entity: sensor.ham_radio_propagation_solar_hf_30_20_night
    name: HF Conditions 30m-20m Night
  - entity: sensor.ham_radio_propagation_solar_hf_80_40_day
    name: HF Conditions 80m-40m Day
  - entity: sensor.ham_radio_propagation_solar_hf_80_40_night
    name: HF Conditions 80m-40m Night
  - entity: sensor.ham_radio_propagation_solar_geomag_field
    name: HF Conditions Geomag Field
  - entity: sensor.ham_radio_propagation_solar_sig_noise_lvl
    name: HF Conditions Noise Level
  - entity: sensor.ham_radio_propagation_solar_a_index
    name: Solar A-Index
  - entity: sensor.ham_radio_propagation_solar_bz
    name: Solar Bz
  - entity: sensor.ham_radio_propagation_solar_flux_index
    name: Solar Flux Index
  - entity: sensor.ham_radio_propagation_solar_fof2
    name: Solar foF2
  - entity: sensor.ham_radio_propagation_solar_k_index
    name: Solar K-Index
  - entity: sensor.ham_radio_propagation_solar_sunspots
    name: Solar Sunspots
  - entity: sensor.ham_radio_propagation_solar_wind
    name: Solar Wind
  - entity: sensor.ham_radio_propagation_solar_xray
    name: Solar xRay Class
  - entity: sensor.ham_radio_propagation_solar_xray_scale
    name: Solar xRay Scale
title: Solar Data
```

This is the card result:

![Entity Card](https://raw.githubusercontent.com/emics/ham_radio_propagation/main/assets/entity_list.png)

#### CSS Card
Thanks to our friend Mikko a [special card with CSS](https://github.com/emics/ham_radio_propagation/blob/main/MIKKO_CSS.md) to visualize data.


# How To section

[How to read sensor value](https://github.com/emics/ham_radio_propagation/blob/main/SENSOR.md)

[Solar Flux Index](https://github.com/emics/ham_radio_propagation/blob/main/SENSOR.md#solar-flux-index)

[Solar A-Index](https://github.com/emics/ham_radio_propagation/blob/main/SENSOR.md#solar-a-index)

[Solar K-Index](https://github.com/emics/ham_radio_propagation/blob/main/SENSOR.md#solar-k-index)

[Solar X-Ray ](https://github.com/emics/ham_radio_propagation/blob/main/SENSOR.md#solar-x-ray)

[Solar Flare Notification](https://github.com/emics/ham_radio_propagation/blob/main/SENSOR.md#solar-flare-notification)






<p align="center">* * *</p>

## Contributions are welcome!

This is an active open-source project. We are always open to people who want to use the code or contribute to it.

We have set up a separate document containing our [contribution guidelines][contribution].

Thank you for being involved! :heart_eyes:

Special thanks to:
- [@kwirk](https://community.home-assistant.io/u/kwirk)
- [@dragonjon](https://github.com/dragonjon)
- [@Toni](https://www.qrz.com/db/SA6EAL)
- [@ViPeR5000](https://github.com/ViPeR5000)
- [@CT2HUU](https://github.com/CT2HUU)
- @Mikko (Telegram contributor)

---

## Trademark Legal Notices

All product names, trademarks and registered trademarks in the images in this repository, are property of their respective owners.
All images in this repository are used by the author for identification purposes only.
The use of these names, trademarks and brands appearing in these image files, do not imply endorsement.

<!--- hacs -->
[hacs]: https://github.com/custom-components/hacs
[hacsbadge]: https://img.shields.io/badge/HACS-Default-cyan.svg?style=for-the-badge

[commits-shield]: https://img.shields.io/github/last-commit/emics/ham_radio_propagation?color=pink&style=for-the-badge
[commits]: https://github.com/emics/ham_radio_propagation/commits/dev
[releases-shield]: https://img.shields.io/github/release/emics/ham_radio_propagation.svg?style=for-the-badge
[releases]: https://github.com/emics/ham_radio_propagation/releases
[releases-latest]: https://github.com/emics/ham_radio_propagation/releases/latest
[user_profile]: https://github.com/emics
[license-shield]: https://img.shields.io/github/license/emics/ham_radio_propagation.svg?color=yellow&style=for-the-badge
[maintenance-shield]: https://img.shields.io/badge/maintainer-%40emics-orange.svg?style=for-the-badge
[contribution]: https://github.com/emics/ham_radio_propagation/blob/main/CONTRIBUTING.md


<!--- External Link -->
[hamqsl]: http://www.hamqsl.com/
[kc2g]: https://prop.kc2g.com/

[buymecoffee]: https://www.buymeacoffee.com/emics
[buymecoffeebadge]: https://img.buymeacoffee.com/button-api/?text=Buy%20me%20a%20coffee&emoji=&slug=emics&button_colour=FFDD00&font_colour=000000&font_family=Cookie&outline_colour=000000&coffee_colour=ffffff
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg?style=for-the-badge
[forum]: https://community.home-assistant.io/t/custom-component-ham-radio-propagation/547664
[telegram-badge]: https://img.shields.io/static/v1?label=telegram&message=support%20chat&color=informational&style=for-the-badge&logo=telegram
[telegram-group]: https://t.me/+SbSwDkEPwFFkZDlk