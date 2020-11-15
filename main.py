from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from database import DataBase
from kivy.factory import Factory
from kivy.animation import Animation
from kivy.garden.matplotlib import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvas

Builder.load_string("#:import utils kivy.utils")


class CreateAccountWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count("@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)

                self.reset()

                sm.current = "login"
            else: 
                invalidForm()
        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""


class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def loginBtn(self):
        if db.validate(self.email.text, self.password.text):
            MainWindow.current = self.email.text
            self.reset()
            sm.current = "main"
            print('hereeee')
        else:
            invalidLogin()
            print('here')

    def createBtn(self):
        self.reset()
        sm.current = "create"

    def reset(self):
        self.email.text = ""
        self.password.text = ""


class MainWindow(Screen):
    n = ObjectProperty(None)
    created = ObjectProperty(None)
    email = ObjectProperty(None)
    current = ""

    def logOut(self):
        sm.current = "login"

    def on_enter(self, *args):
        self.plot.clear_widgets()
        password, name, created = db.get_user(self.current)
        self.n.text = "Account Name: " + name
        self.email.text = "Email: " + self.current
        self.created.text = "Created On: " + created
        x = np.random.rand(100)
        fig, ax = plt.subplots()
        ax.hist(x)
        canvas =  FigureCanvas(figure=fig)

        self.plot.add_widget(canvas)

class WindowManager(ScreenManager):
    pass


def invalidLogin():
    pop = Popup(title='Invalid Login',
                  content=Label(text='Invalid username or password.'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()


def invalidForm():
    pop = Popup(title='Invalid Form',
                  content=Label(text='Please fill in all inputs with valid information.'),
                  size_hint=(None, None), size=(400, 400))

    pop.open()


# kv = Builder.load_file("rateme.kv")

sm = ScreenManager()
# sm.add_widget(Factory.LoginWindow(name="login"))
# sm.add_widget(CreateAccountWindow(name="create"))
# sm.add_widget(MainWindow(name="main"))
# sm.current = "login"
db = DataBase("users.txt")

# screens = [LoginWindow(name="login"), CreateAccountWindow(name="create"),MainWindow(name="main")]
# for screen in screens:
#     sm.add_widget(Factory.screen)




class RateMe(MDApp):

    def __init__(self, **kwargs):
        self.title = "Rate Me"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        # sm = ScreenManager()
        
        super().__init__(**kwargs)

    def animate_card(self, widget):
        anim = Animation(pos_hint={"center_y": 0.6})
        anim.start(widget)
    def animate_background(self, widget):
        anim = Animation(size_hint_y=0.8)
        anim.start(widget.ids.widget_row)

    def build(self):
        # sm.add_widget(Factory.LoginWindow())
        sm.add_widget(Factory.LoginWindow(name="login"))
        sm.add_widget(CreateAccountWindow(name="create"))
        sm.add_widget(MainWindow(name="main"))
        # sm.current = "login"
        return sm


if __name__ == "__main__":
    RateMe().run()