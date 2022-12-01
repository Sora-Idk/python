import pygame as pg
import math
from settings import *
import raytracing

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
        self.pxcur = self.px
        self.pycur = self.py
        self.RayTracedSurface = pg.surface.Surface((SCREEN_WIDTH,SCREEN_HEIGHT))

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
        self.facing = math.radians((self.mousePos[0]-SCREEN_WIDTH/2))
        #this is temp
        self.aimX = self.px + math.cos(self.facing)*aimRaySize
        self.aimY = self.py + math.sin(self.facing)*aimRaySize

        if self.facing>=360 or self.facing<=-360:
            pg.mouse.set_pos(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
            self.facing = 0


    def movement(self):
        self.aim()
        sin_a = math.sin(self.facing)
        cos_a = math.cos(self.facing)
        dx, dy = 0, 0
        speed = vel * Dt
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_s]:
            dx += -speed_cos
            dy += -speed_sin
        if keys[pg.K_a]:
            dx += speed_sin
            dy += -speed_cos
        if keys[pg.K_d]:
            dx += -speed_sin
            dy += speed_cos

        self.px += dx
        self.py += dy
        self.rayTrace()
        self.draw()


    def collisionDetection(self):
        pass

    def rayTrace(self):
        coords = raytracing.rayCoords(self,self.px,self.py)
        coordsX = coords[0]
        coordsY = coords[1]
        pg.Surface.fill(self.RayTracedSurface, 'black')
        for n in range(rayNum+1):
            pg.draw.line(self.RayTracedSurface,'yellow',(self.px,self.py),(coordsX[n],coordsY[n]))

    def draw(self):
        self.mousePos = pg.mouse.get_pos()
        pg.Surface.blit(self.game.screen,self.RayTracedSurface,(0,0))
        pg.draw.circle(self.game.screen,'white',(self.px,self.py),playerSize)
        pg.draw.line(self.game.screen, 'red',(self.px,self.py),(self.aimX,self.aimY))
