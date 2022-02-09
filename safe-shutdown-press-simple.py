# File Name: safe-shutdown-press-simple.py
# Created By: Tony L Hansen and modified by Kayser-Sosa
# Use: Add a Safe Off Switch to Power Down Your Raspberry Pi
# Requirements: Python 3.6 or higher

# Code modified from - Add a Safe Off Switch to Power Down Your Raspberry Pi
# https://github.com/TonyLHansen/raspberry-pi-safe-off-switch/

# Resources
# https://github.com/TonyLHansen/raspberry-pi-safe-off-switch/

# Imports ======================================================================================================================
from gpiozero import Button
import os

# Shutdown =====================================================================================================================

# Press GPIO 26 to shutdown 
Button(26).wait_for_press()
os.system("sudo poweroff")