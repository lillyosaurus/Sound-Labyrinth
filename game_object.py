import pygame
import os

class GameObject(pygame.sprite.Sprite):

    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

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
        self.image.set_alpha(value)

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
        self.image = pygame.image.load(os.getcwd()+"/image/post_processed/wall.png")
        self.image.set_colorkey((0,0,0))
        self.image.set_alpha(100)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Player(GameObject):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.getcwd()+"/image/post_processed/player.png")
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Ping(GameObject):

    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([1, 1])
        # self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.center[0]
        self.rect.y = player.rect.center[1]
