#!/usr/bin/python3

# main.py
#     testing interface for RPi based on Kv lang tutorial

import kivy
kivy.require('1.11.1')

from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty


class Controller(FloatLayout):

    ''' Recieves custom widget from Kv file w/ do_action specified in Kv '''

    label_wid = ObjectProperty()
    info = StringProperty()

    def do_action(self):
        self.label_wid.text = 'Label after button press'
        self.info = 'New info text'


class ControllerApp(App):

    def build(self):
        return Controller(info='Hello World')

if __name__ == '__main__':
    ControllerApp().run()
