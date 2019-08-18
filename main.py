from collections import defaultdict
from copy import copy

import numpy as np
import pygame
import pygame.display
from numpy import pi
from numpy.ma import cos, sin
from pygame.color import THECOLORS
from pygame.draw import circle, polygon
from pygame.gfxdraw import circle as gcircle
from pygame.gfxdraw import line
from pygame.locals import *


class board_cicle(pygame.sprite.Sprite):
    pass



class 


class checkerboard(pygame.sprite.Sprite):
    def __init__(self, surface):
        super().__init__()
        self.surface = surface
        self.s_x, self.s_y = surface.get_size()
        self.scale = 50
        self.x = list()
        self.y = list()
        self.point = dict()
        self.r = 13
        self.x_y()

    def x_y(self):
        for i in range(-7, 8):
            y_min = -abs(abs(i) - 7) * cos(pi / 3)
            y_max = abs(abs(i) - 7) * cos(pi / 3)
            for j in np.linspace(y_min, y_max, abs(abs(i) - 7) + 1):
                self.x.append(int(self.s_x / 2 + i * self.scale))
                self.y.append(int(self.s_y / 2 + j * self.scale))
                self.point[int(self.s_x / 2 +
                               i * self.scale)] = int(self.s_y / 2 +
                                                      j * self.scale)
        return

    def draw_circle(self):
        x = copy(self.x)
        y = copy(self.y)
        for i, j in zip(x, y):
            circle(self.surface, THECOLORS['white'], [i, j], self.r, 0)
            gcircle(self.surface, i, j, self.r, (0, 0, 0))

    def draw_line(self):
        points = copy(self.point)
        x = [i for i in points.keys()]
        y = [i for i in points.values()]
        for i in range(8):
            x1 = x[i]
            x2 = x[i + 7]
            y1 = y[i]
            y2 = self.s_y - y[i + 7]
            line(self.surface, x1, y1, x2, y2, (0, 0, 0))
        for i in range(8):
            x1 = x[i]
            x2 = x[i + 7]
            y1 = self.s_y - y[i]
            y2 = y[i + 7]
            line(self.surface, x1, y1, x2, y2, (0, 0, 0))

        return 0

    def paint_color(self):
        points = copy(self.point)
        x = [i for i in points.keys()]
        y = [i for i in points.values()]
        x1 = x[0]
        x2 = x[4]
        x3 = x[4]
        y1 = y[0]
        y2 = y[4]
        y3 = self.s_y - y[4]
        polygon(self.surface, THECOLORS['cyan'],
                ([x1, y1], [x2, y2], [x3, y3]))
        x1 = self.s_x - x[0]
        x2 = self.s_x - x[4]
        x3 = self.s_x - x[4]
        y1 = y[0]
        y2 = y[4]
        y3 = self.s_y - y[4]
        polygon(self.surface, THECOLORS['pink'],
                ([x1, y1], [x2, y2], [x3, y3]))

    def draw_board(self):
        self.paint_color()
        self.draw_line()
        self.draw_circle()


class piece(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        pygame.Sprite.__init__(self)
        self.peice_rect = pygame.Rect(x - r, y - r, 2 * r, 2 * r)
        self.original_color = color
        self.color = color

    def update(self, bc=0):
        '''
        bc:button_count -> int
        '''
        if bc == 1:
            self.color = THECOLORS['{}'.format(self.color)]
        if bc == 2:
            self.color = self.original_color

        self.peice_rect.move(x, y)


def is_win(color):
    pass


def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((1080, 720))
    pygame.display.set_caption('Basic Pygame program')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    board = checkerboard(screen)
    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Event loop
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            screen.blit(background, (0, 0))
            board.draw_board()
        pygame.display.flip()


if __name__ == '__main__': main()
