"""TODO:

fix bug with multiple walls displaying (Sungyu)
    maybe make a wall hide all the other walls when pinged

display controlls information/ instructions (Kyle)

remove delay on sound pings (kyle)
    please do not use sleep()

Build speach synthesizer (kyle)

Build function for npc dialogue (Sungyu)
def speach("string")
    play voice synthesizer
    display text
    return none

Make NPC class (Tim)

Build introductory NPC of the grim reaper to introduce you to the world and your situation (Tim)

Build introductory level design for level(Tim)
"""

import model
import pygame
import os
import game_object as go

if __name__ == '__main__':
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    pygame.mixer.init()
    m = model.Model()
    m.run_game()
