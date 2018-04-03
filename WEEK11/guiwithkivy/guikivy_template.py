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

	if firebase.get('/green') != None:
		green = firebase.get('/green')
	else:
		green = "OFF"
		firebase.put('/', 'green', "OFF")

	if firebase.get('/red') != None:
		red = firebase.get('/red')
	else:
		red = "OFF"
		firebase.put('/', 'red', "OFF")

	def build(self):
		Window.size=(200,200)
		layout=GridLayout(cols=2,row_force_default=True,row_default_height=100)
		# add your widget to the layout

		lbl_green = Label(text="GreenLED",font_size=50,halign='center',valign='middle')
		self.tgl_btn_green = ToggleButton(id="green",text=self.green,font_size=50,state="normal" if self.green=="OFF" else "down")
		self.tgl_btn_green.bind(state=self.update_status)

		layout.add_widget(lbl_green)
		layout.add_widget(self.tgl_btn_green)

		lbl_red = Label(text="RedLED",font_size=50,halign='center',valign='middle')
		self.tgl_btn_red = ToggleButton(id="red",text=self.red,font_size=50,state="normal" if self.red=="OFF" else "down")
		self.tgl_btn_red.bind(state=self.update_status)
		layout.add_widget(lbl_red)
		layout.add_widget(self.tgl_btn_red)
		
		return layout

	def update_status(self, instance, value):
		# use this callback to update firebase
		if instance.id == "green":
			if self.green=="ON":
				instance.state="normal"
				instance.text = "OFF"
				self.green = "OFF"
				firebase.put('/', 'green', "OFF")
			else:
				instance.state = "down"
				instance.text = "ON"
				self.green = "ON"
				firebase.put('/', 'green', "ON")
		else:
			if self.red=="ON":
				instance.state="normal"
				instance.text = "OFF"
				self.red = "OFF"
				firebase.put('/', 'red', "OFF")
			else:
				instance.state = "down"
				instance.text = "ON"
				self.red = "ON"
				firebase.put('/', 'red', "ON")

GuiKivy().run()