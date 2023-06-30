import random

import pygame as pg
from settings import *
import time
pg.init()
pg.font.init()


def start():
    disp = pg.display.set_mode(window_size)
    pg.display.set_caption('Gobble!')
    return disp


def draw_grid(canvas):
    canvas.fill(colors["BG"])
    line_color = colors["lineColor"]
    pg.draw.rect(canvas,line_color,pg.Rect(0,0,game_window_size[0],game_window_size[1]),1)
    for i in range(1,amount_cells):
        pg.draw.line(canvas, line_color, (i*cell_size,0), (i*cell_size,game_window_size[0]+1))
    for j in range(1,amount_cells):
        pg.draw.line(canvas, line_color, (0,j*cell_size), (game_window_size[1]+1,j*cell_size))
    return canvas


def draw_player(canvas,player):
    player_color = colors["playerColor"]
    p1 = pg.rect.Rect(player.posx+1,player.posy+1,cell_size-1,cell_size-1)
    pg.draw.rect(canvas,player_color,p1)
    return canvas


def draw_food(canvas,food):
    food_color = colors["foodColor"]
    f1 = pg.rect.Rect(food.posx*cell_size+1,food.posy*cell_size+1,cell_size-1,cell_size-1)
    pg.draw.rect(canvas,food_color,f1)
    return canvas


def draw_text(text,font,size,transparent):
    text_color = colors['textColor']
    font = pg.font.SysFont(font,size)
    text_plane = font.render(text, True, text_color)

    if not transparent:
        container_width = text_plane.get_width()+(text_padding*2)
        container_height = text_plane.get_height()+(text_padding*2)

        container = pg.Surface((container_width,container_height))
        container.fill(colors["containerColor"])

        container.blit(text_plane,(text_padding,text_padding))

        return container

    return text_plane


def title_screen(running, points = 0):
    screen = pg.display.set_mode(window_size)
    while not running:
        screen.fill(colors["BG"])
        title = draw_text('Gobble', "Ink Free", 80, True)
        screen.blit(title,((window_size[0] / 2) - (title.get_width() / 2), (window_size[1] / 3) - (title.get_height() / 2)))
        text = draw_text('Click in the window to start playing!','Cascadia Code', 32, True)
        screen.blit(text,((window_size[0] / 2) - (text.get_width() / 2), (window_size[1] / 2) - (text.get_height() / 2)))
        prev_score_text = "prev score: " + str(points)
        prev_score = draw_text(prev_score_text, 'Cascadia Code', 32, True)
        screen.blit(prev_score,((window_size[0] / 2) - (prev_score.get_width() / 2), (window_size[1] / 2) + (prev_score.get_height())))
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            if pg.mouse.get_pressed()[0]:
                print('e')
                running = True

    return running


def draw(player, food, start_time):
    t = timer(start_time)[1]
    canvas = pg.Surface(game_window_size)
    points_text = "Points:: " + str(player.points) # this is before player variable o_o
    text = draw_text(points_text, "Cascadia Code", 42, True)
    grid = draw_grid(canvas)
    player = draw_player(canvas,player)
    food = draw_food(canvas, food)
    time_text = draw_text("Time Remaining: ","Cascadia Code", 16, True)
    time = draw_text(str(t),"Cascadia Code", 32, True)


    frame = pg.Surface(window_size)
    frame.fill(colors["BG"])

    # blit stuff on this line
    frame.blit(player, (0, 0))
    frame.blit(food,(0,0))
    frame.blit(grid, (0, 0))
    frame.blit(text, (525,50))
    frame.blit(time_text, (525, 100))
    frame.blit(time,(620,100))


    return frame


def count_point(food, player):
    boolean = False
    if food.posx == player.posx/cell_size and food.posy == player.posy/cell_size:
        boolean = True
    return boolean


def timer(start_time):
    time_left = round(time_limit - abs(start_time-time.time()))
    if time_left < 0:
        return False, time_left
    return True, time_left


def update(running, player, food, start_time):
    pg.display.update()
    running = timer(start_time)[0]
    if count_point(food,player):
        player.points += 1
        food.posx = random.randint(0, amount_cells-1)
        food.posy = random.randint(0, amount_cells-1)
        print("points>>",player.points)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()

        if pg.mouse.get_pressed()[0]:#replace this with button
            running = True
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w and player.posy > 0:
                player.movesmade+=1
                player.posy -= cell_size
            if event.key == pg.K_s and player.posy < game_window_size[1]-cell_size:
                player.posy += cell_size
                player.movesmade += 1
            if event.key == pg.K_a and player.posx > 0:
                player.posx -= cell_size
                player.movesmade += 1
            if event.key == pg.K_d and player.posx < game_window_size[0]-cell_size:
                player.posx += cell_size
                player.movesmade += 1

    return running, player, food


class Player:
    def __init__(self):
        self.posx = 0
        self.posy = 0
        self.points = 0
        self.movesmade = 0


class Food:
    def __init__(self):
        self.posx = random.randint(0,amount_cells-1)
        self.posy = random.randint(0,amount_cells-1)