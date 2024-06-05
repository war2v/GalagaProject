import pygame
import random
import sys
sys.path.append('/Users/xthev/OneDrive/Documents/ProgrammingProjects/PythonProjects/GalagaProject/Background/Debris')
import Debris

class SpawnDebris:
    def __init__(self):
        self.debris_gp = pygame.sprite.Group()
    
    def update(self):
        
        self.debris_gp.update()

    def spawn_debris(self, pos):
        random_number = random.randrange(2, 4)
        
        for debris in range(random_number):
            color_num = random.randrange(0, 4)
            more_debris = Debris.Debris(color_num)
            more_debris.rect.x = pos[0]
            more_debris.rect.y = pos[1]
            self.debris_gp.add(more_debris)