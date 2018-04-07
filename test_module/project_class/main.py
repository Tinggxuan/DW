import time
import ADS1x15
import RPi.GPIO as GPIO


# create adc object to read the analog reading
adc1 = ADS1x15.ADS1115(address=0x48)
adc2 = ADS1x15.ADS1115(address=0x49)


try:
    while True:
        pass

except KeyboardInterrupt:
    GPIO.cleanup()



