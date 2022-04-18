import random
import time

from paho.mqtt import client as mqtt_client

serial = "pythondevice001"
broker = 'public-mqtt-93bb.managed-mqtt.com'
port = 8883
topic = f"python/{serial}/mqtt"
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = 'datacake'
password = 'datacake'

def on_connect(client, userdata, flags, rc):
    client.subscribe(topic)
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d\n", rc)

def on_message(client, userdata, message):
    print("received message =",str(message.payload.decode("utf-8")))

client = mqtt_client.Client(client_id)
client.username_pw_set(username, password)
client.on_connect = on_connect
client.on_message = on_message
client.tls_set()    
client.loop_start()    
client.connect(broker, port)

msg_count = 0

while True:
    time.sleep(10)
    msg = f"messages: {msg_count}"
    result = client.publish(topic, msg)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        print(f"Send `{msg}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")
    msg_count += 1