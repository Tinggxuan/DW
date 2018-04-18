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
from kivy.uix.spinner import Spinner, SpinnerOption
from kivy.uix.bubble import Bubble
from kivy.uix.behaviors import ToggleButtonBehavior

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

############# Login Screen child widget attribute #############

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
       
############################### This is a divider ###############################

<ControlScreen>:
    id: controlscreen
    ControlBackgroundImage:
        allow_stretch: True
        keep_ratio: False
        opacity: 0.4
        source: 'piping.jpg'
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
                text: 'Control Center'
                font_size: self.height*1.1
                font_name: 'Gugi-Regular'
                size_hint: 1, 1

        ControlOptionMenu:
            pos_hint: {'x': -0.3, 'y':0.55}
            Label:
                text: 'Block'
                font_size: self.height*0.9
                font_name: 'Gugi-Regular'
                size_hint: 1, 1
        
        ControlOptionMenu:
            pos_hint: {'x': -0.3, 'y':0.35}
            Label:
                text: 'Floor'
                font_size: self.height*0.9
                font_name: 'Gugi-Regular'
                size_hint: 1, 1

        BoxLayout:
            pos_hint: {'x': 1.3, 'y': 0.9}
            size_hint: 0.15, 0.05
            LogoutButton:
                controlscreen: controlscreen
                
        BoxLayout:
            pos_hint: {'x': 1.198, 'y': 0.9}
            size_hint: 0.08, 0.05
            SmallQuitButton:

        BoxLayout:
            pos_hint: {'center_x': 0.5, 'y': 0.1}
            size_hint: 0.15, 0.1
            EnterButton:
                controlscreen: controlscreen

        BoxLayout:
            size_hint: 0.5, 0.1
            pos_hint: {'x':0.5, 'y':0.55}
            # canvas:
            #     Color:
            #         rgba: 0,1,0,1
            #     Rectangle:
            #         size: self.size
            #         pos: self.pos
            # Button:
            #     size_hint: self.size
            #     text: "Please select the floor unit"
            #     font_size: self.height*0.9
            #     font_name: 'Gugi-Regular'


        MyThing:
            text: ''
            font_size: self.height*0.5
            max: 2
            values: ["1"]
            size_hint: None,None
            size: (280,130)
            background_normal: "./T/1.png" 
            pos_hint: {'center_x':0.7,'center_y':0.599}
            background_down: "./T/xin.png"
           # background_color: 1,1,1,1

        MyThing:
            text: ''
            font_size: self.height*0.5
            values: ["1", "2"]
            size_hint: None, None
            background_normal: "./T/1.png" 
            pos_hint: {'center_x':0.7,'center_y':0.4}
            size: (280,130)
            background_down: "./T/xin.png"
        
                

############# Control Screen child widget attribute #############
<ControlOptionMenu>:
    size_hint: 1, 0.1

<LogoutButton>
    text: 'LOGOUT'
    font_size: self.height*0.6
    padding_y: self.height*0.1
    font_name: 'Gugi-Regular'
    background_color: 0,0,0,0
    on_press: self.logout(self.parent, self.parent.pos)
    on_release: self.parent.clear_canvas()

    canvas.after:
        Color:
            rgba: get_color_from_hex('#ffffff')
        Line:
            points: self.pos[0]-self.size[0]*0.05 , self.pos[1], self.pos[0] + self.size[0], self.pos[1]
            width: 3
        Line:
            points: self.pos[0]-self.size[0]*0.05, self.pos[1] + self.size[1], self.pos[0] + self.size[0], self.pos[1] + self.size[1]
            width: 3
        Line:
            points: self.pos[0]-self.size[0]*0.05, self.pos[1], self.pos[0]-self.size[0]*0.05, self.pos[1] + self.size[1]
            width: 3
        Line:
            ellipse: self.size[0] + self.pos[0] - self.size[1]/2.0, self.pos[1], self.size[1], self.size[1], 360, 540
            width: 3
    

<SmallQuitButton>:
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
            points: self.pos[0] , self.pos[1], self.pos[0] + self.size[0]*1.2, self.pos[1]
            width: 3
        Line:
            points: self.pos[0], self.pos[1] + self.size[1], self.pos[0] + self.size[0]*1.2, self.pos[1] + self.size[1]
            width: 3
        Line:
            ellipse: self.pos[0] - self.size[1]/2.0, self.pos[1], self.size[1], self.size[1], 180, 360
            width: 3
        Line:
            points: self.pos[0] + self.size[0]*1.2, self.pos[1] + self.size[1], self.pos[0] + self.size[0]*1.2, self.pos[1]
            width: 3

<EnterButton>:
    text: 'ENTER'
    font_size: self.height*0.6
    padding_y: self.height*0.1
    font_name: 'Gugi-Regular'
    background_color: 0,0,0,0
    on_press: self.trypopup() #unfinished

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

# <DropDownButton@Button>:
#     font_size: self.height*0.6
#     padding_y: self.height*0.1
#     font_name: 'Gugi-Regular'
#     background_color: 0,0,0,0



#!text
#:kivy 1.7.2
#:import Factory kivy.factory.Factory

#:set color_button (0.85, 0.85, 0.85, 0.85)  
#:set color_button_pressed (0.6, 0.6, 0.6, 0.6) 
#:set color_font   (0.957, 0.890, 0.843, 1)  # off white

<MyThingButton@Button>
    #background_down: "./NOT.png"           
    #background_normal: "./NOT.png"
    font_size: self.height*0.5
    allow_stretch: True
        # size_hint = 0.1, 0.1
    

<MySpinnerOption@SpinnerOption>:
    background_color: color_button if self.state == 'down' else color_button_pressed
    #background_normal: "./T/YES.png"
    #background_down: "./T/niao.png" #"atlas://data/images/defaulttheme/button"
    allow_stretch: True
    #background_disabled_normal: "./T/niao.jpg"
    color: color_font
    font_size: self.height*0.5
 
<MyThing@Spinner>: #Spinner:
    text: ""
    values: ["1", "2", "3","4","5","6","7"]
    # background_color: color_button if self.state == 'normal' else color_button_pressed
    background_color: 1,1,1,1
    background_normal: "./piping.png" 
    background_down: "./piping.png"   
    allow_stretch: True        
    color: color_font
    option_cls: Factory.MySpinnerOption
    size_hint: 2,2
    #####pos_hint= {'top':0.7,'right":0.6}


############################### This is a divider ###############################
''')
class Toggleslider(ToggleButtonBehavior, Image):
    def __init__(self, **kwargs):
        super(Toggleslider, self).__init__(**kwargs)
        self.source = './T/CLOSED.png'
        #self.size_hint = (0.7,0.7)

    def on_state(self, widget, value):
        if value == 'down' and self.source == './T/CLOSED.png':
            self.source = './T/MIDDLE.png' 
            self.source = './T/OPENED.png'
        else:
            self.source = './T/MIDDLE.png' 
            self.source = './T/CLOSED.png'
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
        
    def check_database(self):
        if len(self.username.text.strip()) > 0 and len(self.password.text.strip())>0:
            result = str(usr_database.get("/" + self.username.text.strip()))
            if result == self.password.text:
                # Go to control page
                self.username.text = ""
                self.password.text = ""
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

############### This is a divider ###################

class ControlScreen(Screen):
     
    #def layout(self):
    #layout = BoxLayout(orientation="vertical")
    #btn1 = Button()
    #btn2 = Button()
    #layout.add_widget(btn1)
    #layout.add_widget(btn2)

    def trypopup(self):
        print('yes')
        #popup = Popup(title='Control Setting', title_size=60,content=Button(text='yes'),size_hint=(0.7, 0.7), size=(self.size[0]*0.6, self.size[0]*0.6),title_align='center')
        #popup.open()
        self.box=BoxLayout(orientation="vertical")
        #self.box = FloatLayout(size=(0.5,0.5))
        toggle=Toggleslider()
        self.box.add_widget(toggle)

        #self.box.add_widget(Label(font_name="Gugi-Regular",text="lala"))
        self.box.add_widget(Button(font_name="Gugi-Regular",text="CLOSE",color=(0,0,0,1), font_size=48, size_hint=(0.2,0.2),pos_hint={'center_x':0.5,'center_y':0.3},on_press=self.exit_,background_normal="./T/YES.png"))
        #content = Button(text="Close",size_hint=(0.1,0.1))

        self.popup = Popup(title='Control Setting',title_font="Gugi-Regular", title_size=100, content=self.box, size_hint=(0.6, 0.6), size=(self.size[0]*0.6, self.size[0]*0.6),title_align='center',auto_dismiss=False,background="./T/shui.png")
        
        self.popup.open()
        
        #popup = Popup(content = content, auto_dismiss=False,size_hint=(0.3,0.3))
        #popup.open()
        #pop = Popup(title="Control Setting", size_hint=(0.5,0.5),title_size=24,title_align='center', auto_dismiss=True)
        #pop.open()
    def exit_(self,value):
        self.popup.dismiss()

class ControlBackgroundImage(Image):
    pass

class ControlOptionMenu(BoxLayout):
    canvas_opacity = NumericProperty(0)

    def changeLogoutBtnColor(self, parent):
        with self.canvas:
            self.color=get_color_from_hex('#00ff00')
            print(parent)
            Ellipse(parent.pos[0] - parent.size[1]/2.0, parent.pos[1], parent.size[1],parent.size[1], 180, 360)
            Ellipse(parent.size[0] + parent.pos[0] - parent.size[1]/2.0, parent.pos[1],parent.size[1], parent.size[1],360,540)

    def show_canvas(self):
        self.canvas_opacity = 1

    def clear_canvas(self):
        self.canvas_opacity = 0

class LogoutButton(Button):
    controlscreen = ObjectProperty()

    def logout(self, parent, pos):
        parent.show_canvas()
        self.controlscreen.manager.transition.direction = 'right'
        self.controlscreen.manager.current = 'loginscreen'


class SmallQuitButton(Button):
    
    def quit_app(self):
        App.get_running_app().stop()

class EnterButton(Button):
    controlscreen = ObjectProperty()

    def trypopup(self):
        print('lala')
        self.controlscreen.trypopup()
        #pop = Popup(title="Control Setting", size_hint=(0.5,0.5),title_size=24,title_align='center', auto_dismiss=True)
        #pop.open()
    
    # def controlunit(self):
        # Go to the 'switchscreen' with all the parameter needed
        # self.controlscreen.manager.transition.direction = 'left'
        # self.controlscreen.manager.current = 'switchscreen'




class cut_copy_paste(Bubble):
    pass


class BubbleShowcase(FloatLayout):

    def __init__(self, **kwargs):
        super(BubbleShowcase, self).__init__(**kwargs)
        self.but_bubble = Button(text='Press to show bubble')
        self.but_bubble.bind(on_release=self.show_bubble)
        self.add_widget(self.but_bubble)

    def show_bubble(self, *l):
        if not hasattr(self, 'bubb'):
            self.bubb = bubb = cut_copy_paste()
            self.add_widget(bubb)
        else:
            values = ('left_top', 'left_mid', 'left_bottom', 'top_left',
                'top_mid', 'top_right', 'right_top', 'right_mid',
                'right_bottom', 'bottom_left', 'bottom_mid', 'bottom_right')
            index = values.index(self.bubb.arrow_pos)
            self.bubb.arrow_pos = values[(index + 1) % len(values)]

############### This is a divider ###################

from kivy.uix.scrollview import ScrollView

class MyThingButton(ScrollView):
    def __init__(self,MyThing,**kwargs):
        super().__init__(**kwargs)


###################### DIVIDER ########

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
            loginscreen = LoginScreen(name='loginscreen')
            controlscreen = ControlScreen(name='controlscreen')
            # tgl=Toggle(name="toggle")
            # err=SettingsScreen(name="error")
            # sm.add_widget(err)
            sm.add_widget(loginscreen)
            sm.add_widget(controlscreen)
            # sm.add_widget(tgl)
            sm.current='loginscreen'
            return sm

if __name__=='__main__':
    usr_url = "https://user-ebff1.firebaseio.com/"
    usr_token = "TDrEhWg2htZPnCl6BYXQEkU1lzwVR09CpvEuT4PL"
    usr_database = firebase.FirebaseApplication(usr_url, usr_token)

    building_control_url = "https://building-control-f7747.firebaseio.com/"
    building_control_token = "BRSEyh9LmukzG7ocB6D73zmA9kx7AkatgJWLmLpe"
    building_control_database = firebase.FirebaseApplication(building_control_url, \
                                building_control_token)

    SwitchScreenApp().run()