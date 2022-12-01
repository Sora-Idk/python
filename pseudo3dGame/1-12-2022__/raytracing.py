from settings import rayNum,SCREEN_WIDTH
import pygame as pg
import math


angle = 360/rayNum

def rayCoords(self,px,py):
    angle = 360 / rayNum
    px = px
    py = py
    coordsX = list()
    coordsY = list()
    for n in range(rayNum+1):
        x = px + math.cos(angle*n)*SCREEN_WIDTH
        y = py + math.sin(angle*n)*SCREEN_WIDTH
        coordsX.append(int(x))
        coordsY.append(int(y))

    if len(coordsY)>=rayNum:
        return(coordsX,coordsY)