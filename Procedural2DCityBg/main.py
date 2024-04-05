import random
import time
import pygame as pg
import numpy as np

pg.init()

#bg Variables
Running = True
_res = np.array([1080,720])
window = pg.display.set_mode(_res,pg.RESIZABLE)
layers_to_blit = []
__frame = 0

#%ages
#def bg0
bg0_c1 = 80
bg0_c2 = 50
bg0_c3 = 30
bg0_c4 = 10
bg0_yaxis_offset = 160
#def bg1
bg1_road_height = 80
#def cloud
cloud_height_start = 5
cloud_height_end = 30

#speeds
lightpost_speed = 15

#colors
colors = {
    "w":(255, 255, 255),
    "k":(0, 0, 0),
    "o0":(252, 170, 146),
    "o1":(255, 147, 115),
    "o2":(255, 131, 94),
    "o3":(255, 108, 64),
    "o4":(252, 65, 3)
}

#keybinds
k_quit = pg.K_ESCAPE

def keypress_handler(key):
    if key == k_quit:
        pg.quit()
        Running = False

#def bg layer 0 circle things
def bg0():
    #get the current window size
    _res = np.array([window.get_width(),window.get_height()])

    canvas = pg.Surface(_res, pg.SRCALPHA)
    canvas.convert_alpha()

    _center = _res/2
    _center[1] *= bg0_yaxis_offset/100

    _radius = np.sum(_center)
    pg.Surface.fill(canvas, colors["o0"])
    # 80%, 50%, 30% 10%
    pg.draw.circle(canvas,colors["o1"], _center, int(_radius*bg0_c1/100))
    pg.draw.circle(canvas,colors["o2"], _center, int(_radius*bg0_c2/100))
    pg.draw.circle(canvas,colors["o3"], _center, int(_radius*bg0_c3/100))
    pg.draw.circle(canvas,colors["o4"], _center, int(_radius*bg0_c4/100))
    return canvas

#def bg layer 1 the roads
def bg1():
    #get the current window size
    _res = np.array([window.get_width(),window.get_height()])

    canvas = pg.Surface(_res, pg.SRCALPHA)
    canvas.convert_alpha()

    #top height of road = height of window-20%height of window
    _height = _res[1]*bg1_road_height/100

    pg.draw.rect(canvas, colors["k"],pg.Rect(0,_height,_res[0],_height))
    return canvas

#def clouds
def clouds():
    #get the current window size
    _res = np.array([window.get_width(),window.get_height()])

    canvas = pg.Surface(_res, pg.SRCALPHA)
    canvas.convert_alpha()

    # select random value between 5% from top to 30% from top
    height = random.randint((int(_res[1]*cloud_height_start/100)), int(_res[1]*cloud_height_end/100))

    pg.draw.rect(canvas, (255,0,0), pg.Rect(_res[0]*80/100,height,(_res[0]*2)*3/100,_res[1]*3/100))

    return canvas

def lightposts():
    #get the current window size
    _res = np.array([window.get_width(),window.get_height()])

    canvas = pg.Surface(_res, pg.SRCALPHA)
    canvas.convert_alpha()

    #base, 95%right, 97%up from roadheight
    base = pg.Rect(_res[0]*95/100,(_res[1]*bg1_road_height/100)*97/100,_res[0]*5/100,_res[1]*5/100)
    #rod1, 96.5%right, 90%up from roadheight,2%thickness
    rod1 = pg.Rect(_res[0]*96.5/100,(_res[1]*bg1_road_height/100)*90/100,_res[0]*2/100,_res[1]*10/100)
    #rod1, 97.5%right, 90%up from roadheight
    rod2 = pg.Rect(_res[0]*97/100,(_res[1]*bg1_road_height/100)*60/100,_res[0]*1/100,_res[1]*40/100)

    #drawing base
    pg.draw.rect(canvas, colors["k"], base)
    pg.draw.rect(canvas,colors["k"], rod1)
    pg.draw.rect(canvas,colors["k"], rod2)
    return canvas


def get_static():
    layers_to_blit.clear()
    layers_to_blit.append(bg0())
    layers_to_blit.append(bg1())


def draw():
    get_static()
    for each_layer in layers_to_blit:
        pg.Surface.blit(window,each_layer,(0,0))

    pg.display.flip()

def display_color():
    for key in colors.keys():
        pg.display.set_caption(key)
        pg.Surface.fill(window, colors[key])
        pg.display.flip()
        time.sleep(0.5)

while Running:
    draw()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            Running = False
        if event.type == pg.KEYDOWN:
            keypress_handler(event.key)
    pg.time.Clock().tick(60)
    print(pg.time.get_ticks()/60)


