import pygame
from player import hero
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
# exits program
def terminate():
    pygame.quit()
    quit()


