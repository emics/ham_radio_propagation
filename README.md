# HAM Radio Propagation for Home Assistant

Welcome to my repository Home Assistant - Custom Component for HAM Radio Propagation connected to the [hamqsl.com][hamqsl] API.

[![Don't buy me a coffee](https://img.shields.io/static/v1.svg?label=Don't%20buy%20me%20a%20coffee&message=🔔&color=black&logo=buy%20me%20a%20coffee&logoColor=white&labelColor=6f4e37)](https://paypal.me/macedonio)
---

## Introduction

> The goal is to integrate the data from hamqsl.com APIs in a custom component in Home Assistant.
> This custom component is still in the development/testing phase. 
> Bugs are still being worked out and breaking changes are common.

## Installation

### Using [Home Assistant Community Store](https://hacs.xyz/) (recommended)

This integration can be added to HACS as a [custom repository](https://hacs.xyz/docs/faq/custom_repositories):

* URL: `https://github.com/emics/ham_radio_propagation`
* Category: `Integration`

Once downloaded and configured as per below information, you'll need to restart HomeAssistant to have the custom component and the sensors of ztm platform taken into consideration.

Then add the data to your `configuration.yaml` file as shown in the example:

```yaml
# Example configuration.yaml entry
sensor:
  - platform: ham_radio_propagation
```

## Configuration
This Integration don't require configuration

## Contributions are welcome

---

## Trademark Legal Notices

All product names, trademarks and registered trademarks in the images in this repository, are property of their respective owners.
All images in this repository are used by the author for identification purposes only.
The use of these names, trademarks and brands appearing in these image files, do not imply endorsement.

<!--- hacs -->
[hacs]: https://github.com/custom-components/hacs
[hacs_faq_custom]: https://hacs.xyz/docs/faq/custom_repositories
[hacs_custom]: https://img.shields.io/badge/HACS-Custom-41BDF5.svg
[hacs_integration]: https://github.com/hacs/integration

<!--- External Link -->
[hamqsl]: http://www.hamqsl.com/
