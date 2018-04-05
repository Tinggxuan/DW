class Tank:
    
    def __init__(self, kwargs):
        # digital pin for water lvl sensor
        self._water_lvl = self.water_lvl()
        # call valve to add the valve
        self._valve = self.valve()
        # call pump to add the pump
        self._pump = self.pump()

    def water_lvl(self, pin_num): # receive digital pin and get the water lvl
        tank_water_sensor = Water_Sensor(pin_num)
        return tank_water_sensor

    def valve(self, pin_num): # create valve obj and add it to Tank obj
        tank_valve = Value(pin_num)
        return tank_valve

    def pump(self, pin_num): # create pump obj and add it to Tank obj
        tank_pump = Pump(pin_num)
        return tank_pump

