import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.graphics import Line

class Touch(Widget):

    def __init__(self, **kwargs):
        super(Touch, self).__init__(**kwargs)

        with self.canvas:
            Line(points=(20,30, 400, 500))
            Color(1,0,0,0.5, mode="rgba")
            self.rect = Rectangle(pos=(0,0), size=(50,50))
            Color(1,1,0,0.5, mode="rgba")
            self.rect1 = Rectangle(pos=(200,300), size=(50,50))


    def on_touch_down(self, touch):
        self.rect.pos = touch.pos
        print("mouse down", touch)
    
    def on_touch_move(self, touch):
        self.rect1.pos = touch.pos
        print("mouse move", touch)
    
    def on_touch_up(self, touch):
        print("mouse up", touch)




class RateMe(App):

    def build(self):
        return Touch()


if __name__ == "__main__":
    RateMe().run()