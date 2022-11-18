import pygame as pg
import math
from settings import *

clock = pg.time.Clock()
Dt= clock.tick(FPS)/1000

class player():
    def __init__(self,game):
        self.game = game
        self.mousePos = 0
        self.facing = 0
        self.aimX = 0
        self.aimY = 0
        self.px = 100
        self.py = 200

    def key_check(self,Key):
        if Key == 'w':
            self.vy+=vel
        if Key == 'a':
            self.vx-=vel
        if Key == 's':
            self.vy-=vel
        if Key == 'd':
            self.vx+=vel

        self.movement()


    def aim(self):
        self.mousePos = pg.mouse.get_pos()
        self.facing = self.mousePos[0]-SCREEN_WIDTH/2
        self.aimX = self.px + math.cos(math.radians(self.facing))*aimRaySize
        self.aimY = self.py + math.sin(math.radians(self.facing))*aimRaySize

        if self.facing>=360 or self.facing<=-360:
            pg.mouse.set_pos(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
            self.facing = 0


    def movement(self):
        keys = pg.key.get_pressed()
        self.px += (keys[pg.K_d] - keys[pg.K_a]) * vel  * Dt
        self.py += (keys[pg.K_s] - keys[pg.K_w]) * vel  * Dt
        self.aim()
        self.draw()

    def collisionDetection(self):
        pass

    def draw(self):
        self.mousePos = pg.mouse.get_pos()
        pg.draw.circle(self.game.screen,'white',(self.px,self.py),playerSize)
        pg.draw.line(self.game.screen, 'red',(self.px,self.py),(self.aimX,self.aimY))
