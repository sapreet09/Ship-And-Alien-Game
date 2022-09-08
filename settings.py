class Settings():
    def __init__(self):
        '''INITILIAZE THE GAME'S STATIC SETTINGS'''
        # BULLET SETTINGS
        self.bullet_speed_factor=90
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=60,60,60
        # SCREEN SETTINGS
        self.screen_width=1000
        self.screen_height=700
        self.bg_color=(255,255,255)
        self.ship_speed_factor=1.5
        self.ship_limit=3
        self.bullets_allowed=3
        # ALIEN SETTINGS
        self.alien_speed_factor=1
        self.fleet_drop_speed=10
        # FLEET DIRECTION OF 1 REPRESENTS RIGHT: -1 REPRESENTS LEFT
        self.fleet_direction=1

        # HOW QUICKLY THE GAME SPEEDS UP
        self.speedup_scale=1.9

        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
            # INITIALIZE SETTINGS THAT CHANGE THROUGHOUT THE GAME
            self.ship_speed_factor=4
            self.bullet_speed_factor=8
            self.alien_speed_factor=1
            # FLEET DIRECTION 1 REPREENTS RIGHT AND -1 REPRESENTS LEFT 
            self.fleet_direction=1
            # SCORING
            self.alien_points=50

    def increase_speed(self):
            # INCREASE SPEED SETTINGS AND ALIEN POINT VALUES
            self.ship_speed_factor*=self.speedup_scale
            self.bullet_speed_factor*=self.speedup_scale
            self.alien_speed_factor*=self.speedup_scale
            self.alien_points=int(self.alien_points*self.score_scale)
            print(self.alien_points)