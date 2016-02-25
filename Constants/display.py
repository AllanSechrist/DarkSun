import pygame
from player import hero
from player import menus
# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (200, 200, 0)
# screen size
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
# set frames per second
FPS = 30

player = hero.Hero(YELLOW)


# main over world display
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

active_sprite_list = pygame.sprite.Group()
active_sprite_list.add(player)
clock = pygame.time.Clock()

# creates combat menu
combat_menu = menus.CombatMenu(5, (DISPLAY_HEIGHT / 2) + 100, DISPLAY_WIDTH - 10, DISPLAY_HEIGHT - (DISPLAY_HEIGHT / 2) - 105, BLUE,
                               WHITE)


# exits program
def terminate():
    pygame.quit()
    quit()
