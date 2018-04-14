# Change and save the configuration
from kivy.config import Config
Config.set('graphics', 'resizable', '0') # Disable window resize
Config.set('graphics', 'fullscreen', 'auto')

# Import UI module
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button 
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.behaviors import ButtonBehavior
from kivy.core.audio import SoundLoader
from kivy.core.image import Image
#from kivy.graphics import BorderImage
from kivy.graphics import Color, Rectangle
from kivy.uix.popup import Popup

useridpassword={"1":"2","Linhao":"Smiley%7654"}
# error = SoundLoader.load('12915_sweet_trip_mm_kick_mid.wav')
class MyLabel(Label): #MyLabel 
    def __init__(self,**kwargs):
        Label.__init__(self,**kwargs)
        self.bind(size=self.setter('text_size'))
        self.padding=(50,50)
        self.font_size=24
        self.halign='center'
        self.valign='middle'

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas:
            # Add a red color
            Rectangle(pos=(0,0), size=(900, 600),source="backgroundimg.jpg")
            Color(0, 0, 0 )
            
        self.layout=GridLayout(cols=4,padding=70,spacing=30)
        self.add_widget(self.layout)
        self.border1_1=Label(text="")
        self.layout.add_widget(self.border1_1)
        self.border1_2=Label(text="")
        self.layout.add_widget(self.border1_2)
        self.border1_3=Label(text="")
        self.layout.add_widget(self.border1_3)
        self.border1_4=Label(text="")
        self.layout.add_widget(self.border1_4)
        self.border2_1=Label(text="")
        self.layout.add_widget(self.border2_1)
        
        self.borderex_1=Label(text="")
        self.layout.add_widget(self.borderex_1)
        self.borderex_2=Label(text="")
        self.layout.add_widget(self.borderex_2)
        self.borderex_3=Label(text="")
        self.layout.add_widget(self.borderex_3)
        self.borderex_4=Label(text="")
        self.layout.add_widget(self.borderex_4)
        
        
        l1=Label(text='UserName',font_size=30,halign='right',valign='bottom',font_name='Montserrat-Bold')
        self.layout.add_widget(l1)
        self.t1=TextInput(hint_text="Username:",multiline=False,size_hint= (0.25,0.05),font_name='Montserrat-Regular')
        self.layout.add_widget(self.t1)
        
        self.border2_3=Label(text="")
        self.layout.add_widget(self.border2_3)
        self.border3_1=Label(text="")
        self.layout.add_widget(self.border3_1)
        
        
        l2=Label(text='Password',font_size=30,halign='right',valign='top',font_name='Montserrat-Bold')
        self.layout.add_widget(l2)
        self.t2=TextInput(hint_text="Password",multiline=False,size_hint= (0.25,0.05),font_name='Montserrat-Regular')
        self.layout.add_widget(self.t2)
        
        self.border3_3=Label(text="")
        self.layout.add_widget(self.border3_3)
        self.border4_1=Label(text="")
        self.layout.add_widget(self.border4_1)
        
        self.bordere_1=Label(text="")
        self.layout.add_widget(self.bordere_1)
        self.bordere_2=Label(text="")
        self.layout.add_widget(self.bordere_2)
        self.bordere_3=Label(text="")
        self.layout.add_widget(self.bordere_3)
        self.bordere_4=Label(text="")
        self.layout.add_widget(self.bordere_4)

        b1 = Button(text='Quit',on_press=self.quit_app,font_size=22,size_hint= (0.3,0.2),background_color=[47,0,0,0.75],font_name='Montserrat-Bold')
        self.layout.add_widget(b1)
        b2 = Button(text='Enter',font_size=22,size_hint= (0.3,0.2),background_color=[1, 154, 1, 0.8],on_press=self.enter,font_name='Montserrat-Bold')   
        self.layout.add_widget(b2)    
        
        self.border4_3=Label(text="")
        self.layout.add_widget(self.border4_3)
        self.border5_1=Label(text="")
        self.layout.add_widget(self.border5_1)
        self.border5_2=Label(text="")
        self.layout.add_widget(self.border5_2)
        self.border5_3=Label(text="")
        self.layout.add_widget(self.border5_3)
        self.border5_4=Label(text="")
        self.layout.add_widget(self.border5_4)
        
        self.border6_1=Label(text="")
        self.layout.add_widget(self.border6_1)
        self.border6_2=Label(text="")
        self.layout.add_widget(self.border6_2)
        self.border6_3=Label(text="")
        self.layout.add_widget(self.border6_3)
        self.border6_4=Label(text="")
        self.layout.add_widget(self.border6_4)
        self.popup = Popup(title='Invalid input', content=Label(text='Please key in valid information\n\n\n            -click to try again-'),size_hint=(0.3, 0.3),auto_dismiss=False, on_touch_down=self.dismisspopup)                                 
        b2.bind(on_press=self.enter)

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

    def quit_app(self, value):
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
            ms=MenuScreen(name='menu')
            st=SettingsScreen(name='settings')
            tgl=Toggle(name="toggle")
#            err=SettingsScreen(name="error")
#            sm.add_widget(err)
            sm.add_widget(ms)
            sm.add_widget(st)
            sm.add_widget(tgl)
            sm.current='menu'
            return sm

if __name__=='__main__':
    SwitchScreenApp().run()