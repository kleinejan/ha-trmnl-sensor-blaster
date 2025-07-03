# TRMNL Entity Blaster Integration

A Home Assistant custom integration that pushes sensor data to TRMNL devices with grouped JSON payloads.

## Features

- **Custom Sensor Groups**: Organize sensors using Home Assistant labels (e.g., "temperatures", "garbage", "humidity")
- **Grouped JSON Output**: Creates structured payloads like `{"temperatures": [{"name": "toilet", "value": "25°C"}]}`
- **2KB Payload Management**: Automatically handles TRMNL's payload size limits
- **Minimal Data Format**: Sends only essential data (name + value + optional icon) for efficiency
- **Flexible Configuration**: Multi-select sensor groups with custom values

## Installation

### HACS (Recommended)
1. Add this repository to HACS as a custom repository
2. Install "TRMNL Entity Blaster" from HACS
3. Restart Home Assistant

### Manual Installation
1. Copy the `trmnl_entity_blaster` folder to `custom_components/`
2. Restart Home Assistant

## Configuration

1. **Create Labels**: Go to Settings → Labels and create groups like "temperatures", "garbage"
2. **Label Entities**: Assign labels to your sensors
3. **Add Integration**: Settings → Devices & Services → Add Integration → "TRMNL Entity Blaster"
4. **Configure**: Enter your TRMNL webhook URL and select sensor groups

## Example Output

```json
{
  "temperatures": [
    {"name": "Living Room", "value": "23.5°C", "icon": "mdi:home-thermometer"},
    {"name": "Bedroom", "value": "22°C", "icon": "mdi:bed"}
  ],
  "garbage": [
    {"name": "Garbage Day", "value": "2 days", "icon": "mdi:trash-can"}
  ]
}
```

## TRMNL
Create a private plugin on TRMNL, put the WEBHOOK from TRMNL into TRMNL-Sensor-Blaster.
If you 'Force Refresh' and 'Edit Markup' you can see them in 'your variables'.

Now you have all the data you need to build your own dashboard with data from Home assistant.

```yml
{% for product in TRMNL-temperatuur %}
          <div>
  <span class="value value--xxsmall">  {{ product.name }}</span>
  <span class="value value--xsmall">{{ product.value }}</span>
            </div>
{% endfor %}
```

## Requirements

- Home Assistant 2023.1.0+
- TRMNL webhook URL
- Sensors labeled with appropriate groups

## Thanks
This is my first integration that could not have been possible without the
super examples of [TRMNL-SENSOR-PUSH](https://github.com/gitstua/trmnl-sensor-push)

## License

MIT License