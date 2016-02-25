"""
code to create and manage player interaction with pause menu
"""
import pygame
from Constants import display as d


def pause():
    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # exits the game when player closes the window
                paused = False
                d.terminate()

            # gets player input to move player's menu selection
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    # controls for menu select go here
                    pass
                if event.key == pygame.K_RIGHT:
                    # controls for menu select go here
                    pass
                if event.key == pygame.K_UP:
                    # controls for menu select go here
                    pass
                if event.key == pygame.K_DOWN:
                    # controls for menu select go here
                    pass

                if event.key == pygame.K_p:
                    paused = False

        d.gameDisplay.fill(d.RED)

        pygame.display.update()

        d.clock.tick(d.FPS)
