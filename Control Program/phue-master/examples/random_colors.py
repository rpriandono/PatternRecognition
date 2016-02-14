#!/usr/bin/python
from phue import Bridge
import random

b = Bridge('10.10.0.115') # Enter bridge IP here.

#If running for the first time, press button on bridge and run with b.connect() uncommented
#b.connect()

"""
lights = b.get_light_objects()

for light in lights:
	light.brightness = 254
	light.xy = [random.random(),random.random()]
"""
lamp1, lamp2, lamp3 = b.get_light_objects()

"""
lamp1.brightness = 254
lamp2.brightness = 254
lamp3.brightness = 254
"""

normal = [1,1]
red = [0.75,0.25]
purple = [0.45,0.25]
skyblue = [0.15,0.25]
blue = [0.15,0.05]
yellow = [0.45,0.51]
green = [0.09,0.81]
lightgreen = [0.3,0.5]
orange = [0.55,0.4]

lamp1.xy = [1,1]
lamp2.xy = [0.15,0.25]
lamp3.xy = blue

lamp3.on = True