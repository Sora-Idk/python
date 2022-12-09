import time

import pygame
import pygame as pg

import Settings
from Settings import FPS,PlayerSize,PlayerGravity,JumpSize,RES

clock = pg.time.Clock()

class Bird:
    def __init__(self,game):
        self.last_time = time.time()
        self.dt = 0
        self.Gravity = PlayerGravity
        self.game = game
        self.px = 110
        self.py = 110
        self.vy = 0
        self.inbound =True

    def Jump(self):
        if self.vy<=0 and self.inbound==True:
            self.vy+=JumpSize

    def checks(self):
        if RES(0)-JumpSize > self.py >= PlayerSize:
            self.inbound = True
        else:
            self.inbound = False
    def update(self):
        self.dt = time.time()-self.last_time
        self.dt*=FPS
        self.last_time = time.time()

        self.py+=(self.Gravity-self.vy)*self.dt
        if self.vy>0:
            print(self.vy)
            self.vy-=(self.Gravity/2)*self.dt
            print(self.vy)

    def draw(self):
        self.update()
        pg.draw.rect(self.game.screen,(255,0,0),pg.Rect(self.px,self.py,PlayerSize,PlayerSize),2)