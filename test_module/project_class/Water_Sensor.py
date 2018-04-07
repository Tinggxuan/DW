class Water_Sensor:

    def __init__(self, adc_obj, channel):
        self.adc_obj = adc_obj
        self.channel = channel
        self.status = self.get_status()

    def get_status(self):
        reading = self.adc_obj.read_adc(self.channel, 1) #1 refer to the GAIN of the sensor to read voltage from 0 to 4.09V
        result = True if reading > 29000 else False
        return result
        

