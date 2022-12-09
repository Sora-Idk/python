import pygame as pg

from Settings import PipeSpeed,RES,level

class Pipes:
    def __init__(self):
        self.vx = PipeSpeed
        self.px = RES[0]#+pipe width take from the fkin texture
        self.py_top = 20#randomize every pipe barely enough to keep bird go through
        self.py_bottom = RES[1]
        self.level = level
        self.pipeCount = 0

    def generate_pipe(self):
        if self.pipeCount<2*self.level:
            

    def update(self):
        self.px-=self.vx


