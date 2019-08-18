from collections import defaultdict
from copy import copy

import numpy as np
import pygame
import pygame.display
import pygame.gfxdraw
from numpy import pi
from numpy.ma import cos, sin
from pygame.color import THECOLORS
from pygame.locals import *


class fill_circle(pygame.sprite.Sprite):
    def __init__(self, surface, color, pos, pressed=0):
        super().__init__()
        self.surface = surface
        self.color = color
        self.rect = pygame.Rect(pos[0] - r, pos[1] - r, 2 * r, 2 * r)

    def _walk(self):
        self.rect.move_ip(3, 3)

    def update(self):
        pygame.gfxdraw.filled_circle(self.surface, self.rect.centerx,
                                     self.rect.centery, r,
                                     THECOLORS['{}'.format(self.color)])


class line_circle(pygame.sprite.Sprite):
    def __init__(self, surface, color, pos):
        super().__init__()
        self.surface = surface
        self.color = color
        self.pos = pos
        self.rect = pygame.gfxdraw.circle(self.surface, pos[0], pos[1], r,
                                          THECOLORS['{}'.format(color)])


class x_y():
    def __init__(self, surface):
        self.surface = surface
        self.s_x, self.s_y = surface.get_size()
        self.xs = list()
        self.ys = list()
        self.points = dict()
        self.gen_xy()

    def gen_xy(self):
        for i in range(-7, 8):
            y_min = -abs(abs(i) - 7) * cos(pi / 3)
            y_max = abs(abs(i) - 7) * cos(pi / 3)
            for j in np.linspace(y_min, y_max, abs(abs(i) - 7) + 1):
                self.xs.append(int(self.s_x / 2 + i * scale))
                self.ys.append(int(self.s_y / 2 + j * scale))
                self.points[int(self.s_x / 2 + i * scale)] = int(self.s_y / 2 +
                                                                 j * scale)
        return


class checkerboard(pygame.sprite.Sprite):
    def __init__(self, surface):
        super().__init__()
        self.surface = surface
        self.s_x, self.s_y = surface.get_size()
        self.x = x_y(surface).xs
        self.y = x_y(surface).ys
        self.points = x_y(surface).points
        self.draw_board()

    def draw_circle(self):
        x = copy(self.x)
        y = copy(self.y)
        for i, j in zip(x, y):
            pygame.draw.circle(self.surface, THECOLORS['white'], [i, j], r, 0)
            pygame.gfxdraw.circle(self.surface, i, j, r, (0, 0, 0))

    def draw_line(self):
        points = copy(self.points)
        x = [i for i in points.keys()]
        y = [i for i in points.values()]
        for i in range(8):
            x1 = x[i]
            x2 = x[i + 7]
            y1 = y[i]
            y2 = self.s_y - y[i + 7]
            pygame.gfxdraw.line(self.surface, x1, y1, x2, y2, (0, 0, 0))
        for i in range(8):
            x1 = x[i]
            x2 = x[i + 7]
            y1 = self.s_y - y[i]
            y2 = y[i + 7]
            pygame.gfxdraw.line(self.surface, x1, y1, x2, y2, (0, 0, 0))
        return 0

    def paint_color(self):
        points = copy(self.points)
        x = [i for i in points.keys()]
        y = [i for i in points.values()]
        x1 = x[0]
        x2 = x[4]
        x3 = x[4]
        y1 = y[0]
        y2 = y[4]
        y3 = self.s_y - y[4]
        pygame.draw.polygon(self.surface, THECOLORS['cyan'],
                            ([x1, y1], [x2, y2], [x3, y3]))
        x1 = self.s_x - x[0]
        x2 = self.s_x - x[4]
        x3 = self.s_x - x[4]
        y1 = y[0]
        y2 = y[4]
        y3 = self.s_y - y[4]
        pygame.draw.polygon(self.surface, THECOLORS['pink'],
                            ([x1, y1], [x2, y2], [x3, y3]))

    def draw_board(self):
        self.paint_color()
        self.draw_line()
        self.draw_circle()


def is_win(color):
    pass


def main():
    global scale, r
    scale = 40
    r = 13
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((1080, 720))
    pygame.display.set_caption('国际跳棋')

    # Create The Backgound
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    # Display The Background
    board = checkerboard(background)
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Prepare Game Objects
    clock = pygame.time.Clock()
    bule_label = [0, 9, 8, 5, 6, 7, 4, 3, 2, 1]
    d = dict()
    for i in range(10):
        d[i] = fill_circle(
            background, 'blue' (x_y(background).xs[i], x_y(background).ys[i]),
            r)

    # Main Loop
    going = True
    count = 0

    while going:

        clock.tick(60)
        count = abs(count) - 1

        # Handle Input Events
        for event in pygame.event.get():
            if event.type == QUIT:
                going = False
            screen.blit(background, (0, 0))
            c.update()

        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()
