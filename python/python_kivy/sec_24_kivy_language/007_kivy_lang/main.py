import kivy
kivy.require("2.0.0")
from kivy.app import App

code = """

<MeuBotao@Button>:
    text: "botao"

<Tela@BoxLayout>:
    orientation:'horizontal'

    MeuBotao:
    MeuBotao:
    MeuBotao:


BoxLayout:
    Tela:
    Tela:
        orientation: "vertical"
        

"""

from kivy.lang import Builder


class ClasseBuiderApp(App):
    def buid(self):
        return Builder.load_string(code)

janela = ClasseBuiderApp()
janela.run() 