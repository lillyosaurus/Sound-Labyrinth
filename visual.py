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

        self.game_on = True
        self.font_type = 'AmaticSC-Regular.ttf'

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

    def draw_sentence(self,sentence,size,rect_center):
        pure_white = (255, 255, 255)
        white = (220,220,220)
        black = (0, 0, 0)
        font = pygame.font.Font(self.font_type,size)
        X = rect_center[0]
        Y = rect_center[1]
        text = font.render(sentence, True, white, black)
        textRect = text.get_rect()
        textRect.center = (X,Y)
        self.screen.blit(text,textRect)

    def draw_image(self,image,rect_center):
        self.screen.blit(image,rect_center)

    def draw_home_screen(self):
        self.draw_sentence('Sound',96,[self.width//2,self.height//3-48])
        self.draw_sentence('Labyrinth',96,[self.width//2,self.height//3+60])
        #self.draw_image(self.screen, self.width//2, self.height//2 + 48)
        self.draw_sentence('Software Design - Fall 2019',48,[self.width//2, 3*self.height//4-30])
        self.draw_sentence('Kyle Bertram  SeungU Lyu Tim Novak',36,[self.width//2, 3*self.height//4+30])
        self.draw_sentence('Kyle Bertram  SeungU Lyu Tim Novak',36,[self.width//2, 3*self.height//4+30])
        self.draw_sentence('Press I for Instructions, Press C for Credits, Press Space to Start',36,[self.width//2, self.height - 96])

    def draw_instructions(self):
        self.draw_sentence('INSTRUCTIONS GO HERE',36,[self.width//2, self.height//2])
        self.draw_sentence('Press H for Home, Press Space to Start',36,[self.width//2, self.height - 96])

    def draw_credits(self):
        self.draw_sentence('CREDITS GO HERE',36,[self.width//2, self.height//2])
        self.draw_sentence('Press H for Home',36,[self.width//2, self.height - 96])

    def close_screen(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(self.game_on)
                self.game_on = False
                
