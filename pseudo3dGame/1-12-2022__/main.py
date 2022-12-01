import sys
import pygame as pg
from settings import *
from map import *
from player import *

class Game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)
        pg.mouse.set_pos(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.newgame()

    def newgame(self):
        self.map = Map(self)
        self.player = player(self)

    def update(self):
        pg.display.flip()
        self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps():.1f}')

    def draw(self):
        self.player.movement()
        self.screen.fill('black')
        self.map.draw()
        self.player.draw()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

            if event.type == pg.key.get_pressed():
                self.player.key_check(chr(event.key))

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    game = Game()
    game.run()
