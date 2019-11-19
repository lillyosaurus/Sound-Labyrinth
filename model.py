import view
import game_map as gm
import controller as c
import pygame
import visual
import game_map
import game_object
#import audio
#from time import sleep
#import math

class Model:

    def __init__(self):
        self.current_map = gm.GameMap()
        self.view = view.View(self.current_map)
        self.controller = c.Controller()
    def run_game(self):
        clock = pygame.time.Clock()
        count = 0
        previous_ping = None
        while(self.view.on == True):
            clock.tick(300)
            self.current_map.player.print_loaction()
            if self.current_map.at_block() == True:
                self.controller.read_input()
            #process controller inputs for moving
            if self.controller.move_keys['north']:
                self.current_map.player.rect.move_ip(0,-1)
                if self.current_map.player_wall_collision() != None:
                        self.current_map.player.rect.move_ip(0,1)
            if self.controller.move_keys['south']:
                self.current_map.player.rect.move_ip(0,1)
                if self.current_map.player_wall_collision() != None:
                        self.current_map.player.rect.move_ip(0,-1)
            if self.controller.move_keys['west']:
                self.current_map.player.rect.move_ip(-1,0)
                if self.current_map.player_wall_collision() != None:
                        self.current_map.player.rect.move_ip(1,0)
            if self.controller.move_keys['east']:
                self.current_map.player.rect.move_ip(1,0)
                if self.current_map.player_wall_collision() != None:
                        self.current_map.player.rect.move_ip(-1,0)
            #process controller inputs for pings
            if self.current_map.at_block() == True:
                if self.controller.ping_keys['front']:
                    dist = self.current_map.ping_from_player('up',3)
                    print(count)
                    if previous_ping != 'up':
                        previous_ping = 'up'
                        if dist != None:
                            self.view.play_echo(round(dist),'up', self.view.audio.hollow_sound)
                if self.controller.ping_keys['right']:
                    dist = self.current_map.ping_from_player('right',3)
                    if previous_ping != 'right':
                        previous_ping = 'right'
                        if dist != None:
                            self.view.play_echo(round(dist),'right', self.view.audio.hollow_sound)
                if self.controller.ping_keys['left']:
                    dist = self.current_map.ping_from_player('left',3)
                    if previous_ping != 'left':
                        previous_ping = 'left'
                        if dist != None:
                            self.view.play_echo(round(dist),'left', self.view.audio.hollow_sound)
                if self.controller.ping_keys['back']:
                    dist = self.current_map.ping_from_player('down',3)
                    if previous_ping != 'down':
                        previous_ping = 'down'
                        if dist != None:
                            self.view.play_echo(round(dist),'down', self.view.audio.hollow_sound)

            self.view.update_screen()
            for walls in self.current_map.wall_list:
                walls.image.set_alpha(1)

            #print(previous_ping)


if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init()
    m = Model()
    m.run_game()
