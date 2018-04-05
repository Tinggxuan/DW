class Water_Sensor:

    def __init__(self, pin_num):
        self.pin = pin_num
        self.status = self.get_status(pin_num)

    def get_status(self, pin_num):
        # Implement function to get water lvl; expect True/False
        