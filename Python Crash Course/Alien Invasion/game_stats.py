class GameStats():
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        try:
            with open("stats") as file:
                self.high_score = int(file.read())
        except FileNotFoundError:
            print("Error")
            self.high_score = 0
        except ValueError:
            self.high_score = 0

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0

