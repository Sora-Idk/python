import random
from UtilitiesAndVArs import *
from organisms import *
from tools import *
from materials import *
import pygame as pg


pg.init()
#Variables
clock = pg.time.Clock()
running = True
screen = pg.display.set_mode(window_resolution)
screen.fill(colors['bg'])


def create_human():
    temp = []
    humans_list = []
    for NUMBER_OF_HUMANS_REMAINING in range(NUM_OF_HUMANS):
        posx = random.randint(0, window_size[0] - 1)
        posy = random.randint(0, window_size[1] - 1)
        while (posx, posy) in temp:
            posx = random.randint(0, window_size[0] - 1)
            posy = random.randint(0, window_size[1] - 1)
        if (posx, posy) not in temp:
            humans_list.append(Human(pos_x=posx, pos_y=posy, facing=random.randint(1, 4)))
        temp.append((humans_list[-1].pos_x, humans_list[-1].pos_y))
    return humans_list


#FUNC TO DRAW THE INITIAL GRID ON A CANVAS AND RETURN IT
def draw_grid():
    canvas = pg.Surface(window_resolution, pg.SRCALPHA, 32)
    canvas = canvas.convert_alpha()
    box = pg.Rect(0, 0, canvas.get_width(), canvas.get_height())
    pg.draw.rect(canvas, colors['grid_lines'], box, 1)
    for x in range(window_size[0]+1):
        pg.draw.line(canvas,colors['grid_lines'], (x*cell_size[0], 0), (x*cell_size[0], window_resolution[0]))
        for y in range(window_size[1]+1):
            pg.draw.line(canvas, colors['grid_lines'], (0, y*cell_size[1]), (window_resolution[1], y*cell_size[1]))
    return canvas


def draw_players():
    canvas = pg.Surface(window_resolution, pg.SRCALPHA, 32)
    canvas = canvas.convert_alpha()
    #MAKES PLAYERS
    for x in humans:
        pg.draw.rect(canvas, colors['human_color'], pg.Rect(x.pos_x*cell_size[0], x.pos_y*cell_size[1], cell_size[0], cell_size[1]))

    #SHOWS THEIR DIRECTION
    offset_x = cell_size[0] / 3
    offset_y = cell_size[1] / 3
    for x in humans:
        if x.facing == 1:
            pos = ((x.pos_x*cell_size[0]+cell_size[0]/2), (x.pos_y*cell_size[1]+cell_size[1]/2)-offset_y)
            pg.draw.circle(canvas, colors['dir_pointer'], pos, 5)
        if x.facing == 2:
            pos = ((x.pos_x*cell_size[0]+cell_size[0]/2 + offset_x),(x.pos_y*cell_size[1]+cell_size[1]/2))
            pg.draw.circle(canvas, colors['dir_pointer'], pos, 5)
        if x.facing == 3:
            pos = ((x.pos_x*cell_size[0]+cell_size[0]/2), (x.pos_y*cell_size[1]+cell_size[1]/2) + offset_y)
            pg.draw.circle(canvas, colors['dir_pointer'], pos, 5)
        if x.facing == 4:
            pos = ((x.pos_x*cell_size[0]+cell_size[0]/2) - offset_x, (x.pos_y*cell_size[1]+cell_size[1]/2))
            pg.draw.circle(canvas, colors['dir_pointer'], pos, 5)

    return canvas


def make_frame_for(window_name):
    grid = draw_grid()
    players = draw_players()

    window_name.blit(players, (0, 0))
    window_name.blit(grid, (0, 0))


def human_cords():
    arr_ = []
    for each_human in humans:
        arr_.append((each_human.pos_x,each_human.pos_y))
    return arr_


def make_collision_map(cords):
    map_ = []
    for x in range(window_size[0]):
        for y in range(window_size[1]):
            if (x, y) in cords:
                map_.append(1)
            else:
                map_.append(0)
    return map_


#MAIN LOOP
humans = create_human()
col_map = make_collision_map(human_cords())
for humanNumber in humans:
    print(humanNumber)
print(col_map)
while running:
    make_frame_for(screen)
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()
    clock.tick(30)
