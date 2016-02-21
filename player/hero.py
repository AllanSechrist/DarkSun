"""
creates the player class. the player represents the user-controlled sprite on the screen.
"""

import pygame


class Hero(pygame.sprite.Sprite):
    """
    This class creates user controlled characters
    """

    # Attributes
    # Set speed of vector of player
    change_x = 0
    change_y = 0

    def __init__(self, color):

        super().__init__()

        self.image = pygame.Surface([50, 50])
        self.image.fill(color)

        self.rect = self.image.get_rect()

    def update(self):
        """
        move the player
        """
        # move left and right
        self.rect.x += self.change_x

        # move up and down
        self.rect.y += self.change_y

    def go_left(self):
        """
        called when the user hits the left arrow
        """
        self.change_x = -6

    def go_right(self):
        """
        called when the user hits the right arrow
        """
        self.change_x = 6

    def go_up(self):
        """
        called when the user hits the up arrow
        """
        self.change_y = -6

    def go_down(self):
        """
        called when the user hits the down arrow
        """
        self.change_y = 6

    def stop_x(self):
        """
        called when the user lets off the keyboard
        """
        self.change_x = 0

    def stop_y(self):
        """
        called when the user lets off the keyboard
        """
        self.change_y = 0

