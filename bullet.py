import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_settings,screen,ship):
        '''CREATE A BULLET OBJECT AT SCREEN'S CURRENT POSITION'''
        super(Bullet, self).__init__()
        self.screen=screen

        # CREATE A BULLET RECT(0,0) AND THEN SET CORRECT POSITION
        self.rect=pygame.Rect(0,0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top

        # STORE THE BULLET'S POSITION AS A DECIMAL VALUE
        self.y=float(self.rect.y)

        self.color=ai_settings.bullet_color
        self.speed_factor=ai_settings.bullet_speed_factor

    def update(self):
        # DRWA BULLET TO THE SCREEN
        self.y-=self.speed_factor
        self.rect.y=self.y
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)