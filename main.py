import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class AppGrid(Widget):
    name = ObjectProperty(None)
    lastname = ObjectProperty(None)
    email = ObjectProperty(None)



    def btn_submit(self):

        print(self.name.text, self.email.text, self.lastname.text)

        self.name.text=""
        self.email.text=""
        self.lastname.text=""
        

        

class RateMe(App):

    def build(self):
        return AppGrid()


if __name__ == "__main__":
    RateMe().run()