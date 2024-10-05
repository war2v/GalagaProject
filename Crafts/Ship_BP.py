

from Crafts.CraftTypes import CraftType   

import pygame
from Settings.SETTINGS import *
import random
from Background.HUD import HUD




class Ship_BP(pygame.sprite.Sprite):
    def __init__(self, craft_type = 0):
        super(Ship_BP, self).__init__()

        self.craft_type = craft_type
        self.image = pygame.image.load(CraftType.craft[self.craft_type]).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*3, self.image.get_height()*3))
        self.MACShot_Sound = pygame.mixer.Sound('GAS/Sounds/shot.ogg')
        self.MACShot_Sound.set_volume(0.2)


        self.MachineGunShot_Sound = pygame.mixer.Sound('GAS\Sounds\MachineGun.ogg')
        self.MachineGunShot_Sound.set_volume(0.3)
        self.gun_channel = pygame.mixer.Channel(1)
        self.hit_channel = pygame.mixer.Channel(2)
        self.hit_snd = pygame.mixer.Sound('GAS/Sounds/explosion.ogg')
    
        
        
        
        #gets all rectangular properties of the loaded image.
        #This is how pygame knows how move an object on the screen
        # x coordinate = self.rect.x
        # y coordinate = self.rect.y
    

        self.rect   = self.image.get_rect()
        self.rect.x = settings.width // 2.1
        self.rect.y = self.rect.height-0.5
        self.angle = 0
        
        self.MG_firing = False
        self.MG_fire_rate = 1
        self.MG_timer = 0

        self.MACRounds = pygame.sprite.Group()
        self.Bullets = pygame.sprite.Group()
        self.spawntime = 3
        self.destroyed = False
        self.hp = 5
        self.weapon_choice = 0
        self.bpm = 30
        self.lives = 3
        self.vel_x  = 0
        self.vel_y  = 0
        self.speed  = 5


    def update(self):
        self.MACRounds.update()
        self.Bullets.update()

        if self.MG_firing == True:
            if self.MG_timer == 0:
                self.fire()
                self.MG_firing = self.MG_fire_rate
            self.MG_timer -= 1
        else:
            self.MG_timer = self.MG_fire_rate


        for MAC in self.MACRounds:
            if MAC.rect.y <= 0:
                self.MACRounds.remove(MAC)
        
        for bullet in self.Bullets:
            if bullet.rect.y <= 0:
                self.Bullets.remove(bullet)

        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        
        #This Code Makes sure the ship cannot go out of the window
        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.x >= settings.width - self.rect.width:
            self.rect.x = settings.width - self.rect.width

        if self.rect.y <= 0:
            self.rect.y = 0
        elif self.rect.y >= settings.height - (self.rect.height * 2)-15:
            self.rect.y = settings.height - (self.rect.height * 2)-15

        

    def change_craft_type(self, craft_type):
        match(craft_type):
            case 0:
                self.craft_type = 0
            case 1:
                self.craft_type = 1
            case 2:
                self.craft_type = 2
            case 3:
                self.craft_type = 3
            
        self.image = pygame.image.load(CraftType.craft[self.craft_type]).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*3, self.image.get_height()*3))

    def fireMAC(self):

    
        if self.MACRounds.__len__() >= 2:
                pass
        else:
            if self.gun_channel.get_busy() == True:
                self.gun_channel.stop()
                self.gun_channel.play(self.MACShot_Sound)
            else:
                self.gun_channel.play(self.MACShot_Sound)
            new_MAC = MAC()
            
            new_MAC.rect.x = self.rect.x + (self.rect.width // 2.2)
            new_MAC.rect.y = self.rect.y - 5
            MACRound = new_MAC
            self.MACRounds.add(MACRound)     
            
                
    

    def fireBullet(self):
        if self.Bullets.__len__() >= 3:
            pass
        else:
            if self.gun_channel.get_busy() == True:
                self.gun_channel.stop()
                self.gun_channel.play(self.MachineGunShot_Sound)
            else:
                self.gun_channel.play(self.MachineGunShot_Sound)
            new_Bullet_left = Bullet()
            new_Bullet_left.rect.x = self.rect.x + self.rect.width - 10
            new_Bullet_left.rect.y = self.rect.y + 20
            
            new_Bullet_right = Bullet()
            new_Bullet_right.rect.x = self.rect.x + 10
            new_Bullet_right.rect.y = self.rect.y + 20
            
            self.Bullets.add(new_Bullet_left)
            self.Bullets.add(new_Bullet_right)


    
    def hit(self):
        if self.hit_channel.get_busy() != True:
            self.hit_snd.play() 
        else:
            self.hit_channel.stop()
            self.hit_snd.play() 

        if self.hp <= 0:
            self.destroy()
        self.hp -= 1


    def spawn(self, craft_type): 
        self.__init__(craft_type)

    
    def destroy(self):
        self.kill()
        self.destroyed = True
    
    def rotate(self, angle):
        rot_image = pygame.transform.rotate(self.image, angle)
        rot_rect = self.rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        return rot_image

        




class Enemy(pygame.sprite.Sprite):
    def __init__(self, craft_type = 2):
        super(Enemy, self).__init__()
        self.shiptype = craft_type


        # importing images for explosion animation
        self.explosion_01 = pygame.image.load('GAS\FX\Explosion\explosion1.png').convert_alpha()
        self.explosion_01 = pygame.transform.scale(self.explosion_01, (self.explosion_01.get_width()*3, self.explosion_01.get_height()*3))

        self.explosion_02 = pygame.image.load('GAS\FX\Explosion\explosion2.png').convert_alpha()
        self.explosion_02 = pygame.transform.scale(self.explosion_02, (self.explosion_02.get_width()*3, self.explosion_02.get_height()*3))

        self.explosion_03 = pygame.image.load('GAS\FX\Explosion\explosion3.png').convert_alpha()
        self.explosion_03 = pygame.transform.scale(self.explosion_03, (self.explosion_03.get_width()*3, self.explosion_03.get_height()*3))

        self.explosion_04 = pygame.image.load('GAS/FX/Explosion/explosion4.png').convert_alpha()
        self.explosion_04 = pygame.transform.scale(self.explosion_04, (self.explosion_04.get_width()*3, self.explosion_04.get_height()*3))
        
        self.explosion_05 = pygame.image.load('GAS\FX\Explosion\explosion5.png').convert_alpha()
        self.explosion_05 = pygame.transform.scale(self.explosion_05, (self.explosion_05.get_width()*3, self.explosion_05.get_height()*3))

        self.explosion_06 = pygame.image.load('GAS\FX\Explosion\explosion6.png').convert_alpha()
        self.explosion_06 = pygame.transform.scale(self.explosion_06, (self.explosion_06.get_width()*3, self.explosion_06.get_height()*3))

        self.explosion_07 = pygame.image.load('GAS/FX/Explosion/explosion7.png').convert_alpha()
        self.explosion_07 = pygame.transform.scale(self.explosion_07, (self.explosion_07.get_width()*3, self.explosion_07.get_height()*3))

        self.p_explosion_01 = pygame.image.load('GAS\FX\Explosion\purple_explosion1.png').convert_alpha()
        self.p_explosion_01 = pygame.transform.scale(self.p_explosion_01, (self.p_explosion_01.get_width()*3, self.p_explosion_01.get_height()*3))

        self.p_explosion_02 = pygame.image.load('GAS\FX\Explosion\purple_explosion2.png').convert_alpha()
        self.p_explosion_02 = pygame.transform.scale(self.p_explosion_02, (self.p_explosion_02.get_width()*3, self.p_explosion_02.get_height()*3))

        self.p_explosion_03 = pygame.image.load('GAS\FX\Explosion\purple_explosion3.png').convert_alpha()
        self.p_explosion_03 = pygame.transform.scale(self.p_explosion_03, (self.p_explosion_03.get_width()*3, self.p_explosion_03.get_height()*3))

        self.p_explosion_04 = pygame.image.load('GAS\FX\Explosion\purple_explosion4.png').convert_alpha()
        self.p_explosion_04 = pygame.transform.scale(self.p_explosion_04, (self.p_explosion_04.get_width()*3, self.p_explosion_04.get_height()*3))
        
        self.p_explosion_05 = pygame.image.load('GAS\FX\Explosion\purple_explosion5.png').convert_alpha()
        self.p_explosion_05 = pygame.transform.scale(self.p_explosion_05, (self.p_explosion_05.get_width()*3, self.p_explosion_05.get_height()*3))


        match craft_type:
            case 0:
                self.anim_explosion = [self.p_explosion_01,
                                    self.p_explosion_02,
                                    self.p_explosion_03,
                                    self.p_explosion_04,
                                    self.p_explosion_05,
                                    self.explosion_06,
                                    self.explosion_07]
            
            case 1:
                self.anim_explosion = [self.explosion_01,
                                    self.explosion_02,
                                    self.explosion_03,
                                    self.explosion_04,
                                    self.explosion_05,
                                    self.explosion_06,
                                    self.explosion_07]
            case 2:
                self.anim_explosion = [self.explosion_01,
                                    self.explosion_02,
                                    self.explosion_03,
                                    self.explosion_04,
                                    self.explosion_05,
                                    self.explosion_06,
                                    self.explosion_07]
            case 3:
                self.anim_explosion = [self.explosion_01,
                                    self.explosion_02,
                                    self.explosion_03,
                                    self.explosion_04,
                                    self.explosion_05,
                                    self.explosion_06,
                                    self.explosion_07]
            
        self.anim_index = 0
        self.frame_len_max = 4
        self.frame_len = self.frame_len_max

        self.is_destroyed = False
        self.is_invincible = False

        self.image = pygame.image.load(CraftType.craft[craft_type]).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*3, self.image.get_height()*3))
        self.MACShot_Sound = pygame.mixer.Sound('GAS/Sounds/shot.ogg')
        self.hit_snd = pygame.mixer.Sound('GAS/Sounds/explosion.ogg')
       
    

        self.rect   = self.image.get_rect()
        self.rect.x = random.randrange(0, settings.width - self.rect.width)
        self.rect.y = settings.height
        self.angle = 0
        self.hp = 15
        self.gun_timer = random.randrange(1,10)

        self.MACRounds = pygame.sprite.Group()

    
        self.vel_x  = random.randrange(-3, 3)
        self.vel_y  = -random.randrange(2, 5)

    def update(self):
        self.MACRounds.update()
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        
        if self.is_destroyed:
            max_index = self.anim_explosion.__len__() - 1
            if self.frame_len == 0:
                self.anim_index += 1
                if self.anim_index > max_index:
                    self.kill()
                else:
                    self.image = self.anim_explosion[self.anim_index]
                    self.frame_len = self.frame_len_max                
            else:
                self.frame_len -= 1
                



        for MAC in self.MACRounds:
            if MAC.rect.y <= 0 or MAC.rect.x <= 0 or MAC.rect.y <= settings.height or  MAC.rect.x <= settings.width:
                self.MACRounds.remove(MAC)

        #if self.gun_timer == 0:
            ##self.fire()
        #    self.gun_timer = random.randrange(1,3)
        #self.gun_timer -=1
            

            

        if self.rect.x <= 0:
            self.vel_x = -self.vel_x
        elif self.rect.x >= settings.width - self.rect.width:
            self.vel_x = -self.vel_x

        
        if self.rect.y <= -self.rect.height:
            self.rect.y= settings.height 
            self.vel_x = -self.vel_x
        elif self.rect.y >= settings.height:
            self.vel_y = -self.vel_y

         

        


    def fireMAC(self):
        if self.shoot_channel.get_busy() == True:
            self.channel.stop()
            self.MACShot_Sound.play()
        else:
            self.MACShot_Sound.play()

        new_MAC = MAC()
        new_MAC.rect.x = self.rect.x + (self.rect.width // 2.0010)
        new_MAC.rect.y = self.rect.y - 5
    

        MACRound = new_MAC
        self.MACRounds.add(MACRound)
    
    def hit(self, type):
        #if self.channel.get_busy() != True:
        #    self.hit_snd.play() 
        #else:
        #    self.channel.stop()
        if not self.is_invincible:
            self.hit_snd.play() 
            if type == "MAC":
                self.hp -= 5
                if self.hp <= 0:
                    self.is_invincible = True
                    self.is_destroyed = True
                    self.rect.x = self.rect.x - 170
                    self.rect.y = self.rect.y - 120
                    self.image = self.anim_explosion[self.anim_index]
                
            elif type == "BULLET":
                self.hp -= 1
                if self.hp <= 0:
                    self.is_invincivle = True
                    self.is_destroyed = True
                    self.rect.x = self.rect.x - 170
                    self.rect.y = self.rect.y - 120
                    self.image = self.anim_explosion[self.anim_index]
        else:
            pass
            
        

    
    
        

        

    def rotate(self, angle):
        new_image = pygame.transform.rotate(self.image, angle)
        new_image = self.rect.copy()
        new_image.center = new_image.get_rect().center
        rot_image = new_image.subsurface(new_image).copy()
        return rot_image
    



    
    

class MAC(pygame.sprite.Sprite):
    def __init__(self):
        super(MAC, self).__init__()
        self.image = pygame.image.load('GAS/Rounds/MAC.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*2, self.image.get_height()*2))
        self.rect = self.image.get_rect()
        self.angle = 0

        self.vel_x = 0
        self.vel_y = -15

        

    def update(self):

        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
    
    def rotate(self, angle):
        """rotate an image while keeping its center and size"""
        orig_rect = self.rect
        rot_image = pygame.transform.rotate(self.image, angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        return rot_image
    

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super(Bullet, self).__init__()
        self.image = pygame.image.load('GAS/Rounds/bullet.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*2, self.image.get_height()*2))
        self.rect = self.image.get_rect()
        self.angle = 0

        self.vel_x = 0
        self.vel_y = -30

        

    def update(self):

        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
    
    def rotate(self, angle):
        """rotate an image while keeping its center and size"""
        orig_rect = self.rect
        rot_image = pygame.transform.rotate(self.image, angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        return rot_image
    



         

    