"""
code for general menu class, sub-classes and speech bubbles
"""
import pygame
from Constants import display as d


class Menu(object):
    """
    constructor for parent class
    """

    def __init__(self):
        # variables to draw the size of the menu
        self.top_left = None
        self.top_right = None
        self.bottom_left = None
        self.bottom_right = None

        # variables to draw the border of the menu
        self.border_TL = self.top_left
        self.border_TR = self.top_right
        self.border_BL = self.bottom_left
        self.border_BR = self.bottom_right

        self.color = None

    # draws menu to screen
    def draw_menu(self, gameDisplay):
        pass
        pygame.draw.rect(gameDisplay, self.color, [self.top_left, self.bottom_left, self.top_right, self.bottom_right])

class CombatMenu(Menu):
    """
    creates menu used for combat allowing player interaction
    """

    def __init__(self):
        # calls the parent constructor
        super().__init__()

        self.top_left = 0
        self.top_right = d.DISPLAY_WIDTH
        self.bottom_left = None
