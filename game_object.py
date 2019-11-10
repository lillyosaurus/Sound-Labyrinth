import pygame
import os

class GameObject(pygame.sprite.Sprite):

    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
    
    def print_loaction(self):
        print(self.rect.x)
    
    def print_size(self):
        print(self.rect.size)
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    def draw_offset(self, screen, x, y):
        screen.blit(self.image, self.rect.move(x,y))
    
    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y
    
    def scale_image(self, new_size):
        self.image = pygame.transform.scale(self.image, (new_size, new_size))

class Wall(GameObject):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.getcwd()+"/image/test_tile.png")
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Player(GameObject):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.getcwd()+"/image/test_player.png")
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
