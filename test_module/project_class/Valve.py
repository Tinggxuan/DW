import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

class Valve:

    def __init__(self, pin_num):
        self.pin_num = pin_num
        GPIO.setup(pin_num, GPIO.OUT)

    def activate(self):
        GPIO.output(self.pin_num, GPIO.HIGH)

    def deactivate(self):
        GPIO.output(self.pin_num, GPIO.LOW)
