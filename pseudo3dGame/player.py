import pygame as pg
from settings import vel, player_size, FPS

clock = pg.time.Clock()
Dt= clock.tick(FPS)/1000

class player():
    def __init__(self,game):
        self.game = game
        self.px = 100
        self.py = 200
        self.vx = 0
        self.vy = 0
        self.aim = 0

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

    def movement(self):
        keys = pg.key.get_pressed()
        self.vx += (keys[pg.K_d] - keys[pg.K_a]) * vel  * Dt
        self.vy += (keys[pg.K_s] - keys[pg.K_w]) * vel  * Dt
        print(self.vy,self.vx)
        self.draw()

    def collisionDetection(self):
        pass

    def draw(self):
        print(self.vy,self.vx)
        pg.draw.circle(self.game.screen,'white',(self.px+self.vx,self.py+self.vy),player_size)