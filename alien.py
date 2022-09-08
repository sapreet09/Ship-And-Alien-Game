import pygame
from pygame.sprite import Sprite 

class Alien(Sprite):
    '''A CLASS TO REPRESENT A SINGLE ALIEN IN THE FLEET'''
    def __init__(self,ai_settings,screen):
        super(Alien, self).__init__()
        self.screen=screen
        self.ai_settings=ai_settings


    # LOAD THE ALIEN IMAGE AND SET ITS RECT ATTRIBUTE
        self.image=pygame.image.load('images/alien.png')
        self.image=pygame.transform.scale(self.image, (50,50))
        self.rect=self.image.get_rect()

    # START EACH NEW ALIEN NEAR THE TOP LEFT OF THE SCREEN
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height

    # STORE THE ALIEN'S EXACT POSITION
        self.x=float(self.rect.x)
    
    def blitme(self):
        # DRAW THE ALIEN AND ITS EXACT POSITION
        self.screen.blit(self.image,self.rect)

    def update(self):
        self.x+=(self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)     #MOVE THE ALIEN RIGHT OR LEFT
        self.rect.x=self.x

    def check_edges(self):
        # RETURN TRUE IF ALIEN IS AT EDGE OF THE SCREEN
        screen_rect=self.screen.get_rect()
        if self.rect.right>=screen_rect.right:
            return True
        elif self.rect.left<=0:
            return True