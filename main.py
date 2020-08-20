import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from cubeface import cubeface
from buttonpanel import buttonpanel
from kivy.clock import Clock
import os
import neat
import time,math
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
        self.trainer = None
        self.reupdate()
    def reupdate(self,*args):  # function that redraws the cube
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
        self.bp = buttonpanel(self)
        self.add_widget(self.bp) #place holder
        self.add_widget(Label(text='')) #place holder
    def getfaces(self):
        return self.faces
# class traincube(GridLayout):
#     def __init__(self,**kwargs):
#         super(traincube,self).__init__(**kwargs)
#         self.rows = 2
#         self.cubes = list()
#         for i in range(4):
#             c = cube()
#             c.trainer = self
#             self.cubes.append(c)
#             self.add_widget(c)
#         self.solvemove = None
#     def terminate(self):
#         self.solvemove.cancel()
#     def eval_genomes(self,genomes,config):
#         self.ges = []  # genomes and corresponding networks stored in list
#         self.networks = []
#         self.genomelength = len(genomes)
#         for genome_id, genome in genomes:
#             network = neat.nn.feed_forward.FeedForwardNetwork.create(genome,config)
#             genome.fitness = 0 # initize all genome to have 0 fitness
#             self.ges.append(genome)
#             self.networks.append(network)
#         self.solvemove = Clock.schedule_interval(lambda dt: self.evolve_all(),0) #every clock cycle update all cubes
#     def evolve_all(self):
#         #for i,cube in enumerate(self.cubes):
#             i = 0
#             self.cubes[i].bp.evolvegenome(self.ges[i],self.networks[i])
#     def run(self,config_file):
#         configs = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
#                          neat.DefaultSpeciesSet, neat.DefaultStagnation,
#                          config_file)

#         p = neat.Population(configs)

#         p.add_reporter(neat.StdOutReporter(True))
#         stats = neat.StatisticsReporter()
#         p.add_reporter(stats)
#         # select the most fit neural network after n generations
#         winner = p.run(self.eval_genomes, 3)
#         # print('\nBest genome:\n{!s}'.format(winner))

#     def solve(self):
#         local_dir = os.path.dirname(__file__)
#         config_path = os.path.join(local_dir, 'config-feedforward.txt')
#         self.run(config_path)
        
       

class CubeApp(App):
    def build(self): 
        return cube()


if __name__ == '__main__':
    CubeApp().run()