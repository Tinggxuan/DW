#!/usr/bin/python
# -*- coding: utf-8 -*-

from pythymiodw import *

def print_temp(t_celcius):
    t_F = t_celcius * 9/5 + 32
    print("The temperature in Celsius is {:.3f} and Fahrenheit is {:.3f}".format(float(t_celcius), float(t_F))

def forward(speed, duration):
    robot.wheels(speed, speed)
    robot.sleep(duration) 
    robot.wheels(0, 0)

robot = ThymioReal() # create an object

############### Start writing your code here ################ 

# Prompt user to enter speed and duration of movement
speed = int(input("Please enter the speed: "))
print(str(speed))
duration = int(input("Please enter the duration: "))
print(str(duration))

# Move according to the specified speed and duration
forward(speed, duration)

# Read temperature in celcius from the sensor and print it
print_temp(robot.get_temperature())

########################## end ############################## 

robot.quit() # disconnect the communication

