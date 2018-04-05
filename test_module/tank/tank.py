class Tank:
    
    def __init__(self, kwargs):
        # digital pin for water lvl sensor
        self._water_lvl = self.water_lvl()
        # call valve to add the valve
        self._valve = self.valve()
        # call pump to add the pump
        self._pump = self.pump()

    def water_lvl(self): # receive digital pin and get the water lvl
        pass
        

    def valve(self): # create valve obj and add it to Tank obj
        pass
        

    def pump(self): # create pump obj and add it to Tank obj
        pass
        
