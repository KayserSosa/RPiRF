#!/bin/sh
# launcher.sh
# Navigate to home dir, then to program dir, then execute, then back home

cd /
cd /home/pi/mqtt-rf
sudo python3 mqtt-subscribe.py
cd /
