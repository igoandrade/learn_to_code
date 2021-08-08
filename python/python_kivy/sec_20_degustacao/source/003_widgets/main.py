#coding: utf-8

from kivy.app import App 
from kivy.uix.button import Button 

def click():
    print("O botão foi pressionado")

def build():
    bt=Button(text="Clique Aqui")
    bt.on_press = click
    return bt

janela=App()
janela.build=build
janela.run()