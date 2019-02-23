import random
from itertools import chain
import pygame
from pygame.locals import *

class Pygame:

    def unmovable(self, wall_list, space_list):
        i = 0
        j = 0

        pygame.init()
        window = pygame.display.set_mode((480, 480), RESIZABLE)
        wall = pygame.image.load("ressource/mur.png").convert()
        wall.get_rect()
        while i != len(wall_list):
            window.blit(wall, tuple(32*x for x in wall_list[i]))
            i = i + 1
        space = pygame.image.load("ressource/espace.png").convert()
        space.get_rect()
        while j != len(space_list):
            window.blit(space, tuple(32*x for x in space_list[j]))
            j = j + 1
        pygame.display.flip()
        return window, space

    def movable(self, window, item_list, tina_position):
        itemx = pygame.image.load("ressource/item1.png").convert_alpha()
        itemx.get_rect()
        window.blit(itemx, tuple(32*x for x in item_list[0]))
        itemy = pygame.image.load("ressource/item2.png").convert_alpha()
        itemy.get_rect()
        window.blit(itemy, tuple(32*x for x in item_list[1]))
        itemz = pygame.image.load("ressource/item3.png").convert_alpha()
        itemz.get_rect()
        window.blit(itemz, tuple(32*x for x in item_list[2]))
        itemtina = pygame.image.load("ressource/Gardien.png").convert_alpha()
        itemtina.get_rect()
        window.blit(itemtina, tuple(32*x for x in tina_position[0]))
        pygame.display.flip()

    def display_mac(self, window, mcgyver_position, space):
        mac = pygame.image.load("ressource/MacGyver.png").convert()
        mac.get_rect()
        window.blit(mac, tuple(32*x for x in mcgyver_position))
        pygame.display.flip()
        window.blit(space, tuple(32*x for x in mcgyver_position))