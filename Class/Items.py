import random
from itertools import chain
import pygame
from pygame.locals import *

class Items:

    def items_position(self, space_list, maps):
        item_list = []

        space_rand = random.randint(0, len(space_list) - 1)
        item_list.append(space_list[space_rand])
        space_rand = random.randint(0, len(space_list) - 1)
        item_list.append(space_list[space_rand])
        space_rand = random.randint(0, len(space_list) - 1)
        item_list.append(space_list[space_rand])
        item_coord = list(chain.from_iterable(item_list))
        list1, list2 = zip(*item_list)
        maps[list2[0]][list1[0]] = "X"
        maps[list2[1]][list1[1]] = "Y"
        maps[list2[2]][list1[2]] = "Z"
        item_coord = item_list[1]

        return item_list, maps