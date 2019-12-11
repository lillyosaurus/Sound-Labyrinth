import pygame
import os
import textrect

class VisualView():
    """
    The class used to display the game on to a screen.

    Attributes:
    map -> GameMap object with all required objects to play the game
    width -> width of the screen in pixels
    height -> height of the screen in pixels
    img_size -> size to scale images when loaded
    margin -> margin in pixels
    screen -> initialized screen for display with width and height
    game_on -> boolean to check whether the game is running or not
    font_type -> font used to display dialogues
    """

    def __init__(self, gamemap):
        """
        Initalize the Audio class with default variable values

        gamemap: GameMap object
        """
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
        """
        Load all the images needed to show instruction page.
        """
        self.control_img_size = 72
        self.player = pygame.transform.scale(pygame.image.load('image/player.png'),(self.img_size,self.img_size))
        self.wall = pygame.transform.scale(pygame.image.load('image/wall.png'),(self.img_size,self.img_size))
        self.reaper = pygame.transform.scale(pygame.image.load('documents/NPCs/reaper/image.png'),(self.img_size,self.img_size))
        self.fallen_ruler = pygame.transform.scale(pygame.image.load('documents/NPCs/fallen_ruler/image.png'),(self.img_size,self.img_size))

        # load ASWD
        self.a  = pygame.transform.scale(pygame.image.load('image/controls/a.png'),(self.control_img_size,self.control_img_size))
        self.s = pygame.transform.scale(pygame.image.load('image/controls/s.png'),(self.control_img_size,self.control_img_size))
        self.w = pygame.transform.scale(pygame.image.load('image/controls/w.png'),(self.control_img_size,self.control_img_size))
        self.d = pygame.transform.scale(pygame.image.load('image/controls/d.png'),(self.control_img_size,self.control_img_size))

        #load arrow NEED TO ADD IN ARROW IMAGE
        self.arrow = pygame.transform.scale(pygame.image.load('image/controls/a.png'),(self.control_img_size,self.control_img_size))

    def clear_screen(self):
        """
        Clear the screen by filling the whole screen with color black
        """
        self.screen.fill((0,0,0))

    def refresh_screen(self):
        """
        Refresh the screenStart
        """
        pygame.display.flip()

    def draw_screen(self):
        """
        Draw all objects inside the GameMap object with respect to the Player object.
        Using right values for offset, Player is always showed in the center of the screen.
        """
        x_offset = int(self.width/2) - self.map.player.rect.x - self.map.pixel_size/2
        y_offset = int(self.height/2) - self.map.player.rect.y - self.map.pixel_size/2
        for wall in self.map.wall_list:
            wall.draw_offset(self.screen, x_offset, y_offset)
        for NPC in self.map.NPC_list:
            NPC.draw_offset(self.screen,x_offset, y_offset)
        self.map.player.draw_offset(self.screen, x_offset, y_offset)

    def draw_sentence(self,sentence,size,rect_center):
        """
        Draw sentence onto the screen.

        Arguments:
        sentence -> string to show on the screen
        size -> size of the font
        rect_center -> center coordinate to show the sentence
        """
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

    def draw_paragraph(self,sentence,size,rect):
        """
        Draw paragraph onto the screen.
        Automatically aligns sentence so that they don't go out of border.

        Arguments:
        sentence -> string to show on the screen
        size -> size of the font
        rect -> rectangle to put the paragraph in
        """
        white = (220,220,220)
        black = (0, 0, 0)
        font = pygame.font.Font(self.font_type,size)

        my_rect = textrect.render_textrect(sentence,font,rect,white,black,justification = 0)
        self.screen.blit(my_rect, rect.topleft)

    def draw_image(self,image,rect_center):
        """
        Draw image onto the screen.

        Arguments:
        image -> image to draw
        rect_center -> center coordinate to show the image
        """
        self.screen.blit(image,rect_center)

    def draw_rotated_image(self,image,angle,rect_center):
        """
        Rotates an image counterclockwise with units of degrees
        """
        new_image = pygame.transform.rotate(image,angle)
        self.draw_image(new_image,rect_center)

    def blink_text(self,sentence,size,rect_center,time):
        """
        Blink a specific sentence with time interval

        Arguments:
        sentence -> string to show on the screen
        size -> size of the font
        rect_center -> center coordinate to show the sentence
        time -> time interval in milisecond
        """
        if pygame.time.get_ticks() < self.tick + time:
            self.draw_sentence(sentence,size,rect_center)
        elif pygame.time.get_ticks() > self.tick + time*2:
            self.tick = pygame.time.get_ticks()

    def draw_aswd(self,aswd_center_x,aswd_center_y):
        """
        Draw ASWD key image
        """
        self.draw_image(self.a, [aswd_center_x-self.control_img_size*2//2, aswd_center_y+self.control_img_size//2])
        self.draw_image(self.s, [aswd_center_x, aswd_center_y+self.control_img_size//2])
        self.draw_image(self.w, [aswd_center_x, aswd_center_y-self.control_img_size//2])
        self.draw_image(self.d, [aswd_center_x+self.control_img_size*2//2, aswd_center_y+self.control_img_size//2])

    def draw_arrow(self,arrow_center_x,arrow_center_y):
        """
        Draw arrow key image
        """
        self.draw_rotated_image(self.arrow,90, [arrow_center_x-self.control_img_size*2//2, arrow_center_y+self.control_img_size//2])
        self.draw_rotated_image(self.arrow,180, [arrow_center_x, arrow_center_y+self.control_img_size//2])
        self.draw_rotated_image(self.arrow,0, [arrow_center_x, arrow_center_y-self.control_img_size//2])
        self.draw_rotated_image(self.arrow,270, [arrow_center_x+self.control_img_size*2//2, arrow_center_y+self.control_img_size//2])

    def draw_home_screen(self):
        """
        Draw home screen with title, player image, and simple blinking instructions
        """
        self.clear_screen()
        self.draw_sentence('Sound',96,[self.width//2,self.height//3-48])
        self.draw_sentence('Labyrinth',96,[self.width//2,self.height//3+60])
        self.draw_image(self.player, [self.width//2-self.img_size//2, self.height//2-self.img_size//2+48])
        self.draw_sentence('Software Design - Fall 2019',48,[self.width//2, 3*self.height//4-30])
        self.draw_sentence('Kyle Bertram  SeungU Lyu Tim Novak',36,[self.width//2, 3*self.height//4+30])
        self.draw_sentence('Kyle Bertram  SeungU Lyu Tim Novak',36,[self.width//2, 3*self.height//4+30])
        #self.blink_text('Press I for Instructions, Press C for Credits, Press Space to Start',36,[self.width//2, self.height - 96], 1000)
        self.draw_sentence('Press I for Instructions, Press C for Credits, Press Space to Play',36,[self.width//2, self.height - 96])

    def draw_instructions(self):
        """
        Draw instruction screen
        """
        self.margin = 72
        self.clear_screen()

        self.draw_paragraph('The Game',72,pygame.Rect((self.margin, 48, self.width - self.margin*2, 300)))
        self.draw_paragraph("You find yourself trapped in the labyrinth, an endless maze between the world of the living and the dead. A place where souls are kept if they still have unfinished business, ties to the world or regrets for what they've done. In order to resolve your past life, you must now learn to help the other trapped souls move on. Only then can you yourself pass on to the afterlife.", 36, pygame.Rect((self.margin, 144, self.width - self.margin*2, 300)))

        self.draw_paragraph('In the game you will navigate using echolocation, and are able to see three meters in any direction',36,pygame.Rect((self.margin, self.height//2-48, self.width - self.margin*2, 300)))

        self.draw_aswd(self.width//4,self.height//2+120)
        self.draw_sentence('Use ASWD keys to move',24,[self.width//4+48, self.height//2+160+120])

        self.draw_arrow(3*self.width//4-self.control_img_size, self.height//2+120)
        self.draw_sentence('Use arrow keys to ping',24,[3*self.width//4-48, self.height//2+160+120])

        self.draw_sentence('Press C for Credits, Press H for Home, Press Space to Start',36,[self.width//2, self.height - 96])

    def draw_credits(self):
        """
        Draw credit screen
        """
        #'''CODE TO GENERATE REPRESENTITIVE IMAGES
        #self.draw_image(self.player, [self.width//2-self.img_size//2, self.height//2-self.img_size//2+48])
        #self.draw_image(self.fallen_ruler, [self.width//2-self.img_size//2+2*128, self.height//2-self.img_size//2+48])

        self.draw_paragraph('About Sound Labyrinth',72,pygame.Rect((self.margin, 48, self.width - self.margin*2, 200)))
        self.draw_paragraph('Sound Labyrinth is an accessible videogame which is designed to provide the same experience to people with a range of sensory abilities. People with a visual impairment can navigate the game via audio input, while people who have hearing impairments can navigate with visual input.', 36, pygame.Rect((self.margin, 144, self.width - self.margin*2, 300)))
        self.draw_paragraph('This game was created by Kyle Bertram, SeungU Lyu and Tim Novak as the final project for Software Design at Olin College of Engineering.', 36, pygame.Rect((self.margin, 144 + 196 + 24, self.width - self.margin*2, 300)))
        self.draw_sentence('Press H for Home',36,[self.width//2, self.height - 96])

    def close_screen(self):
        """
        Check whether the use pressed close button on the window
        If clicked, set game_on to False so that the game is not being played anymore.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_on = False
