import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class AppGrid(Widget):
   pass
        

        

class RateMe(App):

    def build(self):
        return AppGrid()


if __name__ == "__main__":
    RateMe().run()