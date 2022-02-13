# File Name: mqtt-subscribe.py
# Created By: Kayser-Sosa, with help from ThatGuyYouKnow.
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
import logging
from paho.mqtt import client as mqtt_client


# MQTT Broker ==================================================================================================================
broker = '##.##.##.##'   #<------------ IP Address of MQTT Server, in this case the Home Assistant Server
port = 1883 #<------------------- port used on MQTT Server, default port was used
username = 'username' #<--------------- username setup on the Home Assistant Server
password = 'password' #<------------- password setup for the user on the Home Assistant Server

# Subscribe to Multiple Topics ('topic',qos)
subscribetopic = [('etekcityzap/switch1/command',1),('etekcityzap/switch2/command',1),('etekcityzap/switch3/command',1),('etekcityzap/switch4/command',1),('etekcityzap/switch5/command',1),('etekcityzap/switch6/command',1)]
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^ these are the topics I used, enter whatever you want yours to be

# Generate Client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'


# MQTT Log File ================================================================================================================
FORMAT = '%(asctime)s - %(user) - %(message)s'
logging.basicConfig(filename='/home/pi/mqtt-rf/mqtt.log', level=logging.DEBUG, format=FORMAT)
#^^^^^^^^^^^^^^^^^^^^^ log file that will contain all the same stuff as the print() commands with a time/date stamp, you will ahve to manually empty the file when too big


# MQTT Connection ==============================================================================================================
def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
            logging.debug("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
            logging.debug("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


# MQTT Subscriptions & Commands ================================================================================================
def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        logging.debug(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        
        topic = msg.topic
        message = msg.payload.decode()
  
        # Full path to rf-send.py is required for the auto-startup via rc.local
               
        # EtekcityZap-Switch-1
        if topic == "etekcityzap/switch1/command":
           if message  == "ON":
              os.system("python3 /home/pi/mqtt-rf/rf-send.py -p 185 -t 1 code") #<---------------------- put in your code for the word code, pulse and time might be the same or similar
           elif message  == "OFF":
              os.system("python3 /home/pi/mqtt-rf/rf-send.py -p 185 -t 1 code") #<---------------------- put in your code for the word code, pulse and time might be the same or similar
              
        # EtekcityZap-Switch-2
        if topic == "etekcityzap/switch2/command":
           if message  == "ON":
              os.system("python3 /home/pi/mqtt-rf/rf-send.py -p 185 -t 1 code") #<---------------------- put in your code for the word code, pulse and time might be the same or similar
           elif message  == "OFF":
              os.system("python3 /home/pi/mqtt-rf/rf-send.py -p 185 -t 1 code") #<---------------------- put in your code for the word code, pulse and time might be the same or similar
              
        # EtekcityZap-Switch-3
        if topic == "etekcityzap/switch3/command":
           if message  == "ON":
              os.system("python3 /home/pi/mqtt-rf/rf-send.py -p 185 -t 1 code") #<---------------------- put in your code for the word code, pulse and time might be the same or similar
           elif message  == "OFF":
              os.system("python3 /home/pi/mqtt-rf/rf-send.py -p 185 -t 1 code") #<---------------------- put in your code for the word code, pulse and time might be the same or similar
              
        # EtekcityZap-Switch-4
        if topic == "etekcityzap/switch4/command":
           if message  == "ON":
              os.system("python3 /home/pi/mqtt-rf/rf-send.py -p 185 -t 1 code") #<---------------------- put in your code for the word code, pulse and time might be the same or similar
           elif message  == "OFF":
              os.system("python3 /home/pi/mqtt-rf/rf-send.py -p 185 -t 1 code") #<---------------------- put in your code for the word code, pulse and time might be the same or similar

        # EtekcityZap-Switch-5
        if topic == "etekcityzap/switch5/command":
           if message  == "ON":
              os.system("python3 /home/pi/mqtt-rf/rf-send.py -p 168 -t 1 code") #<---------------------- put in your code for the word code, pulse and time might be the same or similar
           elif message  == "OFF":
              os.system("python3 /home/pi/mqtt-rf/rf-send.py -p 168 -t 1 code") #<---------------------- put in your code for the word code, pulse and time might be the same or similar
              
        # EtekcityZap-Switch-6
        if topic == "etekcityzap/switch6/command":
           if message  == "ON":
              os.system("python3 /home/pi/mqtt-rf/rf-send.py -p 168 -t 1 code") #<---------------------- put in your code for the word code, pulse and time might be the same or similar
           elif message  == "OFF":
              os.system("python3 /home/pi/mqtt-rf/rf-send.py -p 168 -t 1 code") #<---------------------- put in your code for the word code, pulse and time might be the same or similar
        
    client.subscribe(subscribetopic)
    client.on_message = on_message


# Main Never Ending Loop =======================================================================================================
def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()

if __name__ == '__main__':
    run()