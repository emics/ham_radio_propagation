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

After adding a custom repository you can use HACS to install this integration using user interface.

1. Search for `Ham Radio`
2. Click the `INSTALL THIS REPOSITORY IN HACS` button
3. Restart Home Assistant

### Manual

To install this integration manually you have to download [*ham_radio_propagation.zip*](https://github.com/emics/ham_radio_propagation/archive/refs/heads/main.zip) and extract its contents to `config/custom_components/ham_radio_propagation` directory:

```bash
mkdir -p custom_components/ham_radio_propagation
cd custom_components/ham_radio_propagation
wget https://github.com/emics/ham_radio_propagation/archive/refs/heads/main.zip
unzip main.zip
rm main.zip
```

## Configuration

### Config flow

To configure this integration go to: `Configurations` -> `Integrations` -> `ADD INTEGRATIONS` button, search for `Ham Radio Propagation` and configure the component.

You can also use following [My Home Assistant](http://my.home-assistant.io/) link

[![Open your Home Assistant instance and start setting up a new integration.](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=ham_radio_propagation)

### Setup 

Now the integration is added to HACS and available in the normal HA integration installation

1. In the HomeAssistant left menu, click `Configuration`
2. Click `Integrations`
3. Click `ADD INTEGRATION`
4. Type `Ham Radio Propagation` and select it
5. Configure the Options
   * Update interval (minutes, default 120)

Once you done that, you’re ready to start.



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
