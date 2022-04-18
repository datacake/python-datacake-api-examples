"""
Easy Data Ingestion Demo using Datacake API Devices and Webhook Integration
(c) 2022 Simon Kemper @Datacake
"""
import requests

# The Webhook URL for your API Product on Datacake
url = "https://api.datacake.co/integrations/api/85dd4a6f-f587-4e5d-a522-c871caaba059/"

# Serial for device identification on Datacake
serial = "pythondevice001"

# Some random sensor data (replace with real data)
temperature = 16.04
humidity = 53.23
pressure = 1015
light = 734
power_status = True
lat = 51.4356
lon = 6.953

# Create a dictionary containing payload for webhook call
payload = {
    "s": serial,
    "t": temperature,
    "h": humidity,
    "p": pressure,
    "l": light,
    "ps": power_status,
    "loc": "(" + str(lat) + "," + str(lon) + ")"
}

# Do a post request on the webhook including payload data
r = requests.post(url, json=payload)

print(r)