import kivy
kivy.require("2.0.0")
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

def funcSelf(x):
    print("self")

Button.funcSelf = funcSelf

class Tela(BoxLayout):
    def funcRoot(self):
        print("root")
        self.ids.lb1.text = 'root'

class KeyWordsApp(App):
    def funcApp(self):
        print("app")

janela = KeyWordsApp()
janela.run()