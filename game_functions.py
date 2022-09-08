import sys
from turtle import Screen
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


def check_keydown_events(event, ai_settings, screen, ship, bullets):
        '''RESP0OND TO KEYPRESSES'''
        if event.key==pygame.K_RIGHT:
                 # MOVE THE SHIP TO THE RIGHT
                    ship.moving_right=True
        elif event.key==pygame.K_LEFT:
                ship.moving_left=True
        elif event.key==pygame.K_SPACE:
                fire_bullet(ai_settings,screen,ship,bullets)
def fire_bullet(ai_settings,screen,ship,bullets):
        #FIRE A BULLET IF LIMIT NOT REACHED YET
        # CREATE A NEW BULLET AND ADD IT TO THE BULLETS GROUP
                if len(bullets)<ai_settings.bullets_allowed:
                        new_bullet=Bullet(ai_settings,screen,ship)
                        bullets.add(new_bullet)      #add new bullet to the group that we created in alien_invansion
def check_keyup_events(event,ship):
            if event.key==pygame.K_RIGHT:
                    ship.moving_right=False
            elif event.key==pygame.K_LEFT:
                    ship.moving_left=False


def check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets):
    for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:        #KEYDOWN MEANS WHEN A KEY IS HELD DOWN
               check_keydown_events(event,ai_settings,screen,ship,bullets)

            elif event.type==pygame.KEYUP:          #KEYUP MEANS WHEN A KEY IS PHYSICALLY  RELEASED
                check_keyup_events(event,ship)
            elif event.type==pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y=pygame.mouse.get_pos()
                check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y)

def check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y):
        # START A NEW GAME WHEN PLAYER HITS PLAY BUTTON
        button_clicked=play_button.rect.collidepoint(mouse_x,mouse_y)
        if button_clicked and not stats.game_active:
                # RESET THE GAME SETTINGS
                ai_settings.initialize_dynamic_settings()
                # HIDE THE MOUSE CURSOR
                pygame.mouse.set_visible(False)         #MAKING MOUSE'S CURSOR INVISIBLE DURING THE GAME 
                # RESET THE GAME statistics
                stats.reset_stats()
                stats.game_active=True

                # RESET THE SCOREBOARD IMAGES
                sb.prep_score()
                sb.prep_high_score()
                sb.prep_level()
                sb.prep_ships()

                # EMPTY THE LIST OF ALIENS AND BULLETS
                aliens.empty()
                bullets.empty()

                # CREATE A NEW FLEET AND CENTER THE SHIP
                create_fleet(ai_settings,screen,ship,aliens)
                ship.center_ship()

def update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button):
        # UPDATING IMAGES ON THE SCREEN AND FLIP  TO THE NEW SCREEN
        # REDRAW ALL BULLETS BEHIND SHIP AND ALIENS
        for bullet in bullets.sprites():                  #The bullets.sprites() method returns a list of all sprites in the group bullets.
                bullet.draw_bullet()
        # screen.fill(ai_settings.bg_color)
        ship.blitme()
        aliens.draw(screen)
        # DRAW THE SCORE INFORMATION
        sb.show_score()

        # DRAW THE PLAY BUTTON IF THE GAME IS INACTIVE
        if not stats.game_active:
                play_button.draw_button()
        pygame.display.flip()

def update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets):
        bullets.update()

        # GET RID OF BULLETS THAT HAVE DISAPPEARED
        for bullet in bullets.copy():
            if bullet.rect.bottom<=0:
                bullets.remove(bullet)
                        # print(len(bullets))
        # Check for any bullets that have hit aliens.
        # If so, get rid of the bullet and the alien.
        check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets)

def check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets):
        """Respond to bullet-alien collisions."""
        # Remove any bullets and aliens that have collided.
        collisions=pygame.sprite.groupcollide(bullets,aliens,True,True) 
        if collisions:
                for aliens in collisions.values():
                        stats.score+=ai_settings.alien_points*len(aliens)
                        sb.prep_score()
                check_high_score(stats,sb)
        if len(aliens)==0:
                # IF THE ENTIRE FLEET IS DESTROYED START A NEW LEVEL
                # DESTROY EXISTING BULLETS , SPEED UP GAME AND CREATE NEW FLEET
                bullets.empty()
                ai_settings.increase_speed()

                # INCREASE LEVEL
                stats.level+=1
                sb.prep_level()

                create_fleet(ai_settings,screen,ship,aliens)



def get_number_aliens_x(ai_settings,alien_width):
        # DETERMINE THE NUMBER OF ALIENS THAT FIT IN A ROW
        available_space_x=ai_settings.screen_width-2*alien_width
        number_aliens_x=int(available_space_x/(2*alien_width))
        return number_aliens_x

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
        # CREATE AN ALIEN AND PLACE IT IN THE ROW
        alien=Alien(ai_settings, screen)

        alien_width=alien.rect.width
        alien.x=alien_width+2*alien_width*alien_number
        alien.rect.x=alien.x
        alien.rect.y=alien.rect.height+2*alien.rect.height*row_number
        aliens.add(alien)

def create_fleet(ai_settings,screen,ship,aliens):
        #CREATE A FULL FLEET OF ALIENS
        # creating an alien and find the number pf aliens in the row

        alien=Alien(ai_settings, screen)
        number_aliens_x=get_number_aliens_x(ai_settings,alien.rect.width)
        number_rows=get_number_rows(ai_settings,ship.rect.height,alien.rect.height)

        # CREATE THE FIRST ROW OF THE ALIEN
        for row_number in range(number_rows):
                for alien_number in range(number_aliens_x):
                        # CREATE AN ALIEN AND PLACE IT IN THE ROW
                        create_alien(ai_settings,screen,aliens,alien_number,row_number)

def get_number_rows(ai_settings,ship_height,alien_height):
        available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
        number_rows=int(available_space_y/(2*alien_height))
        return number_rows

def ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets):
        # RESPOND TO SHIP BEING HIT BY ALIENS
        if stats.ships_left>0:
                # DECREMENT SHIPS_LEFT
                stats.ships_left-=1

                # UPDATE SCOREBOARD
                sb.prep_ships()

                # EMPTY THE LIST OF ALIENS AND BULLETS
                aliens.empty()
                bullets.empty()

                # CREATE A NEW FLEET AND CENTER THE SHIP
                create_fleet(ai_settings,screen,ship,aliens)
                ship.center_ship()

                # PAUSE
                sleep(0.5)
        else:
                stats.game_active=False
                pygame.mouse.set_visible(True)         #MAKING MOUSE'S CURSOR VISIBLE AT THE END OF THE GAME



def update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets):
        # UPDATE THE POSITION OF ALL THE ALIENS IN THE FLEET
         # CHECK IF THE FLEET IS AT EDGE AND  UPDATE THE POSITIONS OF ALL ALIENS IN THE FLEET
        check_fleet_edges(ai_settings,aliens)
        aliens.update()
        # LOOK FOR ALIEN SHIP COLLISION
        if pygame.sprite.spritecollideany(ship,aliens):
                ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets)
        # LOOK FOR ALIENS HITTING THE BOTTOM OF THE SCREEN
        check_aliens_bottom(ai_settings,screen,stats,sb,ship,aliens,bullets)


def check_fleet_edges(ai_settings,aliens):
        # RESPOND APPROPRIATELY IF ANY ALIENS REACHED AT THE EDGE OF THE Screen
        for alien in aliens.sprites():
                if alien.check_edges():
                        change_fleet_direction(ai_settings,aliens)
                        break

def change_fleet_direction(ai_settings,aliens):
        # DROP THE ENTIRE FLEET AND CHANGE THE FLEET'S DIRECTION
        for alien in aliens.sprites():
                alien.rect.y+=ai_settings.fleet_drop_speed
        ai_settings.fleet_direction*=-1

def check_aliens_bottom(ai_settings,screen,stats,sb,ship,aliens,bullets):
        # CHECK IF ANY ALIEN REACHED THE BOTTOM OF THE SCREEN
        screen_rect=screen.get_rect()
        for alien in aliens.sprites():
                if alien.rect.bottom>=screen_rect.bottom:
                        # TREAT THIS THE SAME AS IF THE SHIP GOT HIT
                        ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets)
                        break

def check_high_score(stats,sb):
        # CHECK TO SEE IF THERE'S A NEW HIGH SCORE
        if stats.score>stats.high_score:
                stats.high_score=stats.score
                sb.prep_high_score()