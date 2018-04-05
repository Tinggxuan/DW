import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

class Pump:

    def __init__(self, pin_num):
        self.pin_num = pin_num
        GPIO.setup(pin_num, GPIO.OUT)

    def activate(self, duration):
        GPIO.output(self.pin_num, GPIO.HIGH)
        sleep(duration)
        GPIO.output(self.pin_num, GPIO.LOW)