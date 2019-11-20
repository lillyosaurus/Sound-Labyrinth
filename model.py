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
        #the map of the game world which stores the objects
        self.map = gm.GameMap()
        self.view = view.View(self.map)
        self.controller = c.Controller()


    def run_game(self):

        #EXPLAIN
        clock = pygame.time.Clock()


        #Stores which direction was just pinged so you cant ping twice in the same direction
        previous_ping = None

        while(self.view.on == True):

            #forces the frames per second (fps) of the game to be equal to 60 fps
            clock.tick(60)

            #prevents the user from providing input while they are moving
            if self.map.at_block() == True:

                #updates the controller
                self.controller.read_input()

                #process controller inputs for pings
                if self.controller.ping_keys['front']:

                    #TODO: EXtract to function in Model
                    #process_ping('direction',sight_range,clock)
                    #   do visual and audio only when allowed after 1 second
                    #   return None
                    dist = self.map.ping_from_player('up',3)
                    if previous_ping != 'up':
                        previous_ping = 'up'
                        if dist != None:
                            self.view.play_echo(round(dist),'up', self.view.audio.hollow_sound)

                elif self.controller.ping_keys['right']:

                    dist = self.map.ping_from_player('right',3)
                    if previous_ping != 'right':
                        previous_ping = 'right'
                        if dist != None:
                            self.view.play_echo(round(dist),'right', self.view.audio.hollow_sound)

                elif self.controller.ping_keys['left']:

                    dist = self.map.ping_from_player('left',3)
                    if previous_ping != 'left':
                        previous_ping = 'left'
                        if dist != None:
                            self.view.play_echo(round(dist),'left', self.view.audio.hollow_sound)

                elif self.controller.ping_keys['back']:

                    dist = self.map.ping_from_player('down',3)
                    if previous_ping != 'down':
                        previous_ping = 'down'
                        if dist != None:
                            self.view.play_echo(round(dist),'down', self.view.audio.hollow_sound)

            #process controller inputs for moving
            speed = self.map.player.speed
            if self.controller.move_keys['north']:

                #TODO: Extract to function in player
                #player.move("direction")
                self.map.player.rect.move_ip(0,-speed)
                if self.map.player_wall_collision() != None:
                        self.map.player.rect.move_ip(0,speed)

            elif self.controller.move_keys['south']:

                self.map.player.rect.move_ip(0,speed)
                if self.map.player_wall_collision() != None:
                        self.map.player.rect.move_ip(0,-speed)

            elif self.controller.move_keys['west']:

                self.map.player.rect.move_ip(-speed,0)
                if self.map.player_wall_collision() != None:
                        self.map.player.rect.move_ip(speed,0)

            elif self.controller.move_keys['east']:

                self.map.player.rect.move_ip(speed,0)
                if self.map.player_wall_collision() != None:
                        self.map.player.rect.move_ip(-speed,0)

            #update visuals
            self.view.update_screen()


if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init()
    m = Model()
    m.run_game()
