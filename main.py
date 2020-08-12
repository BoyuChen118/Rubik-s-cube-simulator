import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from cubeface import cubeface
from buttonpanel import buttonpanel
        

class cube(GridLayout):
    def __init__(self,**kwargs):
        super(cube,self).__init__(**kwargs)
        self.cols=4
        self.Y = ['yellow']*9
        self.W = ['white']*9
        self.O = ['orange']*9
        self.R = ['red']*9
        self.G = ['green']*9
        self.B = ['blue']*9
        self.faces = [self.Y,self.W,self.O,self.R,self.G,self.B]
        self.reupdate()
    def reupdate(self):  # function that redraws the cube
        self.add_widget(Label(text='')) #place holder
        self.add_widget(cubeface(self.B))
        self.add_widget(Label(text='')) #place holder
        self.add_widget(Label(text='')) #place holder

        self.add_widget(cubeface(self.R))
        self.add_widget(cubeface(self.W))
        self.add_widget(cubeface(self.O))
        self.add_widget(cubeface(self.Y))

        self.add_widget(Label(text='')) #place holder
        self.add_widget(cubeface(self.G))
        self.add_widget(buttonpanel(self)) #place holder
        self.add_widget(Label(text='')) #place holder
class TestApp(App):
    def build(self): 
        return cube()


if __name__ == '__main__':
    TestApp().run()