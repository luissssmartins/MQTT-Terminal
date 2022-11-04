import paho.mqtt.client as mqtt

import json
import uuid

mqtt_config = open('config.json')

conf = json.load(mqtt_config)

mqtt_config.close()

mqtt_server = conf["address"]
mqtt_port = conf["port"]
mqtt_user = conf["username"]
mqtt_password = conf["password"]

def on_connect(client, userdata, flags, rc):

    print(f"Connected with result code {rc}")

    client.subscribe("#")

def on_message(client, userdata, msg):
    print(f"Message received [{msg.topic}]: {msg.payload}")


client = mqtt.Client("client-" + uuid.uuid4())

client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set(mqtt_user, mqtt_password)

client.connect(mqtt_server, mqtt_port)

client.loop_forever()
