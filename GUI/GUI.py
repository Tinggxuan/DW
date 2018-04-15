# Change and save the configuration
from kivy.config import Config
Config.set('graphics', 'resizable', '0') # Disable window resize
Config.set('graphics', 'fullscreen', 'auto')


# Register all the font
from kivy.core.text import LabelBase
LabelBase.register(name="Archivo_Black",  
                   fn_regular="./fonts/Archivo_Black/ArchivoBlack-Regular.ttf")

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


useridpassword={"1":"2","Linhao":"Smiley%7654"}

Builder.load_string('''
#:import get_color_from_hex kivy.utils.get_color_from_hex

<LoginScreen>:

    LoginBackgroundImage:
        allow_stretch: True
        keep_ratio: False
        opacity: 0.3
        source: 'login_background.jpeg'
        size: self.size
        pos: self.pos

        canvas:
            Color:
                rgba: get_color_from_hex('#0052cc')
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
                font_size: self.height*0.8
                font_name: 'Archivo_Black'
                size_hint: 1, 1

        LoginMenu:
            pos_hint: {'x': 0, 'y': 0.6}
            LoginTextInput:
                hint_text: 'Username'

        LoginMenu:
            pos_hint: {'x': 0, 'y': 0.45}        
            LoginTextInput:
                hint_text: 'Password'
                allow_copy: False
                password: True

        LoginMenu:
            pos_hint: {'center_x': 0.5, 'y': 0.25}
            canvas.before:
                Clear
            LoginButton:

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
            rgba: get_color_from_hex('#80aaff')
        Rectangle:
            size: self.size
            pos: self.pos

# Define the attribute of the LoginTextInput
<LoginTextInput>:
    size_hint: 1, 1
    font_size: self.height*0.7
    padding_y: self.height*0.1
    font_name: 'Archivo_Black'
    multiline: False
    hint_text_color: get_color_from_hex('#e6eeff')
    background_color: 0,0,0,0
    foreground_color: get_color_from_hex('#0041cc')
    cursor_color: get_color_from_hex('#0041cc')

    canvas.after:
        Color: 
            rgb: get_color_from_hex('#80aaff')
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
    font_size: self.height*0.7
    padding_y: self.height*0.1
    font_name: 'Archivo_Black'
    background_color: 0,0,0,0
    on_press: self.login(self.parent, self.parent.pos)

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
<QuitButton>:
    background_color: 0,0,0,0
    on_press: self.quit_app()
    canvas.after:
        Color:
            rgba: get_color_from_hex('#ffffff')
        # Ellipse:
        #     pos: self.pos
        #     size: self.size

        Color:
            rgb: get_color_from_hex('#ff0000')
        Line:
            cap: 'none'
            points: self.pos[0]+self.size[0]*0.25, self.pos[1]+self.size[1]*0.25, self.pos[0]+self.size[0]*0.75, self.pos[1]+self.size[1]*0.75
            width: 8
        Line:
            cap: 'none'
            points: self.pos[0]+self.size[0]*0.25, self.pos[1]+self.size[1]*0.75, self.pos[0]+self.size[0]*0.75, self.pos[1]+self.size[1]*0.25
            width: 8
        Line:
            ellipse: self.pos[0], self.pos[1], self.size[1], self.size[1], 180, 360
            width: 8
        Line:
            ellipse: self.pos[0], self.pos[1], self.size[1], self.size[1], 360, 540
            width: 8




<SettingsScreen>:
    BoxLayout:
        Label:
            text: 'Settings Screen'
            font_size: 50
        Button:
            text: 'Back to menu'
            font_size: 50
            on_press: 
                root.manager.transition.direction = 'right'
                root.manager.current = 'menu'

''')



class LoginBackgroundImage(Image):
    pass

class LoginMenu(BoxLayout):

    def changeLoginBtnColor(self, parent):
        with self.canvas:
            self.color=get_color_from_hex('#00ff00')
            print(parent)
            Ellipse(parent.pos[0] - parent.size[1]/2.0, parent.pos[1], parent.size[1],parent.size[1], 180, 360)
            Ellipse(parent.size[0] + parent.pos[0] - parent.size[1]/2.0, parent.pos[1],parent.size[1], parent.size[1],360,540)


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
    
    def login(self, parent, pos):

        with parent.canvas.before:
            Color(0, 0.902,0.6)
            Rectangle(size=self.size, pos=pos)

        with self.canvas.after:
            Color(0, 0.902,0.6)
            Ellipse(pos=(pos[0] - self.size[1]/2.0, pos[1]), size=(self.size[1],self.size[1]), angle_start=180, angle_end=360)
            Ellipse(pos=(self.size[0] + pos[0] - self.size[1]/2.0, pos[1]), size=(self.size[1],self.size[1]),angle_start=360,angle_end=540)
            Line(points=[self.pos[0] , self.pos[1], self.pos[0] + self.size[0], self.pos[1]],\
                 width=3)
            Line(points=[self.pos[0], self.pos[1] + self.size[1], self.pos[0] + self.size[0], self.pos[1] + self.size[1]],\
                 width=3)
            Line(ellipse=[self.pos[0] - self.size[1]/2.0, self.pos[1], self.size[1], self.size[1], 180, 360],\
                 width=3)
            Line(ellipse=[self.size[0] + self.pos[0] - self.size[1]/2.0, self.pos[1], self.size[1], self.size[1], 360, 540],\
                 width=3)

    def check_database(self, id, password):
        pass

class QuitButton(Button):
    
    def quit_app(self):
        App.get_running_app().stop()

class LoginScreen(Screen):
    
    def enter(self, value):
        print("enter preesed")
        print(str(self.t1.text))
        if self.t1.text in useridpassword:
            print("done1")
            if self.t2.text==useridpassword[self.t1.text]:
                self.manager.transition.direction = 'left'      
                self.manager.current= 'settings'
                self.username=self.t1.text
            else:
                self.popup.open()
        else:
            self.popup.open()

    def dismisspopup(self,instance, touch):
        print("failed login")
        self.popup.dismiss()

    def quit_app(self):
        App.get_running_app().stop()



#print(MenuScreen.self.t1.text)

class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__( **kwargs)
        self.layout=GridLayout(cols=3,padding=40,spacing=10)
        with self.canvas:
    # Add a red color
            
            Rectangle(pos=(0,0), size=(900, 600),source="building.jpg")
            
        self.add_widget(self.layout)
        
        self.blk = ['1','2','3','4','5','6']
        self.floor = ['1','2','3','4','5','6','7','8','9','10']
        self.unit = ['1','2','3','4']
        

#Button(text="[color=000000][b]Progress[/b][/color]", on_press=self.change_to_progress, font_size=70,background_normal = 'growth.jpg', markup = True)
       
        self.l1=Label(text="",valign='bottom',halign='left',font_size=22,font_name='Montserrat-Regular',padding_y=0)
        with self.l1.canvas:
            Color(1, 1, 1, 0.3)
            Rectangle(pos=(0,495), size=(900,200))

        self.layout.add_widget(self.l1)
        l2=Label(text='', valign='bottom',halign='center',font_size=28)
        self.layout.add_widget(l2)
        self.but3=Button(text='|  Logout ',on_press=self.change_to_menu,font_size=26,size_hint= (0.25,0.03),background_color=[1, 1, 1,0],font_name='Montserrat-Bold',padding_y=10)
        self.layout.add_widget(self.but3)
        
        self.border10=Label(text="",size_hint= (0.03,0.03))
        self.layout.add_widget(self.border10)
        self.border10_2=Label(text="",size_hint= (0.03,0.03))
        self.layout.add_widget(self.border10_2)
        self.border10_3=Label(text="",size_hint= (0.03,0.03))
        self.layout.add_widget(self.border10_3)
        
        
        l2_1=Label(text='', valign='bottom',halign='center',font_size=28)
        self.layout.add_widget(l2_1)
        l4=Label(text='Block',valign='bottom',halign='left',font_size=28,padding_x=0,padding_y=0,font_name='Montserrat-Bold')
        self.layout.add_widget(l4)
        l2_2=Label(text='', valign='top',halign='left',font_size=28)
        self.layout.add_widget(l2_2)
        
        l6=Label(text='',size_hint= (0.1,0.5))
        self.layout.add_widget(l6)
        self.t5=TextInput(hint_text='block number',multiline=False,size_hint= (0.1,0.6),font_name='Montserrat-Regular')
        self.layout.add_widget(self.t5)
        l6_2=Label(text='',size_hint= (0.1,0.5))
        self.layout.add_widget(l6_2)
        
        l7_1=Label(text='')
        self.layout.add_widget(l7_1)
        l7=Label(text='Floor',valign='bottom',halign='left',font_size=28,padding_x=0,padding_y=0,font_name='Montserrat-Bold')
        self.layout.add_widget(l7)
        l7_1=Label(text='')
        self.layout.add_widget(l7_1)
        
        l8_1=Label(text='',size_hint= (0.1,0.5))
        self.layout.add_widget(l8_1)
        self.t8=TextInput(hint_text='floor number',multiline=False,size_hint= (0.1,0.6),font_name='Montserrat-Regular')
        self.layout.add_widget(self.t8)
        l8_1=Label(text='',size_hint= (0.1,0.5))
        self.layout.add_widget(l8_1)
        
        l9=Label(text='')
        self.layout.add_widget(l9)
        self.border9_1=Label(text="")
        self.layout.add_widget(self.border9_1)
        self.border9_2=Label(text="")
        self.layout.add_widget(self.border9_2)
        self.border9_3=Label(text="",size_hint= (0.2,0.5))
        self.layout.add_widget(self.border9_3)
        
        b12=Button(text='Enter',font_size=24,size_hint= (0.2,0.5),background_color=[1, 154, 1, 1],on_press=self.change_to_toggle,font_name='Montserrat-Bold')
        self.layout.add_widget(b12)
        self.border6_1=Label(text="",size_hint= (0.2,0.5))
        self.layout.add_widget(self.border6_1)
        self.border6_2=Label(text="")
        self.layout.add_widget(self.border6_2)
        self.border6_3=Label(text="")
        self.layout.add_widget(self.border6_3)
        self.border6_4=Label(text="")
        self.layout.add_widget(self.border6_4)
        
        
    
        
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
            sm=ScreenManager()
            loginscreen=LoginScreen(name='login')
            st=SettingsScreen(name='settings')
            tgl=Toggle(name="toggle")
#            err=SettingsScreen(name="error")
#            sm.add_widget(err)
            sm.add_widget(loginscreen)
            sm.add_widget(st)
            sm.add_widget(tgl)
            sm.current='login'
            return sm

if __name__=='__main__':
    SwitchScreenApp().run()