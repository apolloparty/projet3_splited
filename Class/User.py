import pygame
from pygame.locals import *

class User:

    def entry_user(self):
        move = input("Entrez ZQSD pour vous déplacer : ")
        return move

    def entry_raw(self):
        pygame.init()
        move = ""
        passing = 1
        while passing == 1:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_s:
                        move = "s"
                    if event.key == K_z:
                        move = "z"
                    if event.key == K_d:
                        move = "d"
                    if event.key == K_q:
                        move = "q"
                    return move
                if event.type == QUIT:
                    quit()