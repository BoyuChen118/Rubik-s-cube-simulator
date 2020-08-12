import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
class buttonpanel(GridLayout):  # all ways user can interact with the cube is added
    def __init__(self,cube,**kwargs):
        super(buttonpanel,self).__init__(**kwargs)
        self.cols = 2
        self.padding = [15,15,15,15]
        self.cube = cube
        self.frontbutton = Button(text = 'F',font_size=13,on_press=self.frontcallback)

        self.add_widget(self.frontbutton)

        self.revfrontbutton = Button(text = 'F\'',font_size=13,on_press=self.revfrontcallback)
        self.add_widget(self.revfrontbutton)

        self.bottombutton = Button(text = 'B',font_size=13,on_press=self.bottomcallback)
        self.add_widget(self.bottombutton)

        self.revbottombutton = Button(text = 'B\'',font_size=13,on_press=self.revbottomcallback)
        self.add_widget(self.revbottombutton)

        self.rightbutton = Button(text = 'R',font_size=13,on_press=self.rightcallback)
        self.add_widget(self.rightbutton)

        self.revrightbutton = Button(text = 'R\'',font_size=13,on_press=self.revrightcallback)
        self.add_widget(self.revrightbutton)

        self.leftbutton = Button(text = 'L',font_size=13,on_press=self.leftcallback)
        self.add_widget(self.leftbutton)

        self.revleftbutton = Button(text = 'L\'',font_size=13,on_press=self.revleftcallback)
        self.add_widget(self.revleftbutton)
        

    def frontcallback(self,instance):
        self.cube.clear_widgets()
        for i in range(6,9):
            temp = self.cube.Y[i]
            temp2 = self.cube.O[i]
            temp3 = self.cube.W[i]
            self.cube.Y[i] = self.cube.R[i]
            self.cube.O[i] = temp
            self.cube.W[i] = temp2
            self.cube.R[i] = temp3

        self.cube.reupdate()


    def revfrontcallback(self,instance):
        self.cube.clear_widgets()
        for i in range(6,9):
            temp = self.cube.Y[i]
            temp2 = self.cube.O[i]
            temp3 = self.cube.W[i]
            self.cube.W[i] = self.cube.R[i]
            self.cube.O[i] = temp3
            self.cube.Y[i] = temp2
            self.cube.R[i] = temp
        self.clockwise([6,7,8,3,4,5,0,1,2],4)
        self.cube.reupdate()
    def bottomcallback(self,instance):
        pass
    def revbottomcallback(self,instance):
        print("revback")
    def rightcallback(self,instance):
        print('right')
    def revrightcallback(self,instance):
        print('revright')
    def leftcallback(self,instance):
        print('right')
    def revleftcallback(self,instance):
        print('revright')
    def clockwise(self,config,facenum):  
        
        temp = self.cube.faces[facenum][config[1]]
        temp2 = self.cube.faces[facenum][config[5]]
        temp3 = self.cube.faces[facenum][config[7]]
        # rotate inner ring clockwise
        self.cube.faces[facenum][config[1]] =  self.cube.faces[facenum][config[3]]
        self.cube.faces[facenum][config[5]] = temp
        self.cube.faces[facenum][config[7]] = temp2
        self.cube.faces[facenum][config[3]] = temp3

        temp = self.cube.faces[facenum][config[2]]
        temp2 = self.cube.faces[facenum][config[6]]
        temp3 = self.cube.faces[facenum][config[8]]
        self.cube.faces[facenum][config[2]] =  self.cube.faces[facenum][config[0]]
        self.cube.faces[facenum][config[8]] = temp
        self.cube.faces[facenum][config[6]] = temp3
        self.cube.faces[facenum][config[0]] = temp2
        
        #rotate outer ring clockwise
    def cclockwise(self,config,facenum):
        temp = self.cube.faces[facenum][config[1]]
        temp2 = self.cube.faces[facenum][config[5]]
        temp3 = self.cube.faces[facenum][config[7]] 
        # rotate inner ring counterclockwise
        self.cube.faces[facenum][config[1]] =  self.cube.faces[facenum][config[3]]
        self.cube.faces[facenum][config[5]] = temp
        self.cube.faces[facenum][config[7]] = temp2
        self.cube.faces[facenum][config[3]] = temp3

        temp = self.cube.faces[facenum][config[2]]
        temp2 = self.cube.faces[facenum][config[6]]
        temp3 = self.cube.faces[facenum][config[8]]
        self.cube.faces[facenum][config[2]] =  self.cube.faces[facenum][config[0]]
        self.cube.faces[facenum][config[8]] = temp
        self.cube.faces[facenum][config[6]] = temp3
        self.cube.faces[facenum][config[0]] = temp2
        
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
class cubeface(GridLayout):
    def __init__(self,color,**kwargs):
        super(cubeface,self).__init__(**kwargs)
        self.cols=3
        self.squares = []
        for counter,i in enumerate(color):
            s = square(i,counter)
            self.squares.append(s)  #contains all squares of this particular face
            self.add_widget(s)
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