class Tank:
    
    def __init__(self, kwargs):
        # digital pin for water lvl sensor
        self.water_sensor = self.water_sensor(kwargs['water_sensor'])
        # call valve to add the valve
        self.valve = self.valve(kwargs['valve'])
        # call pump to add the pump
        self.pump = self.pump(kwargs['pump'])

    def water_sensor(self, pin_num): # create water sensor obj and add it to Tank obj
        tank_water_sensor = {}
        for key, value in pin_num.items():
            tank_water_sensor[key] = Water_Sensor(value)
        return tank_water_sensor

    def valve(self, pin_num): # create valve obj and add it to Tank obj
        tank_valve = {}
        for key, value in pin_num.items():
            tank_valve[key] = Valve(value)
        return tank_valve

    def pump(self, pin_num): # create pump obj and add it to Tank obj
        tank_pump = {}
        for key, value in pin_num.items():
            tank_pump[key] = Pump(value)
        return tank_pump

