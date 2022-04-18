# Python API Examples for Datacake
- How to send sensor data from any Python script to Datacake using Webhook Integration.
- How to send and receive sensor data using Paho MQTT Library and Third-Party MQTT Integration on Datacake.

## python_api_example.py

Basic example on how to send sensor data to Datacake using a POST HTTP Webhook call. The URL we are performing a POST call on is the URL of an API Product (and Device) on Datacake. 

### python_api_example_decoder.js

This is the corresponding decoder for the above python example.

### Run locally

You can test the above Python example on your local desktop, machine, Raspberry Pi, whatever device that has Python support and Requests library installed. Simply run the example like the following:

```
pip3 install requests
python3 python_api_example.py
```

## python_api_example_mqtt.py

Bidirectional MQTT communication example.

### Public Datacake MQTT Server

For this example we are using a public Datacake MQTT Broker. The connection details are as follows:

- Host: `public-mqtt-93bb.managed-mqtt.com`
- Port: `1883` or `8883` (for TLS with CA-Signed Certificate)
- Username: `datacake`
- Password: `datacake`

### Run locally

```
pip3 install paho
python3 python_api_example_mqtt.py
```