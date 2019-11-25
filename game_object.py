import pygame
import os
import random

class GameObject(pygame.sprite.Sprite):

    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.original_image = self.image

    def location(self):
        return(self.rect.x, self.rect.y)

    def size(self):
        return(self.rect.size)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def draw_offset(self, screen, x, y):
        screen.blit(self.image, self.rect.move(x,y))

    def set_position(self, x, y):
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

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.getcwd()+"/image/wall.png")
        self.image = pygame.transform.rotate(self.image, random.choice([0,90,180,270]))
        self.image.set_colorkey((0,0,0))
        self.original_image = self.image
        self.set_transparency(1)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def scale_image(self, new_size):
        self.image = pygame.transform.scale(self.image, (new_size, new_size))
        self.original_image = pygame.transform.scale(self.original_image, (new_size, new_size))
        self.rect.size = (new_size, new_size)

class Player(GameObject):
    """A class which stores the player data

    Attributes:
    image -> the picture of the Player
    rect -> the bounding box of the Player
    speed -> the walking speed of the Player
    inventory -> a dictionary of boolians storing what items the player has picked up
    """

    def __init__(self, x, y):
        """Set the starting values of the attributes"""

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.getcwd()+"/image/player.png")
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
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
    image -> the picture of the npc as shown in the world
    rect -> the bounding box of the NPC
    dialogue -> a list of the dialogue strings of the NPC
    key -> a dictionary storing the checkpoint items of the player to advance dialogue
    index_position -> a tracker to track what point the character is through their dialogue"""

    def __init__(self, image, dialogue, key):
        super().__init__(image)
        self.dialogue = dialogue
        self.key = key
        self.index_position = 0

    def update_dialogue(self):
        if index_position in self.key.keys():
            if player.inventory.contains(self.key[index_position]):
                self.index_position += 1
        else:
            say_line(self.dialogue[self.index_position])
            self.index_position += 1
