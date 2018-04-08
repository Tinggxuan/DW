import time
import ADS1x15
import RPi.GPIO as GPIO
import Tank


# create adc object to read the analog reading
adc1 = ADS1x15.ADS1115(address=0x48)
adc2 = ADS1x15.ADS1115(address=0x49)

# initialize the rain_water_tank obj
rain_water_tank = Tank.Tank({'water_sensor':{'low':0, 'high':1},\
                             'valve':{'out':14},\
                             'pump':{'out':15}},\
                             adc1)

# initialize the rain_buffer_tank obj
rain_buffer_tank = Tank.Tank({'water_sensor':{'low':2},\
                             'valve':{'out':23},\
                             'pump':{'waster_out':24, 'rain_out':25}},\
                             adc1)


try:
    while True:
        # condition: rain_water_tank not full and rain_buffer_tank has water
        if rain_buffer_tank.water_sensor['low'] == True:
            if rain_water_tank.water_sensor['high'].get_status() == False:
                rain_buffer_tank.pump['rain_out'].activate()
            else:
                rain_buffer_tank.pump['waste_out'].activate()
        
        # condition: rain_water_tank full and rain_buffer_tank has water
        else:
            rain_buffer_tank.pump['rain_out'].deactivate()
            rain_buffer_tank.pump['waste_out'].deactivate()

except KeyboardInterrupt:
    GPIO.cleanup()



