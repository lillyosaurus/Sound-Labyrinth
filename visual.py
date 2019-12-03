import pygame
import os
import textrect

class VisualView():
    """Drawing Class for the game"""

    def __init__(self, gamemap):
        self.map = gamemap
        self.width = self.map.pixel_size * 7
        self.height = self.map.pixel_size * 7
        self.img_size = 128

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Sound Labyrinth")

        self.game_on = True
        self.font_type = 'AmaticSC-Regular.ttf'

        self.player = pygame.transform.scale(pygame.image.load('image/player.png'),(self.img_size,self.img_size))
        self.arrows = self.wall = pygame.transform.scale(pygame.image.load('image/test_arrows.png'),(self.img_size*2,self.img_size))
        self.aswd = self.wall = pygame.transform.scale(pygame.image.load('image/test_aswd.png'),(self.img_size*2,self.img_size))
        self.show_clicks = True
        self.tick = 0

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

    def draw_paragraph(self,sentance,size,rect):
        white = (220,220,220)
        black = (0, 0, 0)
        font = pygame.font.Font(self.font_type,size)

        my_rect = textrect.render_textrect(sentance,font,rect,white,black,justification = 0)
        self.screen.blit(my_rect, rect.topleft)
        # pure_white = (255, 255, 255)
        # white = (220,220,220)
        # black = (0, 0, 0)
        # line = []
        # for character in sentance:
        #     line.append(character)
        #     font = pygame.font.Font(self.font_type,size)
        #     line1 = font.render(''.join(line), True, white, black)
        #     print(pygame.font.Font.size(line1))
        pass

    def draw_image(self,image,rect_center):
        self.screen.blit(image,rect_center)

    def blink_text(self,sentance,size,rect_center,time):
        if pygame.time.get_ticks() < self.tick + time:
            self.draw_sentence('Press I for Instructions, Press C for Credits, Press Space to Start',36,rect_center)
        elif pygame.time.get_ticks() > self.tick + time*2:
            self.tick = pygame.time.get_ticks()

    def draw_home_screen(self):
        self.clear_screen()
        self.draw_sentence('Sound',96,[self.width//2,self.height//3-48])
        self.draw_sentence('Labyrinth',96,[self.width//2,self.height//3+60])
        self.draw_image(self.player, [self.width//2-self.img_size//2, self.height//2-self.img_size//2+48])
        self.draw_sentence('Software Design - Fall 2019',48,[self.width//2, 3*self.height//4-30])
        self.draw_sentence('Kyle Bertram  SeungU Lyu Tim Novak',36,[self.width//2, 3*self.height//4+30])
        self.draw_sentence('Kyle Bertram  SeungU Lyu Tim Novak',36,[self.width//2, 3*self.height//4+30])
        self.blink_text('Press I for Instructions, Press C for Credits, Press Space to Start',36,[self.width//2, self.height - 96], 1000)

    def draw_instructions(self):
        self.margin = 72
        self.clear_screen()

        self.draw_paragraph('The Game',72,pygame.Rect((self.margin, 48, self.width - self.margin*2, 300)))
        self.draw_paragraph('You are trapped in a labyrinth between the worlds of the  living and the dead, and have been cursed to remain here until you help the tormented souls find their peace. They must attone for their misdeeds, resolve thier regrets in life, and move on to the afterlife. Only then are you free of your duties.', 32, pygame.Rect((self.margin, 144, self.width - self.margin*2, 300)))

        self.draw_image(self.arrows, [self.width//4-self.img_size*2//2, self.height//2-self.img_size//2])
        self.draw_image(self.aswd, [3*self.width//4-self.img_size*2//2, self.height//2-self.img_size//2])

        self.draw_sentence('Press H for Home, Press Space to Start',36,[self.width//2, self.height - 96])

    def draw_credits(self):
        self.draw_sentence('CREDITS GO HERE',36,[self.width//2, self.height//2])
        self.draw_sentence('Press H for Home',36,[self.width//2, self.height - 96])

    def close_screen(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_on = False
