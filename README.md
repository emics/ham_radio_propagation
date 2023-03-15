# HAM Radio Propagation for Home Assistant

![Logo](https://raw.githubusercontent.com/emics/ham_radio_propagation/main/assets/brand/logo.png)

[![GitHub Release][releases-shield]][releases]
[![License][license-shield]](LICENSE)
[![GitHub Activity][commits-shield]][commits]

[![hacs][hacsbadge]][hacs]
[![Project Maintenance][maintenance-shield]][user_profile]
[![Community Forum][forum-shield]][forum]

[![BuyMeCoffee][buymecoffeebadge]][buymecoffee]


Welcome to my repository Home Assistant - Custom Component for HAM Radio Propagation connected to the [hamqsl.com][hamqsl] API.

---

## Introduction

> The goal is to integrate the data from [hamqsl.com][hamqsl] APIs in a custom component in Home Assistant.
> This custom component is still in the development/testing phase. 
> Bugs are still being worked out and breaking changes are common.

## Installation

### Using [Home Assistant Community Store](https://hacs.xyz/) (recommended)

This integration can be added to HACS as a [custom repository](https://hacs.xyz/docs/faq/custom_repositories):

* URL: `https://github.com/emics/ham_radio_propagation`
* Category: `Integration`

Once downloaded and configured as per below information, you'll need to restart HomeAssistant to have the custom component and the sensors of ham_radio_propagation platform taken into consideration.

### Manual installation

* Using the tool of choice open the directory (folder) for your HA configuration (where you find `configuration.yaml`).
* If you do not have a `custom_components` directory (folder) there, you need to create it.
* In the `custom_components` directory (folder) create a new folder called `ham_radio_propagation`.
* Download file `Source code.zip` from the [latest release section][releases-latest] in this repository.
* Extract _all_ files from this archive you downloaded in the directory (folder) you created.

... then if you want to use `configuration.yaml` to configure sensor...



## Configuration
### Platform
Add `ham_radio_propagation` sensor to your `configuration.yaml` file. See configuration examples below.
Restart Home Assistant


```yaml
# Example configuration.yaml entry
sensor:
  - platform: ham_radio_propagation
```
### Dashboard
Add an Entities Card and paste this code.

```yaml
type: entities
entities:
  - entity: sensor.ham_radio_propagation_solar_flux_index
  - entity: sensor.ham_radio_propagation_solar_sunspots
  - entity: sensor.ham_radio_propagation_solar_a_index
  - entity: sensor.ham_radio_propagation_solar_k_index
  - entity: sensor.ham_radio_propagation_solar_bz
  - entity: sensor.ham_radio_propagation_solar_wind
  - entity: sensor.ham_radio_propagation_solar_hf_80_40_day
  - entity: sensor.ham_radio_propagation_solar_hf_80_40_night
  - entity: sensor.ham_radio_propagation_solar_hf_30_20_day
  - entity: sensor.ham_radio_propagation_solar_hf_30_20_night
  - entity: sensor.ham_radio_propagation_solar_hf_17_15_day
  - entity: sensor.ham_radio_propagation_solar_hf_17_15_night
  - entity: sensor.ham_radio_propagation_solar_hf_12_10_day
  - entity: sensor.ham_radio_propagation_solar_hf_12_10_night
  - entity: sensor.ham_radio_propagation_solar_geomag_field
  - entity: sensor.ham_radio_propagation_solar_sig_noise_lvl
title: HAM Radio Propagation
```

This is the result:

![Entity Card](https://raw.githubusercontent.com/emics/ham_radio_propagation/main/assets/entity_list.png)

<p align="center">* * *</p>

## Contributions are welcome!

This is an active open-source project. We are always open to people who want to use the code or contribute to it.

We have set up a separate document containing our [contribution guidelines][contribution].

Thank you for being involved! :heart_eyes:

---

## Trademark Legal Notices

All product names, trademarks and registered trademarks in the images in this repository, are property of their respective owners.
All images in this repository are used by the author for identification purposes only.
The use of these names, trademarks and brands appearing in these image files, do not imply endorsement.

<!--- hacs -->
[hacs]: https://github.com/custom-components/hacs
[hacsbadge]: https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge
[hacs_faq_custom]: https://hacs.xyz/docs/faq/custom_repositories
[hacs_custom]: https://img.shields.io/badge/HACS-Custom-41BDF5.svg
[hacs_integration]: https://github.com/hacs/integration
[commits-shield]: https://img.shields.io/github/last-commit/emics/ham_radio_propagation?style=for-the-badge
[commits]: https://github.com/emics/ham_radio_propagation/commits/dev
[releases-shield]: https://img.shields.io/github/release/emics/ham_radio_propagation.svg?style=for-the-badge
[releases]: https://github.com/emics/ham_radio_propagation/releases
[releases-latest]: https://github.com/emics/ham_radio_propagation/releases/latest
[user_profile]: https://github.com/emics
[license-shield]: https://img.shields.io/github/license/emics/ham_radio_propagation.svg?style=for-the-badge
[maintenance-shield]: https://img.shields.io/badge/maintainer-%40emics-blue.svg?style=for-the-badge
[contribution]: https://github.com/emics/ham_radio_propagation/blob/main/CONTRIBUTING.md



<!--- External Link -->
[hamqsl]: http://www.hamqsl.com/
[buymecoffee]: https://www.buymeacoffee.com/emics
[buymecoffeebadge]: https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg?style=for-the-badge
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg?style=for-the-badge
[forum]: https://community.home-assistant.io/t/custom-component-ham-radio-propagation/547664
