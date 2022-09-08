import pygame.font

class Button():
    def __init__(self,ai_settings,screen,msg):
        # INITIALIZE BUTTON ATTRIBUTE
        self.screen=screen
        self.screen_rect=screen.get_rect()

        # SET THE DIMENSIONS AND THE ATTRIBUTE OF THE BUTTON
        self.width, self.height=200,50
        self.button_color=(0,255,0)
        self.text_color=(255,255,255)
        self.font=pygame.font.SysFont(None,48)

        # BUILD THE BUTTON'S RECT ATTRIBUTE AND CENTER IT
        self.rect=pygame.Rect(0,0,self.width,self.height)
        self.rect.center=self.screen_rect.center

        # THE BUTTON MESSAGE NEED TO BE PREPPED ONLY ONCE
        self.prep_msg(msg)

    def prep_msg(self,msg):
        # TURN MSG INTO RENDERED IMAGE AND CENTER TEXT ON THE BOTTOM
        self.msg_image=self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect=self.msg_image.get_rect()
        self.msg_image_rect.center=self.rect.center

    def draw_button(self):
        # DRAW BLANK BUTTON AND THEN DRAW MESSAGE
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)