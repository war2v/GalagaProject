import pygame
import random
from Settings.SETTINGS import *
from Crafts.Ship_BP import Enemy

class SpawnEnemies:
    def __init__(self):
        self.e_group = pygame.sprite.Group()
        self.timer = random.randrange(30, 120)

    def update(self):
        self.e_group.update()

        if self.e_group.__len__() >= 8:
            if self.timer == 0:
                self.timer = random.randrange(30*3, 120*3)
        elif self.e_group.__len__() < 8:
            if self.timer == 0:
                self.spawn()
                self.timer = random.randrange(30, 120)
        self.timer -= 1


    def spawn(self):
        ship_type = random.randrange(0, 4)
        if ship_type == 1:
            enemy = Enemy(ship_type)
        elif ship_type == 2:
            enemy = Enemy(ship_type)
        elif ship_type == 3:
            enemy = Enemy(ship_type)
        else:
            enemy = Enemy(ship_type)

        self.e_group.add(enemy)