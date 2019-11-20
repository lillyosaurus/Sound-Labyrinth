import model
import pygame
import os

if __name__ == '__main__':
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    pygame.mixer.init()
    m = model.Model()
    m.run_game()
