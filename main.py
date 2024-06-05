from Settings.imports import *


pygame.mixer.pre_init(44100, -16, 2,512)
pygame.init()
pygame.mixer.init()


#game variables
game_paused = False
menu_state = "main"

#define fonts
font = pygame.font.SysFont("arialblack", 40)

#define 
text_color = (255, 255, 255)



window = pygame.display.set_mode(settings.size)
fps = settings.frame_per_second
clock = pygame.time.Clock()
bg_color = (0, 0, 0)



#         setting up all objects in game         #
#================================================#
def main_menu():
    pygame.display.set_caption("Ruin Hunter Main Menu")
    background = Background()
    active = True
    rec = pygame.Rect(0,1,2,3)
    while active:
        
        background_gp = pygame.sprite.Group(background)


        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    active = False
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_0:
                            play()
        background_gp.update()  
        background_gp.draw(window)  
        pygame.display.update()
    pygame.quit()


def play():
    pygame.display.set_caption("Ruin Hunter")
    #Background set up
    background = Background()
    background_gp = pygame.sprite.Group(background)


    # player set up
    player = Ship_BP()
    user_HUD = HUD.HUD()
    user_HUD_gp = pygame.sprite.Group(user_HUD)
    player_gp = pygame.sprite.Group(player)

    # Enemies set up
    spawn_enemy = SpawnEnemies()

    # Set up Debris
    spawn_debris = SpawnDebris()

    destroyed_enemys = 0
    respawn_timer = 15

    



    # game loop
    active = True
    while active:

        #MAINTAIN FRAME RATE
        clock.tick(fps)

        

            

        # HANDLE ALL EVENTS
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    pygame.quit()
                    quit()
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_p:
                            active = False
                            main_menu()
                        case pygame.K_SPACE:
                            if not player.destroyed:
                                match player.weapon_choice:
                                    case 0:
                                        player.fireMAC()
                                    case 1:
                                        player.fireBullet() 
                            else:
                                #display to screen "PRESS SPACE TO RESPAWN"
                                player = Ship_BP()
                                player_gp.add(player)
                        case pygame.K_TAB:
                            match player.weapon_choice:
                                case 0:
                                    player.weapon_choice = 1
                                case 1:
                                    player.weapon_choice = 0
                    match event.key:
                        case pygame.K_a | pygame.K_LEFT:
                            player.vel_x = -player.speed 
                        case pygame.K_w | pygame.K_UP:
                            player.vel_y = -(player.speed // 1.5)
                        case pygame.K_s | pygame.K_DOWN:
                            player.vel_y = player.speed*1.1
                        case pygame.K_d | pygame.K_RIGHT:
                            player.vel_x = player.speed 
                        case pygame.K_w | pygame.K_UP:
                            player.vel_y = -(player.speed // 1.5)
                        case pygame.K_s | pygame.K_DOWN:
                            player.vel_y = player.speed*1.1

            
            
            
                case pygame.KEYUP:
                    match event.key:
                        case pygame.K_a | pygame.K_LEFT:
                            player.vel_x = 0
                            match event.key:
                                case pygame.K_w | pygame.K_UP:
                                    player.vel_y = 0
                                case pygame.K_s | pygame.K_DOWN:
                                    player.vel_y = 0
                        case pygame.K_d | pygame.K_RIGHT:
                            player.vel_x = 0
                            match event.key:
                                case pygame.K_w | pygame.K_UP:
                                    player.vel_y = 0
                                case pygame.K_s | pygame.K_DOWN:
                                    player.vel_y = 0

                        case pygame.K_w | pygame.K_UP:
                            player.vel_y = 0
                            match event.key:
                                case pygame.K_a | pygame.K_LEFT:
                                    player.vel_x = 0 
                                case pygame.K_d | pygame.K_RIGHT:
                                    player.vel_x = 0
                        case pygame.K_s | pygame.K_DOWN:
                            player.vel_y = 0
                            match event.key:
                                case pygame.K_a | pygame.K_LEFT:
                                    player.vel_x = 0
                                case pygame.K_d | pygame.K_RIGHT:
                                    player.vel_x = 0
                    
        
            
        
            

        
        # UPDATE ALL OBJECTS
        background_gp.update()   
        player_gp.update()
        spawn_enemy.update()
        spawn_debris.update()

        #Check for collisions
        #returns dictionary
        
        
        collided = pygame.sprite.groupcollide(player_gp, spawn_enemy.e_group, False, False)
        for player, enemy in collided.items():
            enemy[0].hit("SHIP")
            spawn_debris.spawn_debris((enemy[0].rect.x+22, enemy[0].rect.y+25)) 
            spawn_debris.spawn_debris((player.rect.x+22, player.rect.y+25))
            if not enemy[0].is_invincible:
                player.hit()
        
        collided = pygame.sprite.groupcollide(player.Bullets, spawn_enemy.e_group,True, False)
        for Bullet, enemy in collided.items():
            if not enemy[0].is_invincible:
                spawn_debris.spawn_debris((Bullet.rect.x, Bullet.rect.y))
            enemy[0].hit("BULLET")
            

        collided = pygame.sprite.groupcollide(player.MACRounds, spawn_enemy.e_group, True, False)
        for MAC, enemy in collided.items():  
            enemy[0].hit("MAC")
            if not enemy[0].is_invincible:
                spawn_debris.spawn_debris((MAC.rect.x, MAC.rect.y))
        
      
    
    
        
        

        # RENDER DISPLAY
        window.fill(bg_color)
        background_gp.draw(window)  
        
        spawn_enemy.e_group.draw(window)
        player_gp.draw(window)
        spawn_debris.debris_gp.draw(window)
        player.MACRounds.draw(window)
        player.Bullets.draw(window)
        for enemy in spawn_enemy.e_group:
            enemy.MACRounds.draw(window)
        user_HUD_gp.draw(window)
        user_HUD.health_bar_gp.draw(window)
        pygame.display.update()


main_menu()
 