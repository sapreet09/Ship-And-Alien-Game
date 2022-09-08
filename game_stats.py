class GameStats():
    # TRACK STATISTICS FOR ALIEN INVANSION
    def __init__(self, ai_settings):
        # INITIALIZE SETTINGS
        self.ai_settings=ai_settings
        self.reset_stats()
        # START GAME IN INACTIVE STATE
        self.game_active=False
        self.high_score=0

    def reset_stats(self):
        # INITIALIZE STATISTICS THAT CAN CHANGE DURING THE GAME
        self.ships_left=self.ai_settings.ship_limit
        self.score=0
        self.level=1