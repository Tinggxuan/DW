from pythymiodw import *
from time import sleep
from firebase import firebase

url = 'https://dw-1d-2018.firebaseio.com' # URL to Firebase database
token = '55mNZni7ImzOoQfwiRuqRYKOTTHZsFJfhsftzSNw' # unique token used for authentication

# Create a firebase object by specifying the URL of the database and its secret token.
# The firebase object has functions put and get, that allows user to put data onto 
# the database and also retrieve data from the database.
firebase = firebase.FirebaseApplication(url, token)

robot = ThymioReal() # create an eBot object

no_movements = True

while no_movements:
    # Check the value of movement_list in the database at an interval of 0.5
    # seconds. Continue checking as long as the movement_list is not in the
    # database (ie. it is None). If movement_list is a valid list, the program
    # exits the while loop and controls the eBot to perform the movements
    # specified in the movement_list in sequential order. Each movement in the
    # list lasts exactly 1 second.

    # Write your code here
    if firebase.get('/movement_list') != None:
        if len(firebase.get('/movement_list')) > 0:
            no_movements = False
    robot.sleep(0.5)

# Write the code to control the eBot here

# 'up' movement => robot.wheels(100, 100)
# 'left' movement => robot.wheels(-100, 100)
# 'right' movement => robot.wheels(100, -100)

movement_list = firebase.get('/movement_list')

for move in movement_list:
    if move == "up":
        robot.wheels(100, 100)
        robot.sleep(1)
    elif move == "left":
        robot.wheels(-100, 100)
        robot.sleep(1)
    elif move == "right":
        robot.wheels(100, -100)
        robot.sleep(1)
    
    robot.wheels(0, 0)

firebase.put('/', 'movement_list', None)

