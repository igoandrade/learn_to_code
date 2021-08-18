import kivy
kivy.require("2.0.0")

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class MinhaTela(BoxLayout):
    def click(self):
        print("oi")
        self.ids.lb1.text = ""
        self.ids.lb2.text = "10"

class Estudo3App(App):
    pass

janela = Estudo3App()
janela.run() 