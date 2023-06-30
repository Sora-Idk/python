import pygame as pg
from funcs import *


running = False
end_screen = False
disp = start()
player = Player()
food = Food()

while True:
    while not running:#title screen
        running = title_screen(running, player.points)
        player = Player()
        food = Food()

    if running:# game
        start_time = time.time()

        while running:
            updates = update(running, player, food, start_time)
            running = updates[0]
            frame = draw(player, food, start_time)

            if running:
                disp.blit(frame, (0,0))

