# Add the next Spot the Station event to Home Assistant sensor
This integration allows you to fetch upcoming International Space Station (ISS) sighting information from Spot the Station and display it as a sensor in Home Assistant.

# Notes
- The script requires feedparser in order to work. this can be installed in HA by running '``pip3 install feedparser``' in the command line.
- Remember to update the feed_url in the spot_the_next_station.py file. You can get an RSS feed for your area at https://spotthestation.nasa.gov/

# Installation
1. Copy the spot_the_station.yaml file to the packages directory in your Home Assistant configuration.
2. Copy the spot_the_next_station.py file to the python_scripts directory in your Home Assistant configuration.
3. Add the following configuration to your configuration.yaml file:
```
homeassistant:
    packages: !include_dir_named packages
    
python_script:
```

# Usage
The Spot the Station integration consists of a sensor that retrieves the upcoming ISS sighting information. The sensor updates automatically once a day ```scan_interval: 1440```.

You can manually trigger an update of the sensor by calling the homeassistant.update_entity service:
```
service: homeassistant.update_entity
data: {}
target:
  entity_id: sensor.spot_the_station
```

# Sensor Attributes
The sensor provides the following attributes:

Date: The date of the upcoming ISS sighting.
Time: The time of the upcoming ISS sighting.
Duration: The duration of the ISS sighting.
Maximum Elevation: The maximum elevation of the ISS during the sighting.
Approach: The approach direction of the ISS.
Departure: The departure direction of the ISS.
Event Start: The start time of the ISS sighting.
Event End: The end time of the ISS sighting.

# Customization
You can customize the sensor's name and icon in the customize section of your spot_the_station.yaml file.
