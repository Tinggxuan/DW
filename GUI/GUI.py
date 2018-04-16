# Change and save the configuration
from kivy.config import Config
Config.set('graphics', 'resizable', '0') # Disable window resize
Config.set('graphics', 'fullscreen', 'auto')


# Register all the font
from kivy.core.text import LabelBase
LabelBase.register(name="Archivo_Black",  
                   fn_regular="./fonts/Archivo_Black/ArchivoBlack-Regular.ttf")
LabelBase.register(name='EastSeaDokdo-Regular',fn_regular='./fonts/EastSeaDokdo-Regular/EastSeaDokdo-Regular.ttf')
LabelBase.register(name='Gugi-Regular',fn_regular='./fonts/Gugi-Regular/Gugi-Regular.ttf')

# Import UI module
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button 
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle, Ellipse, Line
from kivy.uix.popup import Popup
from kivy.utils import get_color_from_hex
from kivy.properties import ObjectProperty, NumericProperty
from kivy.uix.dropdown import DropDown

# Import firebase
from firebase import firebase


import threading

Builder.load_string('''
#:import get_color_from_hex kivy.utils.get_color_from_hex

# Login Screen and all its child widget
<LoginScreen>:
    id: loginscreen
    LoginBackgroundImage:
        allow_stretch: True
        keep_ratio: False
        opacity: 0.3
        source: 'login_background.jpeg'
        size: self.size
        pos: self.pos

        canvas:
            Color:
                rgba: get_color_from_hex('#404040')
            Rectangle:
                size: self.size
                pos: self.pos
    
    FloatLayout:
        size_hint: 0.5, 1
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}

        BoxLayout:
            size_hint: 1, 0.1
            pos_hint: {'x': 0, 'y': 0.8}
            Label:
                text: 'Water Management System'
                font_size: self.height*1
                font_name: 'Gugi-Regular'
                size_hint: 1, 1
                

        LoginMenu:
            pos_hint: {'x': 0, 'y': 0.6}
            LoginTextInput:
                id: username
                hint_text: 'Username'
                

        LoginMenu:
            pos_hint: {'x': 0, 'y': 0.45}        
            LoginTextInput:
                id: password
                hint_text: 'Password'
                allow_copy: False
                password: True


        LoginMenu:
            pos_hint: {'center_x': 0.5, 'y': 0.25}
            canvas.before:
                Clear
                Color:
                    rgba: 0, 0.902,0.6, self.canvas_opacity #0, 0.902,0.6
                Rectangle:
                    size: self.size
                    pos: self.pos
                Ellipse:
                    pos: self.pos[0] - self.size[1]/2.0, self.pos[1]
                    size: self.size[1],self.size[1]
                    angle_start: 180
                    angle_end: 360
                Ellipse:
                    pos: self.size[0] + self.pos[0] - self.size[1]/2.0, self.pos[1]
                    size: self.size[1],self.size[1]
                    angle_start:360
                    angle_end: 540
            LoginButton:
                username: username
                password: password
                loginscreen: loginscreen

        LoginMenu:
            pos_hint: {'center_x': 0.5, 'y': 0.1}
            size_hint: 0.12,0.1
            canvas.before:
                Clear
            canvas:
                Color:
                    rgb: 1,0,0
            QuitButton:
        
# Define the attribute of the BoxLayout
<LoginMenu>:
    size_hint: 1, 0.1
    canvas.before:
        Color: 
            rgba: get_color_from_hex('#f2f2f2')
        Rectangle:
            size: self.size
            pos: self.pos

# Define the attribute of the LoginTextInput
<LoginTextInput>:
    size_hint: 1, 1
    font_size: self.height*0.7
    padding_y: self.height*0.1
    font_name: 'Gugi-Regular'#Archivo_Black'
    multiline: False
    hint_text_color: get_color_from_hex('#d9d9d9')
    background_color: 0,0,0,0
    foreground_color: get_color_from_hex('#000000')
    cursor_color: get_color_from_hex('#000000')

    canvas.after:
        Color: 
            rgb: get_color_from_hex('#f2f2f2')
        Ellipse:
            angle_start: 180
            angle_end: 360
            size: self.size[1],self.size[1]
            pos: self.pos[0] - self.size[1]/2.0, self.pos[1]
        Ellipse:
            angle_start:360
            angle_end:540
            pos: (self.size[0] + self.pos[0] - self.size[1]/2.0, self.pos[1])
            size: (self.size[1], self.size[1])
        Color:
            rgba: get_color_from_hex('#ffffff')
        Line:
            points: self.pos[0] , self.pos[1], self.pos[0] + self.size[0], self.pos[1]
            width: 3
        Line:
            points: self.pos[0], self.pos[1] + self.size[1], self.pos[0] + self.size[0], self.pos[1] + self.size[1]
            width: 3
        Line:
            ellipse: self.pos[0] - self.size[1]/2.0, self.pos[1], self.size[1], self.size[1], 180, 360
            width: 3
        Line:
            ellipse: self.size[0] + self.pos[0] - self.size[1]/2.0, self.pos[1], self.size[1], self.size[1], 360, 540
            width: 3

# Define the attribute for the LoginButton
<LoginButton>:
    text: 'LOGIN'
    font_size: self.height*0.6
    padding_y: self.height*0.1
    font_name: 'Gugi-Regular'
    background_color: 0,0,0,0
    on_press: self.login(self.parent, self.parent.pos)
    on_release: self.parent.clear_canvas()

    canvas.after:
        Color:
            rgba: get_color_from_hex('#ffffff')
        Line:
            points: self.pos[0] , self.pos[1], self.pos[0] + self.size[0], self.pos[1]
            width: 3
        Line:
            points: self.pos[0], self.pos[1] + self.size[1], self.pos[0] + self.size[0], self.pos[1] + self.size[1]
            width: 3
        Line:
            ellipse: self.pos[0] - self.size[1]/2.0, self.pos[1], self.size[1], self.size[1], 180, 360
            width: 3
        Line:
            ellipse: self.size[0] + self.pos[0] - self.size[1]/2.0, self.pos[1], self.size[1], self.size[1], 360, 540
            width: 3

# Define the attribute for the QuitButton
# <QuitButton>:
#     background_color: 0,0,0,0
#     on_press: self.quit_app()
#     canvas.after:
#         Color:
#             rgb: get_color_from_hex('#ff0000')
#         Line:
#             cap: 'none'
#             points: self.pos[0]+self.size[0]*0.25, self.pos[1]+self.size[1]*0.25, self.pos[0]+self.size[0]*0.75, self.pos[1]+self.size[1]*0.75
#             width: 8
#         Line:
#             cap: 'none'
#             points: self.pos[0]+self.size[0]*0.25, self.pos[1]+self.size[1]*0.75, self.pos[0]+self.size[0]*0.75, self.pos[1]+self.size[1]*0.25
#             width: 8
#         Line:
#             ellipse: self.pos[0], self.pos[1], self.size[1], self.size[1], 180, 360
#             width: 8
#         Line:
#             ellipse: self.pos[0], self.pos[1], self.size[1], self.size[1], 360, 540
#             width: 8
<QuitButton>:
    text: 'QUIT'
    font_size: self.height*0.6
    padding_y: self.height*0.1
    font_name: 'Gugi-Regular'
    background_color: 0,0,0,0
    on_press: self.quit_app()

    canvas.after:
        Color:
            rgba: get_color_from_hex('#ffffff')
        Line:
            points: self.pos[0] , self.pos[1], self.pos[0] + self.size[0], self.pos[1]
            width: 3
        Line:
            points: self.pos[0], self.pos[1] + self.size[1], self.pos[0] + self.size[0], self.pos[1] + self.size[1]
            width: 3
        Line:
            ellipse: self.pos[0] - self.size[1]/2.0, self.pos[1], self.size[1], self.size[1], 180, 360
            width: 3
        Line:
            ellipse: self.size[0] + self.pos[0] - self.size[1]/2.0, self.pos[1], self.size[1], self.size[1], 360, 540
            width: 3

#trydropdown list

# <CustomDropDown>:
#     Button:
#         id:btn
#         text: ''
#         size_hint_y:
#         height:
#         on_release:dropdown.open(self)
#     DropDown:
#         id:dropdown
#         on_parent:self.dismiss()
#         on_select:btn.text = '{}'.format(args[1])
#         Button:
#             text:
#             size_hint_y:
#             height:
#             on_release:dropdown.select()
       

############################### This is a divider ###########################################

<ControlScreen>:
    id: controlscreen
    ControlBackgroundImage:
        allow_stretch: True
        keep_ratio: False
        opacity: 0.3
        source: 'piping.jpg'
        size: self.size
        pos: self.pos

        canvas:
            Color:
                rgba: get_color_from_hex('#404040')
            Rectangle:
                size: self.size
                pos: self.pos
''')



class LoginBackgroundImage(Image):
    pass

class LoginMenu(BoxLayout):

    canvas_opacity = NumericProperty(0)

    def changeLoginBtnColor(self, parent):
        with self.canvas:
            self.color=get_color_from_hex('#00ff00')
            print(parent)
            Ellipse(parent.pos[0] - parent.size[1]/2.0, parent.pos[1], parent.size[1],parent.size[1], 180, 360)
            Ellipse(parent.size[0] + parent.pos[0] - parent.size[1]/2.0, parent.pos[1],parent.size[1], parent.size[1],360,540)

    def show_canvas(self):
        self.canvas_opacity = 1

    def clear_canvas(self):
        self.canvas_opacity = 0

class LoginTextInput(TextInput):

    # Override the insert_text to limit the maximum input character
    def insert_text(self, substring, from_undo=False):
        maxLength = 12
        length =len(self.text)
        if length >= maxLength:
            return super(LoginTextInput, self).insert_text("", from_undo=from_undo)
        else:
            return super(LoginTextInput, self).insert_text(substring, from_undo=from_undo)


class LoginButton(Button):

    # Link widget using ObjectPorperty()
    username = ObjectProperty()
    password = ObjectProperty()
    loginscreen = ObjectProperty()

    # Trigger when login button is pressed
    def login(self, parent, pos):

        # Check database for validation
        parent.show_canvas()
        self.check_database()

    def remove_background(self, parent):
        parent.clear_canvas()
        
    def check_database(self):
        if len(self.username.text.strip()) > 0 and len(self.password.text.strip())>0:
            result = usr_database.get("/" + self.username.text.strip())
            print(self.username.text.strip())
            print(self.password.text.strip())
            print(result)
            print(result == self.password.text)
            if result == self.password.text:
                # Go to control page
                self.loginscreen.manager.transition.direction = 'left'
                self.loginscreen.manager.current = 'controlscreen'
                
            else:
                # Prompt the error window and clear the username and password textinput
                self.username.text = ""
                self.password.text = ""
                self.loginscreen.openPopup(1)

        elif len(self.username.text.strip()) > 0:
            self.loginscreen.openPopup(2)

        elif len(self.password.text.strip()) > 0:
            self.loginscreen.openPopup(3)
        else:
            self.loginscreen.openPopup(4)
            
            

class QuitButton(Button):
    
    def quit_app(self):
        App.get_running_app().stop()

class LoginScreen(Screen):

    def openPopup(self, opt):
        if opt == 1:
            # Popup for fail login
            popup = Popup(title='Login Failed', title_size=self.size[0]*0.01,\
                          content=Label(text='Incorrect username or password.'),\
                          size_hint=(None, None), size=(self.size[0]*0.3, self.size[0]*0.3),\
                          on_touchdown=self.dismisspopup)
            popup.open()
        
        elif opt == 2:
            # Popup for missing password
            popup = Popup(title='Insufficient Input', title_size=self.size[0]*0.01,\
                          content=Label(text='Please enter your password.'),\
                          size_hint=(None, None), size=(self.size[0]*0.3, self.size[0]*0.3),\
                          on_touchdown=self.dismisspopup)
            popup.open()

        elif opt == 3:
            # Popup for missing username
            popup = Popup(title='Insufficient Input', title_size=self.size[0]*0.01,\
                          content=Label(text='Please enter your username.'),\
                          size_hint=(None, None), size=(self.size[0]*0.3, self.size[0]*0.3),\
                          on_touchdown=self.dismisspopup)
            popup.open()

        elif opt == 4:
            # Popup for no info input
            popup = Popup(title='Insufficient Input', title_size=self.size[0]*0.01,\
                          content=Label(text='Please enter your username and password.'),\
                          size_hint=(None, None), size=(self.size[0]*0.3, self.size[0]*0.3),\
                          on_touchdown=self.dismisspopup)
            popup.open()

    def dismisspopup(self,instance, touch):
        self.popup.dismiss()

    def quit_app(self):
        App.get_running_app().stop()


class ControlScreen(Screen):
       
    pass

    def change_to_toggle(self,value):
        print("enter2 pressed")
                    
        if self.t5.text not in self.blk:

    
            if self.t8.text not in self.floor:

                self.popup = Popup(title='', content=Label(text='Please key in valid Block and Floor \n\n\n            -click to try again-'),size_hint=(0.3, 0.3),auto_dismiss=False, on_touch_down=self.dismisspopup)      
                self.popup.open()
            else:
                self.popup = Popup(title='', content=Label(text='Please key in valid Block \n\n\n            -click to try again-'),size_hint=(0.3, 0.3),auto_dismiss=False, on_touch_down=self.dismisspopup)      
                self.popup.open()
                
        elif self.t8.text not in self.floor:

                self.popup = Popup(title='', content=Label(text='Please key in valid Floor \n\n\n            -click to try again-'),size_hint=(0.3, 0.3),auto_dismiss=False, on_touch_down=self.dismisspopup)      
                self.popup.open()    
        else:
            self.manager.transition.direction = 'left'
            self.manager.current = "toggle"
    def dismisspopup(self,instance, touch):
        print("failed login")
        self.popup.dismiss()
        
               
    def change_to_menu(self,value):
        self.manager.transition.direction = 'right'
     
        self.manager.current= "menu"


class ControlBackgroundImage(Image):
    pass

class Toggle(Screen):
    def __init__(self, **kwargs):
        super().__init__( **kwargs)
        self.layout=GridLayout(cols=4,padding=50,spacing=10)
        with self.canvas:
    # Add a red color
            
            Rectangle(pos=(0,0), size=(900, 600),source="pipe.jpg")
            
        self.add_widget(self.layout)
        
        self.blk = ['1','2','3','4','5','6']
        self.floor = ['1','2','3','4','5','6','7','8','9','10']
        self.unit = ['1','2','3','4']
        

#Button(text="[color=000000][b]Progress[/b][/color]", on_press=self.change_to_progress, font_size=70,background_normal = 'growth.jpg', markup = True)
       
        self.l1=Label(text=",",valign='bottom',halign='left',font_size=19,font_name='Montserrat-Regular',padding_y=0)
        with self.l1.canvas:
            Color(0, 0, 0, 0.3)
            Rectangle(pos=(0,460), size=(900,220))
        self.layout.add_widget(self.l1)
        l2=Label(text='', valign='bottom',halign='center',font_size=28)
        self.layout.add_widget(l2)
        back=Button(text="Back",on_press=self.back,font_size=26,size_hint= (0.1,0.1),background_color=[1, 1, 1, 0],font_name='Montserrat-Bold')
        self.layout.add_widget(back)
        self.but3=Button(text='|      Logout ',on_press=self.change_to_menu,font_size=26,size_hint= (0.1,0.1),background_color=[1, 1, 1, 0],font_name='Montserrat-Bold',padding_y=10)
        self.layout.add_widget(self.but3)
        
    
        self.border10_1=Label(text="")
        self.layout.add_widget(self.border10_1)
        self.border10=Label(text="Status :",font_name='Montserrat-Regular',valign='bottom',halign='right',font_size=27)
        self.layout.add_widget(self.border10)
        
        self.STATUS=Label(text="Valve Open",font_name='Montserrat-Bold',valign='bottom',halign='center',font_size=27)## get the state and update tis one ,Thanks
        self.layout.add_widget(self.STATUS)
        
        self.border10_3=Label(text="")
        self.layout.add_widget(self.border10_3)
        
        self.border11=Label(text="",size_hint= (0.3,0.3))
        self.layout.add_widget(self.border11)
        tgglbtnON=Button(text="open valve",on_press=self.openvalve,font_size=24,font_name="Montserrat-Bold",size_hint= (0.55,0.55))
        self.layout.add_widget(tgglbtnON)
        tgglbtnOFF=Button(text="close valve",on_press=self.closevalve,font_size=24,font_name="Montserrat-Bold",size_hint= (0.55,0.55))
        self.layout.add_widget(tgglbtnOFF)
        self.border12_2=Label(text="",size_hint= (0.3,0.3))
        self.layout.add_widget(self.border12_2)
        
        self.border11=Label(text="")
        self.layout.add_widget(self.border11)
        self.border10_2=Label(text="")
        self.layout.add_widget(self.border10_2)
        self.border10_3=Label(text="")
        self.layout.add_widget(self.border10_3)
        self.border10_5=Label(text="")
        self.layout.add_widget(self.border10_5)
       
#        self.border13=Label(text="",size_hint= (0.3,0.3))
#        self.layout.add_widget(self.border13)
#        self.border13_2=Label(text="",size_hint= (0.3,0.3))
#        self.layout.add_widget(self.border13_2)
#        self.border13_3=Label(text="",size_hint= (0.3,0.3))
#        self.layout.add_widget(self.border13_3)
#        
#        l2_1=Label(text='', valign='bottom',halign='center',font_size=28)
#        self.layout.add_widget(l2_1)
#        
        
    def dismisspopup(self,instance, touch):
        print("failed login")
        self.popup.dismiss()
        
           
    def openvalve(self,touch):
        self.opendisplay.text="Valve Open"
        self.closeddisplay.text=""
        
    def closevalve(self,touch):
        print("clicked/touched down")
        self.closeddisplay.text="Valve Closed"
        self.opendisplay.text=""
        
        
    def change_to_menu(self,value):
        self.manager.transition.direction = 'right'
        self.manager.current= "menu"
        
    def back(self,value):
        self.manager.transition.direction = 'left'      
        self.manager.current= 'settings'
    

class SwitchScreenApp(App):
    def build(self):
            sm = ScreenManager()
            loginscreen = LoginScreen(name='login')
            controlscreen = ControlScreen(name='controlscreen')
            # tgl=Toggle(name="toggle")
            # err=SettingsScreen(name="error")
            # sm.add_widget(err)
            sm.add_widget(loginscreen)
            sm.add_widget(controlscreen)
            # sm.add_widget(tgl)
            sm.current='login'
            return sm

if __name__=='__main__':
    usr_url = "https://user-ebff1.firebaseio.com/"
    usr_token = "TDrEhWg2htZPnCl6BYXQEkU1lzwVR09CpvEuT4PL"
    usr_database = firebase.FirebaseApplication(usr_url, usr_token)

    SwitchScreenApp().run()