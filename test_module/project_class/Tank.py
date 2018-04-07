import Water_Sensor
import Valve
import Pump

class Tank:
    
    def __init__(self, kwargs, adc):
        # digital pin for water lvl sensor
        self.water_sensor = self.water_sensor(adc, kwargs['water_sensor'])
        # call valve to add the valve
        self.valve = self.valve(kwargs['valve'])
        # call pump to add the pump
        self.pump = self.pump(kwargs['pump'])

    def water_sensor(self, adc, channel): # create water sensor obj and add it to Tank obj
        tank_water_sensor = {} # create empty dicitonary to store the child  class obj
        for key, value in channel.items():
            tank_water_sensor[key] = Water_Sensor.Water_Sensor(adc, value)
        return tank_water_sensor # return dict for ease of child reference

    def valve(self, pin_num): # create valve obj and add it to Tank obj
        tank_valve = {} # create empty dicitonary to store the child class obj
        for key, value in pin_num.items():
            tank_valve[key] = Valve.Valve(value)
        return tank_valve # return dict for ease of child reference

    def pump(self, pin_num): # create pump obj and add it to Tank obj
        tank_pump = {} # create empty dicitonary to store the child class obj
        for key, value in pin_num.items():
            tank_pump[key] = Pump.Pump(value)
        return tank_pump # return dict for ease of child reference

