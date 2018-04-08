import time
import ADS1x15
import RPi.GPIO as GPIO
import Tank
import Toilet_Tank

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
                             'pump':{'toilet_out':15}},\
                             adc1)

# initialize the reservoir_tank obj
reservoir_tank = Tank.Tank({'pump':{'clean_out':1, 'rain_out':12}},\
                            adc1)

# initialize the toilet_tank_1 obj -> level 1 toilet tank
toilet_tank1 = Toilet_Tank.Toilet_Tank({'water_sensor':{'high':0},\
                                        'flush':{'flush':1}
                                        'valve':{'in':16, 'out':20},\
                                        'pump':{'flush':21}},\
                                        adc2)

# initialize the toilet_tank_2 obj -> level 2 toilet tank
toilet_tank2 = Toilet_Tank.Toilet_Tank({'water_sensor':{'high':2},\
                                        'flush':{'flush':3}
                                        'valve':{'in':4, 'out':17},\
                                        'pump':{'flush':21}},\
                                        adc2)



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

        # condition: flush is triggered for toilet_tank1
        if toilet_tank1.flush['flush'].get_status() == True:
            # flush the water out from toilet_tank1
            toilet_tank1.pump['flush'].activate()
            toilet_tank1.valve['out'].activate()
            time.sleep(3)
            toilet_tank1.pump['flush'].deactivate()
            toilet_tank1.valve['out'].deactivate()

            # refill the toilet_tank1
            # use rain_water_tank if available else use clean_water_tank
            if rain_water_tank.water_sensor['low'] == True:
                rain_water_tank.pump['toilet_out'].activate()
                toilet_tank1.valve['in'].activate()
                while not toilet_tank1.water_sensor['high'].get_status():
                    pass
                else:
                    rain_water_tank.pump['toilet_out'].deactivate()
                    toilet_tank1.valve['in'].deactivate()
            else:
                clean_water_tank.pump['toilet_out'].activate()
                toilet_tank1.valve['in'].activate()
                while not toilet_tank1.water_sensor['high'].get_status():
                    pass
                else:
                    clean_water_tank.pump['toilet_out'].deactivate()
                    toilet_tank1.valve['in'].deactivate()

        # condition: flush is triggered for toilet_tank2
        if toilet_tank2.flush['flush'].get_status() == True:
            # flush the water out from toilet_tank1
            toilet_tank2.pump['flush'].activate()
            toilet_tank2.valve['out'].activate()
            time.sleep(3)
            toilet_tank2.pump['flush'].deactivate()
            toilet_tank2.valve['out'].deactivate()

            # refill the toilet_tank1
            # use rain_water_tank if available else use clean_water_tank
            if rain_water_tank.water_sensor['low'] == True:
                rain_water_tank.pump['toilet_out'].activate()
                toilet_tank2.valve['in'].activate()
                while not toilet_tank2.water_sensor['high'].get_status():
                    pass
                else:
                    rain_water_tank.pump['toilet_out'].deactivate()
                    toilet_tank2.valve['in'].deactivate()
            else:
                clean_water_tank.pump['toilet_out'].activate()
                toilet_tank2.valve['in'].activate()
                while not toilet_tank2.water_sensor['high'].get_status():
                    pass
                else:
                    clean_water_tank.pump['toilet_out'].deactivate()
                    toilet_tank2.valve['in'].deactivate()
            

except KeyboardInterrupt:
    GPIO.cleanup()



