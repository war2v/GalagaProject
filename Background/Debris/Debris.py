import pygame
import random




class Debris(pygame.sprite.Sprite):
    def __init__(self, color):
        super(Debris, self).__init__()
        self.width = random.randrange(1, 3)
        self.height = random.randrange(2, 5)
        self.size = (self.width, self.height)
        self.image = pygame.Surface(self.size)
        if color == 1:
            self.color = (random.randrange(0,255), 0, 0)
        elif color == 2:
            self.color = (255, 165, 0)
        elif color == 3:
            self.color = (220,220,220)
        else:
            self.color = (255, 255, 255)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.death_timer = 45
        self.vel_x = random.randrange(-1, 2)
        self.vel_y = random.randrange(-2, 1)
        while self.vel_x == self.vel_y:
            self.vel_x = random.randrange(-2, 1)
            self.vel_y = random.randrange(-1, 4)

    
    def update(self):

        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        
        if self.death_timer == 0:
            self.kill()
        else:
            self.death_timer -= 1
