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
	green = "OFF"
	red = "OFF"
	def build(self):
		layout=GridLayout(cols=2,row_force_default=True,row_default_height=100)
		# add your widget to the layout
		if firebase.get('/green') != None:
			self.green = firebase.get('/green')

		if firebase.get('/red') != None:
			self.red = firebase.get('/red')

		lbl_green = Label(text="GreenLED",font_size=50,halign='center',valign='middle')
		self.tgl_btn_green = ToggleButton(id="green",text=self.green,state="normal" if self.green=="OFF" else "down",\
										  font_size=50,on_press=self.update_status)
		layout.add_widget(lbl_green)
		layout.add_widget(self.tgl_btn_green)

		lbl_red = Label(text="RedLED",font_size=50,halign='center',valign='middle')
		self.tgl_btn_red = ToggleButton(id="red",text=self.red,state="normal" if self.red=="OFF" else "down",\
										font_size=50,on_press=self.update_status)
		layout.add_widget(lbl_red)
		layout.add_widget(self.tgl_btn_red)
		
		return layout

	def update_status(self, instance):
		# use this callback to update firebase
		if instance.id == "green":
			if instance.state=="normal":
				firebase.put('/', 'green', "ON")
				instance.state = "down"
				instance.text = "ON"
			else:
				firebase.put('/', 'green', "OFF")
				instance.state = "normal"
				instance.text = "OFF"
		else:
			if instance.state=="normal":
				firebase.put('/', 'red', "ON")
				instance.state = "down"
				instance.text = "ON"
			else:
				firebase.put('/', 'red', "OFF")
				instance.state = "normal"
				instance.text = "OFF"

GuiKivy().run()