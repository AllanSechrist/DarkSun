"""
code for general menu class, sub-classes and speech bubbles
"""
import pygame



class Menu(object):
    """
    constructor for parent class
    """

    def __init__(self):
        # variables to draw the size of the menu
        self.start_x = None
        self.top_right = None
        self.start_y = None
        self.bottom_right = None
        # sets color of menu and color of menu border
        self.color = None
        self.border_color = None

    # draws menu to screen
    def draw_menu(self, gameDisplay):
        pygame.draw.rect(gameDisplay, self.color, [self.start_x, self.start_y, self.top_right, self.bottom_right])
        pygame.draw.rect(gameDisplay, self.border_color, [self.start_x, self.start_y, self.top_right, self.bottom_right], 2)


class CombatMenu(Menu):
    """
    creates menu used for combat allowing player interaction
    """

    def __init__(self, start_x, start_y, top_right, bottom_right, color, border_color):
        # calls the parent constructor
        super().__init__()

        self.start_x = start_x
        self.top_right = top_right
        self.start_y = start_y
        self.bottom_right = bottom_right

        self.color = color
        self.border_color = border_color
