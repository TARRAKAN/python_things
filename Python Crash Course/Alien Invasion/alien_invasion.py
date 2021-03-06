import sys
import pygame
import game_functions
from settings import Settings
from ship import Ship
from alien import Alien
from game_stats import GameStats
from pygame.sprite import Group
from button import Button
from scoreboard import Scoreboard

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(ai_settings, screen, "Play")
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    game_functions.create_fleet(ai_settings, screen, ship, aliens)

    while(True):
        game_functions.check_events(ai_settings, screen, stats, sb, play_button, ship,
                aliens, bullets)
        if stats.game_active:
            ship.update()
            game_functions.update_bullets(ai_settings, screen, stats, sb, ship,
                    aliens, bullets)
            game_functions.update_aliens(ai_settings, stats, screen,sb,ship, aliens, bullets)
        game_functions.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, 
                    play_button)


run_game()
