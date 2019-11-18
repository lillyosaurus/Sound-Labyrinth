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
        #self.audio = audio.Audio()
    def run_game(self):

        while(self.view.on == True):
            self.controller.read_input()
            count = 0
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
            if self.controller.ping_keys['front']:
                dist = self.current_map.ping_from_player('up',3)
                if dist != None:
                    self.view.play_echo(round(dist),'up', self.view.audio.hollow_sound)
            if self.controller.ping_keys['right']:
                dist = self.current_map.ping_from_player('right',3)
                if dist != None and count == 0:
                    print(count)
                    count +=1
                    print(count)
                    self.view.play_echo(round(dist),'right', self.view.audio.hollow_sound)
            if self.controller.ping_keys['left']:
                dist = self.current_map.ping_from_player('left',3)
                if dist != None:
                    self.view.play_echo(round(dist),'right', self.view.audio.hollow_sound)
            if self.controller.ping_keys['back']:
                dist = self.current_map.ping_from_player('down',3)
                if dist != None:
                    self.view.play_echo(round(dist),'right', self.view.audio.hollow_sound)

            self.view.update_screen()


if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init()
    m = Model()
    m.run_game()
