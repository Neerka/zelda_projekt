import pygame

TILESIZE = 64
win_width = 1280
win_height = 780
win = pygame.display.set_mode((win_width, win_height))


o = pygame.image.load("obstacle.png")
v = pygame.image.load("visible.png")


map = [
[o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o],
[o,v,v,v,v,v,v,v,v,v,v,v,v,v,v,v,v,v,v,o],
[o,v,v,v,v,v,v,v,v,v,v,v,v,v,v,v,v,v,v,o],
[o,v,v,v,v,v,v,v,o,o,o,o,v,v,v,v,v,v,v,o],
[o,v,v,v,v,v,v,v,o,o,o,o,v,v,v,v,v,v,v,o],
[o,v,v,v,v,v,v,v,v,o,o,v,v,v,v,v,v,v,v,o],
[o,v,v,v,v,v,v,v,v,o,o,v,v,v,v,v,v,v,v,o],
[o,v,v,v,v,v,v,v,o,o,o,o,v,v,v,v,v,v,v,o],
[o,v,v,v,v,v,v,v,o,o,o,o,v,v,v,v,v,v,v,o],
[o,v,v,v,v,v,v,v,v,v,v,v,v,v,v,v,v,v,v,o],
[o,v,v,v,v,v,v,v,v,v,v,v,v,v,v,v,v,v,v,o],
[o,v,v,v,v,v,v,v,v,v,v,v,v,v,v,v,v,v,v,o],
[o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o]
]



class Level:
    def __init__(self, map):
        self.map = map
        self.map_width = 20
        self.map_height = 13
        self.TILESIZE = 64
    def draw_game(self):
        """ta funkcja w teorii ma rysowac cala mape"""
        for row in range(self.map_height):
            for column in range(self.map_width):
                win.blit(self.map[row][column], (column*self.TILESIZE, row*self.TILESIZE))

