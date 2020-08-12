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
        # rotate outer ring clockwise
        temp = self.cube.faces[facenum][config[2]]
        temp2 = self.cube.faces[facenum][config[6]]
        temp3 = self.cube.faces[facenum][config[8]]
        self.cube.faces[facenum][config[2]] =  self.cube.faces[facenum][config[0]]
        self.cube.faces[facenum][config[8]] = temp
        self.cube.faces[facenum][config[6]] = temp3
        self.cube.faces[facenum][config[0]] = temp2
        
    def cclockwise(self,config,facenum):
        temp = self.cube.faces[facenum][config[3]]
        temp2 = self.cube.faces[facenum][config[5]]
        temp3 = self.cube.faces[facenum][config[7]] 
        # rotate inner ring counterclockwise
        self.cube.faces[facenum][config[3]] =  self.cube.faces[facenum][config[1]]
        self.cube.faces[facenum][config[5]] = temp3
        self.cube.faces[facenum][config[7]] = temp
        self.cube.faces[facenum][config[1]] = temp2
        # rotate outer ring counterclockwise
        temp = self.cube.faces[facenum][config[0]]
        temp2 = self.cube.faces[facenum][config[6]]
        temp3 = self.cube.faces[facenum][config[8]]
        self.cube.faces[facenum][config[0]] =  self.cube.faces[facenum][config[2]]
        self.cube.faces[facenum][config[8]] = temp2
        self.cube.faces[facenum][config[6]] = temp
        self.cube.faces[facenum][config[2]] = temp3