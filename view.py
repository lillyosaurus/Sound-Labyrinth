import pygame
import os

class View():
    """Drawing Class for the game"""

    def __init__(self, gamemap):
        self.pixel_size = 64
        self.width = self.pixel_size * 7
        self.height = self.pixel_size * 7

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Sound Labyrinth")

        self.map = gamemap
        self.on = True

    def clear_screen(self):
        self.screen.fill((0,0,0))
    
    def refresh_screen(self):
        pygame.display.flip()
    
    def draw_screen(self):
        offset = 1

    def close_screen(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.on = False