
from kivy.uix.button import Button
class square(Button):
    def __init__(self,color='default',number=0,**kwargs):
        super(square,self).__init__(**kwargs)
        switcher = {
            'blue': [0,0,255,1],
            'red': [255,0,0,1],
            'white':[255,255,255,1],
            'green':[0,128,0,1],
            'orange':[255,0,255,1],
            'yellow':[255,255,0,1],
        }
        self.background_color = switcher.get(color,[1,1,1,1])
        self.text = '%d'%number
        self.color = [0,0,0,1]  # make debugging easier (to be deleted)
    def getcolor(self):
        return self.color