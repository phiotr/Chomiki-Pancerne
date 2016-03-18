# -*- coding: utf-8 -*-

from kivy.app import App

from kivy.lang import Builder

from kivy.properties import ObjectProperty, NumericProperty, BooleanProperty

from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

kv = """

"""


class SomeApp(App):

    def build(self):
        
        Builder.load_string(kv)
        
        
        return ...

    def on_pause(self):
        return True

    def on_resume(self):
        return True


if __name__ == '__main__':
    SomeApp().run()
