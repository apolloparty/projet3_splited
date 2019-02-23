import random
from itertools import chain
import pygame
from pygame.locals import *

class Collect:

    def check_items(self, item_list, mcgyver_position, collect):
        if mcgyver_position == item_list[0]:
            collect[0] = 1
        if mcgyver_position == item_list[1]:
            collect[1] = 1
        if mcgyver_position == item_list[2]:
            collect[2] = 1
        print(collect)

        return collect

    def check_win(self, mcgyver_position, tina_position, window):
        ending = pygame.image.load("ressource/Victoire.png").convert()
        victory = ending.get_rect()
        if tuple(mcgyver_position) == tuple(tina_position[0]):
            print("YOU WON")
            while 1:
                for event in pygame.event.get():
                    window.blit(ending, (0, 0))
                    pygame.display.flip()
                    if event.type == KEYDOWN:
                        if event.key == K_q:
                            quit()
                    if event.type == QUIT:
                        quit()