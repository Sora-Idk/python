import pygame as pg

pg.init()
colors = {'grid_lines': (246, 244, 235), 'bg': (145, 200, 228), 'human_color': (120, 193, 255), 'dir_pointer': (255, 255, 255)}
window_size = (5, 5)
window_resolution = (500, 500)
cell_size = (int(window_resolution[0]/window_size[0]), int(window_resolution[1]/window_size[1]))
NUM_OF_HUMANS = 4
