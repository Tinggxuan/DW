from RPi import GPIO
from firebase import firebase

f=open("./../../WEEK4/internetofthings_thymio/secret.txt", "r")
token=f.readline().strip()
url="https://dw-1d-2018.firebaseio.com"

firebase=firebase.FirebaseApplication(url,token)

GPIO.setmode(GPIO.BCM)
ledcolor={'yellow':23, 'red':24}

GPIO.setup(ledcolor.values(), GPIO.OUT)

def set_led(ledno, status):
	# you can use this to set the LED on or off
	pass

while True:
	# get firebase data and call setLED
    pass
