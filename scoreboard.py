import pygame.font
from pygame.sprite import Group
from ship import Ship 



class Scoreboard():
    # A CLASS TO REPORT SCORING INFORMATION
    def __init__(self,ai_settings,screen,stats):
        # INITIALIZING SCOREKEEPING ATTRIBUTES 
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.ai_settings=ai_settings
        self.stats=stats

        # FONT SETTINGS FOR SCORING INFORMATION
        self.text_color=(30,30,30)
        self.font=pygame.font.SysFont(None,48)

        # PREPARE THE INITIAL SCORE IMAGE
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_high_score(self):
        # TURN THE HIGH SCORE INTO THE RENDERED IMAGE
        high_score=int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
        self.text_color, self.ai_settings.bg_color)
        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top


    def prep_score(self):
        # TURN THE SCORE INTO AN RENDERED IMAGE
        rounded_score=int(round(self.stats.score,-1))
        score_str="{:,}".format(rounded_score)
        score_str=str(self.stats.score)
        self.score_image=self.font.render(score_str,True,self.text_color,self.ai_settings.bg_color)

        # DISPLAY THE SCORE AT TOP RIGHT OF THE SCREEN
        self.score_rect=self.score_image.get_rect()
        self.score_rect.right=self.screen_rect.right -20 
        self.score_rect.top=20

    def prep_level(self):
        """Turn the level into a rendered image."""
        self.level_image = self.font.render(str(self.stats.level), True,
        self.text_color, self.ai_settings.bg_color)

        # POSITION THE LEVEL BELOWE THE SCORE
        self.level_rect=self.level_image.get_rect()
        self.level_rect.right=self.score_rect.right
        self.level_rect.top=self.score_rect.bottom+10


    def show_score(self):
        # DRAW SCORE TO THE SCREEN
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        self.ships.draw(self.screen)

    def prep_ships(self):
        # SHOW HOW MANY SHIPS ARE LEFT
        self.ships=Group()
        for ship_number in range(self.stats.ships_left):
            ship=Ship(self.ai_settings,self.screen)
            ship.rect.x=10+ship_number*ship.rect.width
            ship.rect.y=1.5
            self.ships.add(ship)