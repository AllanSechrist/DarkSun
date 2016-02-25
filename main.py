import pygame
from player import hero
from Constants import display as d
from rooms import combat as c
from rooms import pause as p

pygame.init()


pygame.display.set_caption('Dark Sun')

clock = pygame.time.Clock()

active_sprite_list = pygame.sprite.Group()

active_sprite_list.add(d.player)


def main():
    game_exit = False

    while not game_exit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # exits the game when player closes the window
                game_exit = True
                quit()

            # gets player input to move player
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    d.player.go_left()
                if event.key == pygame.K_RIGHT:
                    d.player.go_right()
                if event.key == pygame.K_UP:
                    d.player.go_up()
                if event.key == pygame.K_DOWN:
                    d.player.go_down()

                if event.key == pygame.K_c:
                    c.combat(d.player)

                if event.key == pygame.K_p:
                    p.pause()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                    d.player.stop_x()
                if event.key == pygame.K_UP or pygame.K_DOWN:
                    d.player.stop_y()

        # update the player.
        active_sprite_list.update()

        d.gameDisplay.fill(d.WHITE)
        active_sprite_list.draw(d.gameDisplay)

        pygame.display.update()

        clock.tick(d.FPS)

    pygame.quit()
    quit()


if __name__ == '__main__':
    main()
