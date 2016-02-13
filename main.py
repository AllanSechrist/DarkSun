import pygame
from player import hero
pygame.init()

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (200, 200, 0)

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Dark Sun')

clock = pygame.time.Clock()

FPS = 30

player = hero.Hero(YELLOW)
active_sprite_list = pygame.sprite.Group()


active_sprite_list.add(player)

def main():

    game_exit = False

    while not game_exit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

            # gets player input to move player
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print('Left')
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    print('Right')
                    player.go_right()
                if event.key == pygame.K_UP:
                    print('Up')
                    player.go_up()
                if event.key == pygame.K_DOWN:
                    print('Down')
                    player.go_down()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                    player.stop_x()
                if event.key == pygame.K_UP or pygame.K_DOWN:
                    player.stop_y()

        # update the player.
        active_sprite_list.update()

        gameDisplay.fill(WHITE)
        active_sprite_list.draw(gameDisplay)

        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()
    quit()


if __name__ == '__main__':
    main()

# adsf