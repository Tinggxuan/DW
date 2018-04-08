import Tank

class Toilet_Tank(Tank.Tank): # inherit from class 'Tank'

    def __init__(self, kwargs, adc):
        super().__init__(kwargs,adc) # call the parent class __init__
        self.flush = self.flush(adc, kwargs['flush']) # new attributte


    def flush(self, adc, channel):
        # call the parent class water_sensor to initialise the water_sensor obj
        # use the water sensor as button
        toilet_flush = super().water_sensor(adc, channel) 
        return toilet_flush