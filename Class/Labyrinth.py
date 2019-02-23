import random
from itertools import chain
import pygame
from pygame.locals import *

class Labyrinth:

    def open_map(self):
        maps = []
        x = 0
        y = 1
        with open("ressource/maplabyrinthe.txt") as file:
            for line in file:
                map_line = []
                for char in line:
                    if char != "\n":
                        map_line.append(char)
                        x = x + 1
                    else:
                        y = y + 1
                maps.append(map_line)
        #for line in maps:
           #print(line)
        return maps

    def register_fixed(self, maps):
        space_list = []
        wall_list = []
        tina_position = []
        continuer = 1
        x = 0
        y = 0

        while continuer == 1:
            if maps[y][x] == " ":
                if x == 14 and x != 0 and y != 14:
                    space_list.append((x, y))
                    y = y + 1
                    x = 0
                if maps[y][x] == " ":
                    space_list.append((x, y))
                if maps[y][x] == "#":
                    wall_list.append((x, y))
                x = x + 1
            if maps[y][x] == "#":
                if x == 14 and x != 0 and y != 14:
                    wall_list.append((x, y))
                    y = y + 1
                    x = 0
                if maps[y][x] == "#":
                    wall_list.append((x, y))
                if maps[y][x] == " ":
                    space_list.append((x, y))
                x = x + 1
            if maps[y][x] == "T":
                tina_position.append((x, y))
                x = x + 1
            if maps[y][x] == "M":
                x = x + 1
            if y == 14 and x == 14:
                wall_list.append((x, y))
                continuer = 0
        return space_list, wall_list, tina_position