import pygame

class GameObject(pygame.sprite.Sprite):

    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
    
    def print_loaction(self):
        print(self.rect.center)

class Wall(GameObject):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([64,64])
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
    