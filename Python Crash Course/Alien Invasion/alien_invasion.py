import sys
import pygame
import game_functions
from settings import Settings
from ship import Ship
from pygame.sprite import Group


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings, screen)
    bullets = Group()

    while(True):
        game_functions.check_events(ai_settings, screen, ship, bullets)##
        #game_functions.check_events(ship) 
        ship.update()
        bullets.update()
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        print(len(bullets))
        game_functions.update_screen(ai_settings, screen, ship, bullets)
run_game()
