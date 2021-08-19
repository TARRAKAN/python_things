import sys
import pygame
import game_functions
from settings import Settings
from ship import Ship
from alien import Alien
from pygame.sprite import Group


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    game_functions.create_fleet(ai_settings, screen, ship, aliens)

    while(True):
        game_functions.check_events(ai_settings, screen, ship, bullets)##
        #game_functions.check_events(ship) 
        ship.update()
        bullets.update()
        game_functions.update_bullets(bullets)
        game_functions.update_aliens(ai_settings, aliens)
        game_functions.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
