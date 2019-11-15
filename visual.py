import pygame
import os

class VisualView():
    """Drawing Class for the game"""

    def __init__(self, gamemap):
        self.map = gamemap
        self.width = self.map.pixel_size * 7
        self.height = self.map.pixel_size * 7

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Sound Labyrinth")

        self.on = True

    def clear_screen(self):
        self.screen.fill((0,0,0))

    def refresh_screen(self):
        pygame.display.flip()

    def draw_screen(self):
        x_offset = int(self.width/2) - self.map.player.rect.x - self.map.pixel_size/2
        y_offset = int(self.height/2) - self.map.player.rect.y - self.map.pixel_size/2
        for wall in self.map.wall_list:
            wall.draw_offset(self.screen, x_offset, y_offset)
        self.map.player.draw_offset(self.screen, x_offset, y_offset)

    def close_screen(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.on = False
