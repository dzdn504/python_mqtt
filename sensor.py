import time
import mqtt_client

class Sensor:
    def __init__(self):
        self.counter = 0
        self.mqtt = mqtt_client.MqttClient()
        time.sleep(1)

    def increment_counter(self):
        self.counter += 1
        print("Counter: {} ".format(self.counter))
        self.mqtt.publish("Counter: {} ".format(self.counter))
        time.sleep(1)
        return 

if __name__ == "__main__":
    sensor = Sensor()
    while sensor.counter < 20:
        sensor.increment_counter()