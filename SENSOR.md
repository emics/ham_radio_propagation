# How to read sensor value 
The three main items you want to pay attention to are the **SFI** (Solar Flux Index), the **K-Index** and the **A-Index**.

## Solar Flux Index
Summarization of the Sun's Radiation Output
* 70 – Not Good
* 80 – Good
* 90 – Better
* 100+ – Best


## Solar A-Index 
Daily Average of Magnetic Activity
* 0 – 7 Quiet
* 8 – 15 Unsettled
* 16 – 29 Active
* 30 – 49 Minor storm
* 50 – 99 Major storm
* 100 – 400 Severe storm


## Solar K-Index 
<sub>Updated every Hour</sub>
* 0 Inactive
* 1 Very quiet
* 2 Quiet
* 3 Unsettled
* 4 Active
* 5 Minor storm
* 6 Major storm
* 7 Severe storm
* 8 Very severe storm
* 9 Extremely severe storm

## Solar X-Ray 
<sub>Updated every 10 minutes</sub>

The **Class** sensor is the modern classification system for solar flares and use letters A, B, C, M, or X, according to the peak flux in watts per square metre (W/m2).

The **Scale** sensor is the numerical representation of the Class sensor and can be used to trigger automations and notifications.

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

### Solar Graph
NOAA X-Ray data is very accurate (update every 10 minutes).
In this graph you can see a spike with M9.1 solar Activity

![xray-graph](https://raw.githubusercontent.com/emics/ham_radio_propagation/main/assets/xray-graph.png)


## Solar Flare Notification
For solar flare notification you can create an Automation, this example send an alert to your companion App on your phone with custom message.

Under Settings -> Automation create new and configure  with this Trigger:
```yaml
platform: numeric_state
entity_id: sensor.ham_radio_propagation_solar_xray_scale
above: 1000
```

![autom-sunflare1](https://raw.githubusercontent.com/emics/ham_radio_propagation/main/assets/autom-sunflare1.png)

and this Actions, modify the name of your device and the message:
```yaml
service: notify.mobile_app_iphone_di_emiliano
data:
  message: >-
    High solar activity Class: {{
    states('sensor.ham_radio_propagation_solar_xray') }}
  title: Smart Home Alert
```

![autom-sunflare2](https://raw.githubusercontent.com/emics/ham_radio_propagation/main/assets/autom-sunflare2.png)
