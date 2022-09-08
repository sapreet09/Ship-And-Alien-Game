import sys
from turtle import bgcolor
from alien import Alien
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard




def run_game():
    # INITIALIZE GAME AND CREATE A SCREEN OBJECT
    pygame.init()
    # INITIALIZING THE INSTANCE OF SETTING CLASS 
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invansion")

    # MAKE THE PLAYBUTTON
    play_button=Button(ai_settings,screen,'Play')
     
    # CREATE AN INSTANCE TO STORE GAME STATISTICS AND CREATE A SCOREBOARD
    stats=GameStats(ai_settings)
    sb=Scoreboard(ai_settings,screen,stats)


    # MAKE A SHIP
    ship=Ship(ai_settings,screen)
    bullets=Group()
    aliens=Group()

    # CREATE THE FLEET OF THE ALIENS
    gf.create_fleet(ai_settings,screen,ship,aliens)
    # SET THE BACKGROUND COLOR
    # bg_color=(230,230,230)
    # MAKE AN ALIEN
    alien=Alien(ai_settings,screen)
    # START THE MAIN LOOP FOR THE GAME
    while True:
        # WATCH FOR KEYBOARD AND MOUSE EVENTS
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
        if stats.game_active:
                ship.update()
                gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
                gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)       
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)

        # gf.update_screen(ai_settings,screen,ship,bullets)
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        # MAKE THE MOST RECENT DRAWN SCREEN VISIBLE
        # pygame.display.flip()

run_game()