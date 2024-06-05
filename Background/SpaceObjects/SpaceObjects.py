import pygame
import random
import sys
sys.path.append('/Users/xthev/OneDrive/Documents/ProgrammingProjects/PythonProjects/GalagaProject/Settings')
from SETTINGS import *



class Star(pygame.sprite.Sprite):
    def __init__(self, size = 0):
        super(Star, self).__init__()
        self.width = random.randrange(1,5)
        if size == 0:
            self.height = self.width
            self.size = (self.height, self.width)
        else: 
            self.size = size
        self.image = pygame.Surface(self.size)
        c_start = 245
        c_finish = 255
        speed = random.randrange(1, 2)
        N = random.randrange(0, 255)
        if N < 155:
            R = 0
            G = 0
            B = random.randrange(c_start, c_finish)
        else:
            if N < 230:
                R = 255
                G = 255
                B = 255
            elif N < 250:
                R = random.randrange(c_start, c_finish)
                G = 0
                B = 0
            else:
                R = 0
                G = random.randrange(c_start, c_finish)
                B = 0


        
        self.color = (R, G, B)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, settings.width)
        self.rect.y = 0
        self.vel_x = 0
        self.vel_y = random.randrange(4, 25)
    
    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

