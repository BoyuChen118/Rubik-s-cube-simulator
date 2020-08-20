from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
import os
import neat
import time,math
from random import randint
from kivy.clock import Clock
class buttonpanel(GridLayout):  # all ways user can interact with the cube is in the buttonpanel
    def __init__(self,cube,**kwargs):
        super(buttonpanel,self).__init__(**kwargs)
        self.cols = 2
        self.padding = [15,15,15,15]
        self.cube = cube
        self.buttons = []
        self.scrammove= None
        self.count = 0
        self.solvemove = None
        self.frontbutton = Button(text = 'F',font_size=13,on_press=self.frontcallback)
        self.add_widget(self.frontbutton)
        self.buttons.append(self.frontbutton)

        self.revfrontbutton = Button(text = 'F\'',font_size=13,on_press=self.revfrontcallback)
        self.add_widget(self.revfrontbutton)
        self.buttons.append(self.revfrontbutton)

        self.backbutton = Button(text = 'B',font_size=13,on_press=self.backcallback)
        self.add_widget(self.backbutton)
        self.buttons.append(self.backbutton)

        self.revbackbutton = Button(text = 'B\'',font_size=13,on_press=self.revbackcallback)
        self.add_widget(self.revbackbutton)
        self.buttons.append(self.revbackbutton)

        self.rightbutton = Button(text = 'R',font_size=13,on_press=self.rightcallback)
        self.add_widget(self.rightbutton)
        self.buttons.append(self.rightbutton)

        self.revrightbutton = Button(text = 'R\'',font_size=13,on_press=self.revrightcallback)
        self.add_widget(self.revrightbutton)
        self.buttons.append(self.revrightbutton)

        self.leftbutton = Button(text = 'L',font_size=13,on_press=self.leftcallback)
        self.add_widget(self.leftbutton)
        self.buttons.append(self.leftbutton)

        self.revleftbutton = Button(text = 'L\'',font_size=13,on_press=self.revleftcallback)
        self.add_widget(self.revleftbutton)
        self.buttons.append(self.revleftbutton)

        self.upbutton = Button(text = 'U',font_size=13,on_press=self.upcallback)
        self.add_widget(self.upbutton)
        self.buttons.append(self.upbutton)

        self.revupbutton = Button(text = 'U\'',font_size=13,on_press=self.revupcallback)
        self.add_widget(self.revupbutton)
        self.buttons.append(self.revupbutton)

        self.downbutton = Button(text = 'D',font_size=13,on_press=self.downcallback)
        self.add_widget(self.downbutton)
        self.buttons.append(self.downbutton)

        self.revdownbutton = Button(text = 'D\'',font_size=13,on_press=self.revdowncallback)
        self.add_widget(self.revdownbutton)
        self.buttons.append(self.revdownbutton)

        self.solvebutton = Button(text = 'solve',font_size=13,on_press=self.solve)
        self.add_widget(self.solvebutton)

        self.scramblebutton = Button(text = 'scramble',font_size=13,on_press=self.scramble)
        self.add_widget(self.scramblebutton)
        

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
        self.clockwise([6,7,8,3,4,5,0,1,2],4)
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
        self.cclockwise([6,7,8,3,4,5,0,1,2],4)
        self.cube.reupdate()

    def backcallback(self,instance):
        self.cube.clear_widgets()
        for i in range(0,3):
            temp = self.cube.Y[i]
            self.cube.Y[i] = self.cube.O[i]
            self.cube.O[i] = self.cube.W[i]
            self.cube.W[i] = self.cube.R[i]
            self.cube.R[i] = temp
        self.clockwise([2,1,0,5,4,3,8,7,6],5)
        self.cube.reupdate()

    def revbackcallback(self,instance):
       for i in range (0,3):
            self.backbutton.trigger_action(duration = 0.01)

    def rightcallback(self,instance):
        self.cube.clear_widgets()
        nums = [2,5,8]
        y1 = self.cube.Y[0]
        y2 = self.cube.Y[3]
        y3 = self.cube.Y[6]
        for i in nums:
           temp  = self.cube.B[i]
           temp2 = self.cube.W[i]
           temp3 = self.cube.G[i]
           if i == 2:
            self.cube.B[i] = y3 
            self.cube.Y[6] = temp3
           elif i == 5:
            self.cube.B[i] = y2
            self.cube.Y[3] = temp3
           elif i == 8:
            self.cube.B[i] = y1
            self.cube.Y[0] = temp3
           self.cube.W[i] = temp
           self.cube.G[i] = temp2
        self.clockwise([8,5,2,7,4,1,6,3,0],2)
        self.cube.reupdate()
    def revrightcallback(self,instance):
        for i in range (0,3):
            self.rightbutton.trigger_action(duration = 0.01)
    def leftcallback(self,instance):
        self.cube.clear_widgets()
        nums = [0,3,6]
        y2 = self.cube.Y[2]
        y5 = self.cube.Y[5]
        y8 = self.cube.Y[8]
        for i in nums:
           temp  = self.cube.B[i]
           temp2 = self.cube.W[i]
           temp3 = self.cube.G[i]
           if i == 0:
            self.cube.G[i] = y8
            self.cube.Y[8] = temp
           elif i == 3:
            self.cube.G[i] = y5
            self.cube.Y[5] = temp
           elif i == 6:
            self.cube.G[i] = y2
            self.cube.Y[2] = temp
           self.cube.W[i] = temp3
           self.cube.B[i] = temp2
        self.clockwise([0,3,6,1,4,7,2,5,8],3)
        self.cube.reupdate()   
        
    def revleftcallback(self,instance):
        for i in range (0,3):
            self.leftbutton.trigger_action(duration = 0.01)  # reverse = normal * 3
    
    def downcallback(self,instance):
        self.cube.clear_widgets()
        temp = [self.cube.G[0],self.cube.G[1],self.cube.G[2]]
        # indexes of squares on each face to be swapped 
        Gindexes = [0,1,2]  
        Oindexes = [6,3,0]
        Bindexes = [8,7,6]
        Rindexes = [2,5,8]
        for i in range(0,3):
            self.cube.G[Gindexes[i]] = self.cube.R[Rindexes[i]]  
            self.cube.R[Rindexes[i]] = self.cube.B[Bindexes[i]]
            self.cube.B[Bindexes[i]] = self.cube.O[Oindexes[i]]
            self.cube.O[Oindexes[i]] = temp[i]
        self.clockwise([2,1,0,5,4,3,8,7,6],1)
        self.cube.reupdate()   
    def revdowncallback(self,instance):
        for i in range (0,3):
            self.downbutton.trigger_action(duration = 0.01)  # reverse = normal * 3
    def upcallback(self,instance):
        self.cube.clear_widgets()
        temp = [self.cube.G[6],self.cube.G[7],self.cube.G[8]]
        # indexes of squares on each face to be swapped 
        Gindexes = [6,7,8]  
        Oindexes = [8,5,2]
        Bindexes = [2,1,0]
        Rindexes = [0,3,6]
        for i in range(0,3):
            self.cube.G[Gindexes[i]] = self.cube.O[Oindexes[i]] 
            self.cube.O[Oindexes[i]] = self.cube.B[Bindexes[i]]
            self.cube.B[Bindexes[i]] = self.cube.R[Rindexes[i]]
            self.cube.R[Rindexes[i]] = temp[i]
        self.clockwise([2,1,0,5,4,3,8,7,6],0)
        self.cube.reupdate()   
    def revupcallback(self,instance):
        for i in range (0,3):
            self.upbutton.trigger_action(duration = 0.01)  # reverse = normal * 3
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
    def scramble(self,instance): # scrambles the cube
        self.count = 0 # reset scramble count
        nummoves = randint(100,200)  # number of scramble steps
        self.scrammove = Clock.schedule_interval(lambda dt: self.scramblemove(nummoves),0)
    def scramblemove(self,nummoves):
        move = randint(0,8)
        if self.count < nummoves:
            self.buttons[move].trigger_action()
            self.count += 1
        else:
            self.scrammove.cancel()
            self.scrammove = None
    # def firststepdone(self):  # check if the daisy is complete
    #     indexes = [1]
    #     for i in indexes:
    #         if self.cube.faces[0][i] != 'white':
    #             return False
    #     return True
    # def midwhitesquares(self):
    #     indexes = [1,7]  # indexes of all mid squares
    #     observation = []
    #     for faces in self.cube.getfaces():
    #         for i in indexes:
    #             if faces[i] == 'white':
    #                 observation.append(1)  # its 1 if it's a white 
    #             else:
    #                 observation.append(0)  # 0 otherwise
    #     return observation
    # def value(self):  # see how many petal of the daisy is completed
    #     total = 0
    #     indexes = [1,3,5,7]
    #     for i in indexes:
    #         if self.cube.faces[0][i] == 'white':
    #             total += 1
    #     return total
    # def evolvegenome(self,genome,network):
    #     if not self.firststepdone():
    #         observation = self.midwhitesquares()  # observe where all the middle white squares are 
    #         prev_value = self.value()
    #         output = network.activate(observation)
    #         for i in range(0,8):
    #             if output[i] > 0.5:
    #                 self.buttons[i].trigger_action() 
    #                 genome.fitness += 0.1
    #                 now_value = self.value()
    #                 if now_value < prev_value:  # discourage straying away from objective
    #                     genome.fitness -= 30
    #                 elif now_value > prev_value:
    #                     genome.fitness += 1
    #                 elif now_value == prev_value:
    #                     genome.fitness -=0.2
    #     else: 
    #         self.cube.trainer.terminate()

    # def evolve(self,genomes,networks):
        
    #         self.evolvemove = Clock.schedule_interval(lambda dt:self.evolvegenome(genomes[self.count],networks[self.count]),0)
    #         self.count += 1
       
    def eval_genomes(self,genomes,config):
        self.count = 5  # keep tracks of which genome the simulation is on
        ges = []  # genomes and corresponding networks stored in list
        networks = []
        self.genomelength = len(genomes)
        for genome_id, genome in genomes:
            network = neat.nn.feed_forward.FeedForwardNetwork.create(genome,config)
            genome.fitness = 0 # initize all genome to have 0 fitness
            ges.append(genome)
            networks.append(network)
        print(self.genomelength)
        self.solvemove = Clock.schedule_interval(lambda dt: self.evolvegenome(ges[0],networks[0]),0)
            # while not self.firststepdone():   # while daisy is incomplete
            #     output = network.activate(observation)  # output is a list of output node
            #     for i in range(0,8):
            #         if output[i] > 0.5:
            #             self.buttons[i].trigger_action(duration=0.01) 
            #             genome.fitness -= 0.5
            #            # time.sleep(1)
            # genome.fitness += 10
                        
    # def run(self,config_file): # use neat to make a daisy
    #     configs = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
    #                      neat.DefaultSpeciesSet, neat.DefaultStagnation,
    #                      config_file)

    #     p = neat.Population(configs)

    #     p.add_reporter(neat.StdOutReporter(True))
    #     stats = neat.StatisticsReporter()
    #     p.add_reporter(stats)
    #     # select the most fit neural network after 50 generations
    #     winner = p.run(self.eval_genomes, 3)


    def solve(self,instance):  
        self.cube.trainer.solve()
        # local_dir = os.path.dirname(__file__)
        # config_path = os.path.join(local_dir, 'config-feedforward.txt')
        # self.run(config_path)