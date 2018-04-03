from kivy.app import App 
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.label import Label 
from kivy.uix.togglebutton import ToggleButton
from firebase import firebase

f=open("./../../WEEK4/internetofthings_thymio/secret.txt", "r")
token=f.readline().strip()
url="https://dw-1d-2018.firebaseio.com"

firebase=firebase.FirebaseApplication(url,token)

class GuiKivy(App):

	def build(self):
		layout=None
		# add your widget to the layout

		return layout

	def update_status(self, instance):
		# use this callback to update firebase
		pass


GuiKivy().run()
