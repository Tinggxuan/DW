import time
import ADS1x15
import RPi.GPIO as GPIO
import Tank


# create adc object to read the analog reading
adc1 = ADS1x15.ADS1115(address=0x48)
adc2 = ADS1x15.ADS1115(address=0x49)


rain_water_tank = Tank.Tank({'water_sensor':{'low':0},\
                             'valve':{'in':20,'out':21},\
                             'pump':{'in':19,'out':26}},adc1)

try:
    while True:
        if rain_water_tank.water_sensor['low'].get_status() == True:
            rain_water_tank.valve['in'].activate()
            rain_water_tank.valve['out'].activate()
            rain_water_tank.pump['in'].activate()
            rain_water_tank.pump['out'].activate()
            time.sleep(5)
            rain_water_tank.valve['in'].deactivate()
            rain_water_tank.valve['out'].deactivate()
            rain_water_tank.pump['in'].deactivate()
            rain_water_tank.pump['out'].deactivate()

except KeyboardInterrupt:
    GPIO.cleanup()



