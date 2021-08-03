#coding: utf-8

from kivy.app import App 
from kivy.uix.floatlayout import FloatLayout 
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

from kivy.core.window import Window

def click():
    print(ed.text)

def build():
    layout = FloatLayout()

    lb = Label(text = "Digite alguma coisa:")
    lb.size_hint = None, None
    lb.height = 50
    lb.width = 400
    lb.x = 100
    lb.y = 550


    global ed
    ed = TextInput(text="")
    ed.size_hint = None, None
    ed.height = 300
    ed.width = 400
    ed.x = 100
    ed.y = 250

    bt = Button(text="Clique aqui")
    bt.size_hint = None, None
    bt.height = 50
    bt.width = 200
    bt.x = 200
    bt.y = 100

    bt.on_press = click

    layout.add_widget(lb)
    layout.add_widget(ed)
    layout.add_widget(bt)

    return layout


Window.size = 600, 600
app = App()
app.title = "Tela de Verdade"
app.build = build
app.run()