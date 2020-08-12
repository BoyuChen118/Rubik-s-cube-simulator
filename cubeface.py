from kivy.uix.gridlayout import GridLayout
from square import square
class cubeface(GridLayout):
    def __init__(self,color,**kwargs):
        super(cubeface,self).__init__(**kwargs)
        self.cols=3
        self.squares = []
        for counter,i in enumerate(color):
            s = square(i,counter)
            self.squares.append(s)  #contains all squares of this particular face
            self.add_widget(s)