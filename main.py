from main import *
from kivymd.app import MDApp
from kivy.uix.textinput import TextInput
from kivymd.uix.label import MDLabel

class App (MDApp):
    def app_buil(self):

        self.text = TextInput(text="Hello Ox",halign="center")
    
if __name__=="__main__":
    App().run()

