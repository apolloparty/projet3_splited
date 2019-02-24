import random
from itertools import chain
import pygame
from pygame.locals import *
import Class.Character as Ch
import Class.Collect as Co
import Class.Items as It
import Class.Labyrinth as La
import Class.Motion as Mo
import Class.Pygame as Ga
import Class.User as Us

def main():
    #define collect init, load ressources classes and struct the program
    collect = [0, 0, 0]
    maps = La.Labyrinth().open_map()
    space_list, wall_list, tina_position = La.Labyrinth().register_fixed(maps)
    item_list, maps = It.Items().items_position(space_list, maps)
    window, space = Ga.Pygame().unmovable(wall_list, space_list)
    Ga.Pygame().movable(window, item_list, tina_position)
    for line in maps:
        print(line)
    while 1:
        mcgyver_position, mcx, mcy = Ch.Character().mcgyver(maps)
        Co.Collect().check_win(mcgyver_position, tina_position, window)
        Ga.Pygame().display_mac(window, mcgyver_position, space)
        move = Us.User().entry_raw()
        collect = Co.Collect().check_items(item_list, mcgyver_position, collect)
        Mo.Motion().check_direction(move, mcy, mcx, maps, collect)

main()