import pygame
from player import hero
from Constants import display as d

# creates and positions player sprites and enemy sprites on during combat
def combat(player):
    # save player's current position on non-combat screen
    save_x = player.rect.x
    save_y = player.rect.y


    player.rect.x = 700
    player.rect.y = 300

    in_combat = True

    while in_combat:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # exits the game when player closes the window
                in_combat = False
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

                if event.key == pygame.K_c:
                    in_combat = False
                    # return player back to original spot on non-combat map
                    player.rect.x = save_x
                    player.rect.y = save_y
            """
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                    player.stop_x()
                if event.key == pygame.K_UP or pygame.K_DOWN:
                    player.stop_y()
            """

        d.active_sprite_list.update()

        d.gameDisplay.fill(d.BLACK)
        d.active_sprite_list.draw(d.gameDisplay)
        d.combat_menu.draw_menu(d.gameDisplay)

        pygame.display.update()

        d.clock.tick(d.FPS)