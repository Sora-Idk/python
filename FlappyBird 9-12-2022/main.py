import sys
import pygame as pg
from Settings import *
from Bird import *


class Game:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode(RES)
        self.newgame()

    def newgame(self):
        self.Bird = Bird(self)

    def update(self):
        pg.display.flip()
        self.clock.tick(FPS)
        pg.display.set_caption(str(int(self.clock.get_fps())))

    def draw(self):
        self.screen.fill((100,100,100))
        self.Bird.draw()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.Bird.Jump()

    def run(self):
        while True:
            self.update()
            self.check_events()
            self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()