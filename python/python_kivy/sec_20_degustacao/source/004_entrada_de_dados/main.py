#coding: utf-8

from kivy.app import App 
from kivy.uix.textinput import TextInput 

def build():
    return TextInput(text="Componente de Entrada de texto: ")

janela = App()
janela.build = build
janela.run()
