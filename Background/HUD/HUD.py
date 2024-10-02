

import pygame
from Settings.SETTINGS import *
from Background.HUD.HealthBar import HealthBar


class HUD(pygame.sprite.Sprite):
    def __init__(self, HUDtype = 'GAS/HUD/HUD.png'):
        super(HUD, self).__init__()

        self.image = pygame.image.load(HUDtype).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*120, self.image.get_height()*10))
        self.rect = self.image.get_rect()
        self.rect.y = settings.height - self.rect.height
        self.vel_x = 0 
        self.vel_y = 0
        self.health_bar = HealthBar()
        self.health_bar.rect.x = 10
        self.health_bar.rect.y = settings.height - self.health_bar.rect.y - 45

        self.health_bar_gp = pygame.sprite.Group()
        self.health_bar_gp.add(self.health_bar)



    def update(self):
        self.health_bar_gp.update()

        self.rect.x += self.vel_x
        self.rect.y += self.vel_y