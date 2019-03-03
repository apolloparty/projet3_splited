import random
from itertools import chain
import pygame
from pygame.locals import *


class Character:

    def mcgyver(self, maps):

        """Give mcgyver position as coordinates usable for others objects"""
        mcgyver_position = []
        mcx = 0
        mcy = 0
        x = 0
        y = 0
        continuer = 1

        while continuer == 1:
            if maps[y][x] != "M":
                if y == 14 and x == 14:
                    break
                if x == 14:
                    x = 0
                    y = y + 1
                else:
                    x = x + 1
            if maps[y][x] == "M":
                mcx = x
                mcy = y
                mcgyver_position.insert(0, ((mcx, mcy)))
                continuer = 0
        mcgyver_position = mcgyver_position[0]
        print(mcgyver_position)
        return mcgyver_position, mcx, mcy
