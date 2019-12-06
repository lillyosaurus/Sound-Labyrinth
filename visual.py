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
        self.margin = 72

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Sound Labyrinth")

        self.game_on = True
        self.font_type = 'AmaticSC-Regular.ttf'

        self.load_images()

        self.show_clicks = True
        self.tick = 0

    def load_images(self):
        self.control_img_size = 72
        self.player = pygame.transform.scale(pygame.image.load('image/player.png'),(self.img_size,self.img_size))
        self.wall = pygame.transform.scale(pygame.image.load('image/wall.png'),(self.img_size,self.img_size))
        self.reaper = pygame.transform.scale(pygame.image.load('documents/NPCs/reaper/reaper.png'),(self.img_size,self.img_size))
        self.fallen_ruler = pygame.transform.scale(pygame.image.load('documents/NPCs/fallen_ruler/image.png'),(self.img_size,self.img_size))

        # load ASWD
        self.a  = pygame.transform.scale(pygame.image.load('image/controls/a.png'),(self.control_img_size,self.control_img_size))
        self.s = pygame.transform.scale(pygame.image.load('image/controls/s.png'),(self.control_img_size,self.control_img_size))
        self.w = pygame.transform.scale(pygame.image.load('image/controls/w.png'),(self.control_img_size,self.control_img_size))
        self.d = pygame.transform.scale(pygame.image.load('image/controls/d.png'),(self.control_img_size,self.control_img_size))

        #load arrow NEED TO ADD IN ARROW IMAGE
        self.arrow = pygame.transform.scale(pygame.image.load('image/controls/a.png'),(self.control_img_size,self.control_img_size))

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

    def draw_image(self,image,rect_center):
        self.screen.blit(image,rect_center)

    def draw_rotated_image(self,image,angle,rect_center):
        """ Rotates an image counterclockwise with units of degrees"""
        new_image = pygame.transform.rotate(image,angle)
        self.draw_image(new_image,rect_center)

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

    def draw_aswd(self,aswd_center_x,aswd_center_y):
        self.draw_image(self.a, [aswd_center_x-self.control_img_size*2//2, aswd_center_y+self.control_img_size//2])
        self.draw_image(self.s, [aswd_center_x, aswd_center_y+self.control_img_size//2])
        self.draw_image(self.w, [aswd_center_x, aswd_center_y-self.control_img_size//2])
        self.draw_image(self.d, [aswd_center_x+self.control_img_size*2//2, aswd_center_y+self.control_img_size//2])

    def draw_arrow(self,arrow_center_x,arrow_center_y):
        self.draw_rotated_image(self.arrow,90, [arrow_center_x-self.control_img_size*2//2, arrow_center_y+self.control_img_size//2])
        self.draw_rotated_image(self.arrow,180, [arrow_center_x, arrow_center_y+self.control_img_size//2])
        self.draw_rotated_image(self.arrow,0, [arrow_center_x, arrow_center_y-self.control_img_size//2])
        self.draw_rotated_image(self.arrow,270, [arrow_center_x+self.control_img_size*2//2, arrow_center_y+self.control_img_size//2])

    def draw_instructions(self):
        self.margin = 72
        self.clear_screen()

        self.draw_paragraph('The Game',72,pygame.Rect((self.margin, 48, self.width - self.margin*2, 300)))
        self.draw_paragraph('You are trapped in a labyrinth between the worlds of the  living and the dead, and have been cursed to remain here until you help the tormented souls find their peace. They must atone for their misdeeds, resolve their regrets in life, and move on to the afterlife. Only then are you free of your duties.', 32, pygame.Rect((self.margin, 144, self.width - self.margin*2, 300)))

        self.draw_aswd(self.width//4,self.height//2)
        self.draw_sentence('Use ASWD keys to move',24,[self.width//4+48, self.height//2+160])

        self.draw_arrow(3*self.width//4-self.control_img_size, self.height//2)
        self.draw_sentence('Use arrow keys to ping',24,[3*self.width//4-48, self.height//2+160])

        self.draw_sentence('Press H for Home, Press Space to Start',36,[self.width//2, self.height - 96])

    def draw_credits(self):

        '''CODE TO GENERATE REPRESENTITIVE IMAGES
        self.draw_image(self.player, [self.width//2-self.img_size//2, self.height//2-self.img_size//2+48])
        self.draw_image(self.fallen_ruler, [self.width//2-self.img_size//2+2*128, self.height//2-self.img_size//2+48])
        '''
        self.draw_paragraph('About Sound Labyrinth',72,pygame.Rect((self.margin, 48, self.width - self.margin*2, 300)))
        self.draw_paragraph('Sound Labyrinth is an accessible computer game created for Software Design at Olin College of Engineering. We created this game with the intention of it being fully accessible to sighted and visually imaired players alike.', 32, pygame.Rect((self.margin, 144, self.width - self.margin*2, 300)))
        self.draw_sentence('Press H for Home',36,[self.width//2, self.height - 96])

    def close_screen(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_on = False
