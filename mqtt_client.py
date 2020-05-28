
import paho.mqtt.client as paho
import json
import logging
import time
import requests 
from threading import Timer
import os

# MQTT related constants
MQTT_BROKER_HOST = "localhost"
MQTT_BROKER_PORT = 1883
MQTT_KEEPALIVE = 5
MQTT_OUTBOUND_TOPIC_NAME = "sensor_data"
DEVICE_NAME = "sensor"
EVENT_NAME = "counter-event"
MQTT_BROKER_ADDRESS = MQTT_BROKER_HOST + ":" + str(MQTT_BROKER_PORT)

class MqttClient:
    def __init__(self):
        self.mqttClient = paho.Client()
        self.mqttClient.on_connect = self.on_connect

        self.mqttClient.connect(MQTT_BROKER_HOST, MQTT_BROKER_PORT, MQTT_KEEPALIVE)
        self.mqttClient.loop_start()

    def on_connect(self, client, userdata, message, rc):
        print("Connected to mqtt broker")
        return
    
    def publish(self, data):
        mqttWrapper = {}
        mqttWrapper["name"] = DEVICE_NAME
        mqttWrapper["event"] = EVENT_NAME
        mqttWrapper["data"] = data
        self.mqttClient.publish(MQTT_OUTBOUND_TOPIC_NAME, json.dumps(mqttWrapper))
        return