import RPi.GPIO as GPIO
from time import sleep

# Use the BCM GPIO numbers as the numbering scheme.
GPIO.setmode(GPIO.BCM)

#GPIO.setup(24, GPIO.OUT)
GPIO.setup(23, GPIO.IN)

done = False
#GPIO.output(24,GPIO.HIGH)
while not done:
    print(GPIO.input(23))
    #GPIO.output(24.GPIO.HIGH)
