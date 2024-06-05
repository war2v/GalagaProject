import sys
sys.path.append('/Users/xthev/OneDrive/Documents/ProgrammingProjects/PythonProjects/GalagaProject/Settings')
from GAS import HUD
import pygame
from Settings import SETTINGS


class HealthBar(pygame.sprite.Sprite):
    def __init__(self):
        super(HealthBar, self).__init__()
        
         
        self.image = pygame.image.load('GAS/HUD/hb.png').convert()
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*3, self.image.get_height()*3))
        self.rect = self.image.get_rect()
             
        self.vel_x = 0
        self.vel_y = 0

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y