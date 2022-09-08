import pygame
from pygame.sprite import Sprite



class Ship(Sprite):
    def __init__(self,ai_settings,screen):
        '''INITIALIZING THE SCREEN AND SET ITS STARTING POSITION'''
        super(Ship,self).__init__()
        self.screen=screen
        self.ai_settings=ai_settings
        # LOAD THE SHIP IMAGE 
        self.image=pygame.image.load('images/new.ico').convert()
        self.image=pygame.transform.scale(self.image, (80,40))
        self.image.set_colorkey((255,255,255))

        
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        # START EACH NEW SHIP  AT THE BOTTOM CENTRE OF THE SCREEN
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom

        self.center=float(self.rect.centerx)
        self.moving_right=False
        self.moving_left=False
    def update(self):
        if self.moving_right and self.rect.right< self.screen_rect.right:
            # self.rect.centerx+=1
            self.center+=self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left>0:
            # self.rect.centerx-=1
            self.center-=self.ai_settings.ship_speed_factor
        # UPDATE RECT OBJECT FROM SELF.CENTER
        self.rect.centerx=self.center

    def blitme(self):
        # DRAW THE SHIP AT ITS CURRENT LOCATION
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        # CENTER THE SHIP ON THE SCREEN
        self.center=self.screen_rect.centerx