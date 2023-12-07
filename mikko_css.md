# Custom CSS card thankx to @Mikko
Our friend share on [HRP Telegram Channel](https://t.me/+SbSwDkEPwFFkZDlk) an awesome card for data visualization.


![Device Solar](https://raw.githubusercontent.com/emics/ham_radio_propagation/main/assets/mikko-css.jpg)
 

The first card Overall propagation
```yaml
type: markdown
title: Overall propagation
content: >-
    <table>   
    <tr>
    <td></td><td><h3>10m-12m&nbsp;&nbsp;</h3></td><td><h3>15m-17m&nbsp;&nbsp;</h3></td><td><h3>20m-30m&nbsp;&nbsp;</h3></td><td><h3>40m-80m&nbsp;&nbsp;</h3></td>
    </tr>    
    <tr>     
    <td><h3>Day</h3></td>   
    <td><center><font color="{% if is_state('sensor.ham_radio_propagation_solar_hf_12_10_day', 'Good') %} #008000 {% elif is_state('sensor.ham_radio_propagation_solar_hf_12_10_day', 'Fair') %} #ffff00 {% elif is_state('sensor.ham_radio_propagation_solar_hf_12_10_day', 'Poor') %} #ff0000 {% endif %}"><h3>{{ states('sensor.ham_radio_propagation_solar_hf_12_10_day') }}</h3></font></center></td>     
    <td><center><font color="{% if is_state('sensor.ham_radio_propagation_solar_hf_17_15_day', 'Good') %} #008000 {% elif is_state('sensor.ham_radio_propagation_solar_hf_17_15_day', 'Fair') %} #ffff00 {% elif is_state('sensor.ham_radio_propagation_solar_hf_17_15_day', 'Poor') %} #ff0000 {% endif %}"><h3>{{ states('sensor.ham_radio_propagation_solar_hf_17_15_day') }}</h3></font></center></td>   
    <td><center><font color="{% if is_state('sensor.ham_radio_propagation_solar_hf_30_20_day', 'Good') %} #008000 {% elif is_state('sensor.ham_radio_propagation_solar_hf_30_20_day', 'Fair') %} #ffff00 {% elif is_state('sensor.ham_radio_propagation_solar_hf_30_20_day', 'Poor') %} #ff0000 {% endif %}"><h3>{{ states('sensor.ham_radio_propagation_solar_hf_30_20_day') }}</h3></font></center></td>   
    <td><center><font color="{% if is_state('sensor.ham_radio_propagation_solar_hf_80_40_day', 'Good') %} #008000 {% elif is_state('sensor.ham_radio_propagation_solar_hf_80_40_day', 'Fair') %} #ffff00 {% elif is_state('sensor.ham_radio_propagation_solar_hf_80_40_day', 'Poor') %} #ff0000 {% endif %}"><h3>{{ states('sensor.ham_radio_propagation_solar_hf_80_40_day') }}</h3></font></center></td>   
    </tr>    
    <tr>   
    <td><h3>Night</h3></td>    
    <td><center><font color="{% if is_state('sensor.ham_radio_propagation_solar_hf_12_10_night', 'Good') %} #008000 {% elif is_state('sensor.ham_radio_propagation_solar_hf_12_10_night', 'Fair') %} #ffff00 {% elif is_state('sensor.ham_radio_propagation_solar_hf_12_10_night', 'Poor') %} #ff0000 {% else %} black {% endif %}"><h3>{{ states('sensor.ham_radio_propagation_solar_hf_12_10_night') }}</h3></font></center></td>     
    <td><center><font color="{% if is_state('sensor.ham_radio_propagation_solar_hf_17_15_night', 'Good') %} #008000 {% elif is_state('sensor.ham_radio_propagation_solar_hf_17_15_night', 'Fair') %} #ffff00 {% elif is_state('sensor.ham_radio_propagation_solar_hf_17_15_night', 'Poor') %} #ff0000 {% else %} black {% endif %}"><h3>{{ states('sensor.ham_radio_propagation_solar_hf_17_15_night') }}</h3></font></center></td>   
    <td><center><font color="{% if is_state('sensor.ham_radio_propagation_solar_hf_30_20_night', 'Good') %} #008000 {% elif is_state('sensor.ham_radio_propagation_solar_hf_30_20_night', 'Fair') %} #ffff00 {% elif is_state('sensor.ham_radio_propagation_solar_hf_30_20_night', 'Poor') %} #ff0000 {% else %} black {% endif %}"><h3>{{ states('sensor.ham_radio_propagation_solar_hf_30_20_night') }}</h3></font></center></td>   
    <td><center><font color="{% if is_state('sensor.ham_radio_propagation_solar_hf_80_40_night', 'Good') %} #008000 {% elif is_state('sensor.ham_radio_propagation_solar_hf_80_40_night', 'Fair') %} #ffff00 {% elif is_state('sensor.ham_radio_propagation_solar_hf_80_40_night', 'Poor') %} #ff0000 {% else %} black {% endif %}"><h3>{{ states('sensor.ham_radio_propagation_solar_hf_80_40_night') }}</h3></font></center></td>   
    </tr>    
    </table>
```

and the second one Solar Data
```yaml
type: markdown
title: Solar data
content: >-
    <table>   
    <tr>    
    <td><h2>A index&nbsp;&nbsp;&nbsp;&nbsp;</h2></td><td><h2>Flux index&nbsp;&nbsp;&nbsp;&nbsp;</h2></td><td><h2>K index&nbsp;&nbsp;&nbsp;&nbsp;</h2></td><td><h2>Sunspots&nbsp;&nbsp;&nbsp;&nbsp;</h2></td> 
    </tr>   
    <tr>    
    <td><h2><center><ha-icon icon="mdi:alpha-a"></ha-icon>&nbsp;&nbsp;&nbsp;&nbsp;</center></h2></td><td><h2><center><ha-icon icon="mdi:weather-sunny-alert"></ha-icon>&nbsp;&nbsp;&nbsp;&nbsp;</center></h2></td><td><h2><center><ha-icon icon="mdi:alpha-k"></ha-icon>&nbsp;&nbsp;&nbsp;&nbsp;</center></h2></td><td><h2><center><ha-icon icon="mdi:weather-sunny-alert"></ha-icon>&nbsp;&nbsp;&nbsp;&nbsp;</center></h2></td> 
    </tr>   
    <tr>    
    <td><center><font color="
    {% set val = states('sensor.ham_radio_propagation_solar_a_index') | int %} 
    {% if val < 8 %} #008000 
    {% elif val > 7 and val < 48 %} #bbdb44 
    {% elif val > 47 and val < 80 %} #ffc100 
    {% elif val > 79 and val < 132 %} #ff9a00 
    {% elif val > 131 and val < 208 %} #ff7400 
    {% elif val > 207 %} #ff0000 
    {% else %} black 
    {% endif %} 
    "><h2>{{ states('sensor.ham_radio_propagation_solar_a_index') }} &nbsp;&nbsp;&nbsp;&nbsp;</h2></font></center></td>
    
    <td><center><font color="
    {% set val = states('sensor.ham_radio_propagation_solar_flux_index') | int %} 
    {% if val < 118 %} #ff0000 
    {% elif val > 117 and val < 175 %} #ff7400
    {% elif val > 174 and val < 232 %} #ff9a00 
    {% elif val > 231 and val < 289 %} #ffc100
    {% elif val > 288 and val < 345 %} #bbdb44 
    {% elif val > 344 %} #008000
    {% else %} black 
    {% endif %} 
    "><h2>{{ states('sensor.ham_radio_propagation_solar_flux_index') }}&nbsp;&nbsp;&nbsp;&nbsp;</h2></font></center></td>  
    
    <td><center><font color="
    {% set val = states('sensor.ham_radio_propagation_solar_k_index') | int %} 
    {% if val < 3 %} #008000 
    {% elif val > 2 and val < 5 %} #bbdb44 
    {% elif val == 5 %} #ffc100 
    {% elif val == 6 %} #ff9a00 
    {% elif val == 7 %} #ff7400 
    {% elif val > 7 %} #ff0000 
    {% else %} black 
    {% endif %} 

    "><h2>{{ states('sensor.ham_radio_propagation_solar_k_index') }}&nbsp;&nbsp;&nbsp;&nbsp;</h2></font></center></td>
    <td><center><h2>{{ states('sensor.ham_radio_propagation_solar_sunspots') }}&nbsp;&nbsp;&nbsp;&nbsp;</h2></center></td>  
    </tr>   
    </table>
```

## Custom Background
 To change the background color of the cards take notice that card-mod integration through HACS needs to be installed.
 And add custom CSS with this code at beginning of the snippet.

```yaml
- type: markdown
    card_mod:
        style: |
        ha-card {
            --ha-card-background: #434954;
        }
    title: Solar data
```