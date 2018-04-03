from RPi import GPIO
from firebase import firebase

f=open("./../../WEEK4/internetofthings_thymio/secret.txt", "r")
token=f.readline().strip()
url="https://dw-1d-2018.firebaseio.com"

firebase=firebase.FirebaseApplication(url,token)

GPIO.setmode(GPIO.BCM)
ledcolor={'green':23, 'red':24}

GPIO.setup(list(ledcolor.values()), GPIO.OUT)

def set_led(ledno, status):
	# you can use this to set the LED on or off
	if status == "ON":
		GPIO.output(ledno, GPIO.HIGH)
	elif status == "OFF":
		GPIO.output(ledno, GPIO.LOW)


while True:
	# get firebase data and call setLED
	green = firebase.get('/green')
	red = firebase.get('/red')
	if green != None:
		set_led(23, green)
	else:
		set_led(23, "OFF")

	if red != None:
		set_led(24, red)
	else:
		set_led(24, "OFF")
