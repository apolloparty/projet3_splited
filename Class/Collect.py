import random
from itertools import chain
import pygame
from pygame.locals import *

class Collect:

    def check_items(self, item_list, mcgyver_position, collect):
        #update which items are collected into collect list
        if mcgyver_position == item_list[0]:
            collect[0] = 1
        if mcgyver_position == item_list[1]:
            collect[1] = 1
        if mcgyver_position == item_list[2]:
            collect[2] = 1
        print(collect)

        return collect

    def check_win(self, mcgyver_position, tina_position, window, collect):
        #check if the user has win or not, permit to quit the game in case of win or lose
        winning = pygame.image.load("ressource/Victoire.png").convert()
        victory = winning.get_rect()
        losing = pygame.image.load("ressource/Défaite.png").convert()
        lose = losing.get_rect()

        if tuple(mcgyver_position) == tuple(tina_position[1]) and collect != [1, 1, 1]:
            print("YOU LOSE")
            while 1:
                for event in pygame.event.get():
                    window.blit(losing, (0, 0))
                    pygame.display.flip()
                    if event.type == KEYDOWN:
                        if event.key == K_q:
                            quit()
                    if event.type == QUIT:
                        quit()
        if tuple(mcgyver_position) == tuple(tina_position[0]):
            print("YOU WON")
            while 1:
                for event in pygame.event.get():
                    window.blit(winning, (0, 0))
                    pygame.display.flip()
                    if event.type == KEYDOWN:
                        if event.key == K_q:
                            quit()
                    if event.type == QUIT:
                        quit()
