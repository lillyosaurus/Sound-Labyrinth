import pygame
import os
import random

class GameObject(pygame.sprite.Sprite):
    """The class which provides the chared behavior for all objects shown in the game

    Attributes:
    image -> the image which is displayed on the screen for the object
    rect -> the bounding box of the object
    original_image -> the inital image of the object
    """

    def __init__(self, image):
        """Set the starting values of the attributes"""
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(image)
        self.image.set_colorkey((0,0,0))

        self.rect = self.image.get_rect()
        self.original_image = self.image


    def location(self):
        """gives the location of the image

        Returns:
        (x,y) -> a tuple describing the location of the image."""
        return(self.rect.x, self.rect.y)

    def size(self):
        """gives the size of the image

        Returns:
        (#) -> a tuple describing length of one side of the object in pixels."""
        return(self.rect.size)

    def draw(self, screen):
        """draws the image associated with the object

        Arguments:
        screen -> the screen which the object will be drawn on"""
        screen.blit(self.image, self.rect)

    def draw_offset(self, screen, x, y):
        screen.blit(self.image, self.rect.move(x,y))

    def set_position(self, x, y):
        """A method which sets the position of the object on the screen

        Arguments:
        x -> the x cordinate describing the location of the image.
        y -> the y cordinate describing the location of the image."""
        self.rect.x = x
        self.rect.y = y

    def set_transparency(self, value):
        self.image = self.original_image.copy()
        alpha = value
        self.image.fill((255,255,255, alpha),None, pygame.BLEND_RGBA_MULT)

    def scale_image(self, new_size):
        self.image = pygame.transform.scale(self.image, (new_size, new_size))
        self.rect.size = (new_size, new_size)

    def collision_group(self, group):
        collision_list = pygame.sprite.spritecollideany(self, group)
        return collision_list

    def show(self):
        self.image.set_alpha(255)

    def hide(self):
        self.image.set_alpha(0)

class Wall(GameObject):
    """A class which describes the walls forming the borders of the labrynth"""

    def __init__(self, x, y):
        """Set the starting values of the attributes"""
        super().__init__(os.getcwd()+"/image/wall.png")
        super().set_position(x,y)
        self.set_transparency(1)

    def scale_image(self, new_size):
        """scale the image to a desired size

        Arguments:
        new_size -> the length in pixels of one side of the scaled image"""
        self.image = pygame.transform.scale(self.image, (new_size, new_size))
        self.original_image = pygame.transform.scale(self.original_image, (new_size, new_size))
        self.rect.size = (new_size, new_size)

class Player(GameObject):
    """A class which stores the player data

    Attributes:
    speed -> the walking speed of the Player
    inventory -> a dictionary of boolians storing what items the player has picked up
    """

    def __init__(self, x, y):
        """Set the starting values of the attributes"""
        super().__init__(os.getcwd()+"/image/player.png")
        super().set_position(x,y)
        self.speed = 1
        self.inventory = {}

    def add_to_iventory(self,item):
        """A method which adds an item into the player's inventory

        Arguments
        item -> the name of the item picked up
        Returns
        None"""
        self.inventory[item] = True

    def move_player(self, direction):
        pass

class Ping(GameObject):
    """A class which describes the ping object used for querying distance

    Attributes:
    image -> the pygame surface which stores the position of the ping
    rect -> the bounding box of the ping"""

    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([1, 1])
        # self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.center[0]
        self.rect.y = player.rect.center[1]

class NPC(GameObject):
    """A class which describes NPCs in the world

    Attributes:
    directory -> the file folder which stores the NPC data
    dialogue -> a list of the dialogue strings of the NPC
    key -> a dictionary storing the checkpoint items of the player to advance dialogue
    index_position -> a tracker to track what point the character is through their dialogue"""

    def __init__(self, directory):
        """Set the starting values of the attributes"""
        super().__init__(os.getcwd()+"/documents/NPCs/" + directory + "/image.png")
        self.directory = directory
        self.dialogue = self.load_file("dialogue")
        self.key = self.load_file("keys")
        self.index_position = 0

    def load_file(self,attribute):
        """Pull an atribute from the designated file"""
        file = open(os.getcwd()+"/documents/NPCs/" + self.directory + "/" + attribute + ".txt")
        return eval(file.read())

    def update_dialogue(self):
        """A method which handels loading the dialogue lines of the NPC"""

        #if there is a checkpoint needed for the next line of dialogue
        if index_position in self.key.keys():
            #if the player has achieved the checkpoint
            if player.inventory.contains(self.key[index_position]):
                #print the next position
                self.index_position += 1
                say_line(self.dialogue[self.index_position])

            #if the player has not achieved the checkpoint
            else:
                #repreate the previous line
                say_line(self.dialogue[self.index_position])

        #if it is the first or last dialogue line
        elif index_position == 0 or index_position == len(dialogue)-1:
            #say the first line of dialogue
            say_line(self.dialogue[self.index_position])

        #if there is a normal dialogue line
        else:
            #say the next line of dialogue
            self.index_position += 1
            say_line(self.dialogue[self.index_position])
