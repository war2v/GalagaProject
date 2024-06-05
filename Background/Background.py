

import pygame
from Background.SpaceObjects.SpaceObjects import Star
from random import *
from Background.HUD import HUD
from Settings.SETTINGS import *


class Background(pygame.sprite.Sprite):
    def __init__(self):
        super(Background, self).__init__()
        self.image = pygame.Surface(settings.size)
        self.HUD = HUD.HUD()
        self.color = (0, 0, 15)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.stars = pygame.sprite.Group()
        self.timer = randrange(2, 13)
        
        # Main Music
        pygame.mixer.music.load('GAS/Sounds/music/halo.ogg')
        pygame.mixer.music.set_volume(.5)
        pygame.mixer.music.play(loops=True)

    
    def update(self):
        self.HUD.update()
        self.stars.update()
        for star in self.stars:
            if star.rect.y >= settings.height:
                self.stars.remove(star)
        if self.timer == 0:
            new_star = Star()
            self.stars.add(new_star)
            self.timer = randrange(2, 13)
        
    
        self.image.fill(self.color)
        self.stars.draw(self.image)
        self.timer -= 1
        pass