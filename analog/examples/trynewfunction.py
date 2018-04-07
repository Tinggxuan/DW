import time
import ADS1x15

adc1 = ADS1x15.ADS1115(address=0x48)
adc2 = ADS1x15.ADS1115(address=0x49)

GAIN = 1

def readvalues(adc):
    values = [0]*4
    for i in range(4):
        values[i]= adc.read_adc(i, gain = GAIN)
        if values[i] > 29000:
            values[i] = 1
        else:
            values[i] = 0
        print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*values))
        time.sleep(0.5)
        
print('Reading ADS1x15 values,press Ctrl-C to quit')
print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*range(4)))
print('-' * 37)
while True:
    readvalues(adc1)
    readvalues(adc2)
