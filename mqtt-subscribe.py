# File Name: mqtt-subscribe.py
# Use: Subscribes to multiple MQTT topics to control Etekcity ZAP 433 MHz switches
# Requirements: Python 3.6 or higher

# Code modified from - How to use MQTT in Python (Paho)
# https://www.emqx.io/blog/how-to-use-mqtt-in-python

# Resources
# https://www.emqx.io/blog/how-to-use-mqtt-in-python
# https://stackoverflow.com/questions/41624697/mqtt-python-subscribe-to-multiple-topics-and-write-payloads-on-raspberry-lcd


# Imports ======================================================================================================================
import random
import os
from paho.mqtt import client as mqtt_client


# MQTT Broker ==================================================================================================================
broker = 'ip address'
port = port number
username = 'username'
password = 'password'

# Subscribe to Multiple Topics ('topic',qos)
subscribetopic = [('etekcityzap/switch1/command',1),('etekcityzap/switch2/command',1),('etekcityzap/switch3/command',1),('etekcityzap/switch4/command',1),('etekcityzap/switch5/command',1)]

# Generate Client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'


# MQTT Connection ==============================================================================================================
def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


# MQTT Subscriptions & Commands ================================================================================================
def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        
        topic = msg.topic
        message = msg.payload.decode()
  
        # EtekcityZap-Switch-1
        if topic == "etekcityzap/switch1/command":
           if message  == "ON":
              os.system("python3 rf-send.py -p 185 -t 1 5592371")
           elif message  == "OFF":
              os.system("python3 rf-send.py -p 185 -t 1 5592380")
              
        # EtekcityZap-Switch-2
        if topic == "etekcityzap/switch2/command":
           if message  == "ON":
              os.system("python3 rf-send.py -p 185 -t 1 5592515")
           elif message  == "OFF":
              os.system("python3 rf-send.py -p 185 -t 1 5592524")
              
        # EtekcityZap-Switch-3
        if topic == "etekcityzap/switch3/command":
           if message  == "ON":
              os.system("python3 rf-send.py -p 185 -t 1 5592835")
           elif message  == "OFF":
              os.system("python3 rf-send.py -p 185 -t 1 5592844")
              
        # EtekcityZap-Switch-4
        if topic == "etekcityzap/switch4/command":
           if message  == "ON":
              os.system("python3 rf-send.py -p 185 -t 1 5594371")
           elif message  == "OFF":
              os.system("python3 rf-send.py -p 185 -t 1 5594380")

        # EtekcityZap-Switch-5
        if topic == "etekcityzap/switch5/command":
           if message  == "ON":
              os.system("python3 rf-send.py -p 168 -t 1 87811")
           elif message  == "OFF":
              os.system("python3 rf-send.py -p 168 -t 1 87820")
        
    client.subscribe(subscribetopic)
    client.on_message = on_message


# Main Never Ending Loop =======================================================================================================
def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()

if __name__ == '__main__':
    run()
