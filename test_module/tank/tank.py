class Tank:
    
    def __init__(self, kwargs):
        # digital pin for water lvl sensor
        self.water_sensor = self.water_sensor(kwargs['water_sensor'])
        # call valve to add the valve
        self.valve = self.valve(kwargs['valve'])
        # call pump to add the pump
        self.pump = self.pump(kwargs['pump'])

    def water_sensor(self, pin_num): # create water sensor obj and add it to Tank obj
        tank_water_sensor = Water_Sensor(pin_num)
        return tank_water_sensor

    def valve(self, pin_num): # create valve obj and add it to Tank obj
        tank_valve = Value(pin_num)
        return tank_valve

    def pump(self, pin_num): # create pump obj and add it to Tank obj
        tank_pump = Pump(pin_num)
        return tank_pump

