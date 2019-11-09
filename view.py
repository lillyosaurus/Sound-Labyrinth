import pygame

class View():
    """Drawing Class for the game"""

    def __init__(self, map):

        self.pixel_size = 32
        self.width = self.pixel_size * 7
        self.height = self.pixel_size * 7
        self.screen = 