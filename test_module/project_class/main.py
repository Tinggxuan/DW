import time
import ADS1x15
import RPi.GPIO as GPIO
import Tank


# create adc object to read the analog reading
adc1 = ADS1x15.ADS1115(address=0x48)
adc2 = ADS1x15.ADS1115(address=0x49)

# initialize rain_water_tank obj
rain_water_tank = Tank.Tank({'water_sensor':{'low':0, 'high':1},\
                             'valve':{'toilet_out':14},\
                             'pump':{'toilet_out':15}},\
                             adc1)

# initialize rain_buffer_tank obj
rain_buffer_tank = Tank.Tank({'water_sensor':{'low':2},\
                             'valve':{'waste_out':23},\
                             'pump':{'waste_out':24, 'rain_out':25}},\
                             adc1)
                        
# initialize clean_water_tank obj
clean_water_tank = Tank.Tank({'water_sensor':{'high':3},\
                             'valve':{'toilet_out':7},\
                             'pump':{'toilet_out':8}},\
                             adc1)

# initialize the reservoir_tank obj
reservoir_tank = Tank.Tank({'pump':{'clean_out':1, 'rain_out':12}},\
                            adc1)



try:
    while True:
        # condition: rain_water_tank not full and rain_buffer_tank has water
        if rain_buffer_tank.water_sensor['low'].get_status() == True:
            if rain_water_tank.water_sensor['high'].get_status() == False:
                rain_buffer_tank.pump['rain_out'].activate()
            else:
                rain_buffer_tank.valve['waste_out'].activate()
                rain_buffer_tank.pump['waste_out'].activate()
        
        # condition: rain_water_tank full and rain_buffer_tank has water
        else:
            rain_buffer_tank.valve['waste_out'].deactivate()
            rain_buffer_tank.pump['rain_out'].deactivate()
            rain_buffer_tank.pump['waste_out'].deactivate()

        # condition: clean_water_tank not full -> refill using reservoir tank
        if clean_water_tank.water_sensor['high'].get_status() == False:
            reservoir_tank.pump['clean_out'].activate()
        else:
            reservoir_tank.pump['clean_out'].deactivate()


except KeyboardInterrupt:
    GPIO.cleanup()



