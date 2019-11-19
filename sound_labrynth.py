import model
import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init()
    m = model.Model()
    m.run_game()
