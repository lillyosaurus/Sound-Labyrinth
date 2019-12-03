import view
import game_map as gm
import controller as c
import pygame
import visual
import game_map
import game_object

class Model:

    def __init__(self):
        #the map of the game world which stores the objects
        self.map = gm.GameMap()
        self.view = view.View(self.map)
        self.controller = c.Controller()
        self.ping_delay = 600
        self.previous_time = 0
        self.turned_on_wall = None
        self.wall_transparency = 0

        self.show_home_screen = True
        self.show_instructions = False
        self.show_credits = False
        self.game_on = False
        self.run = True

    def wall_collision_ping(self,direction,current_time):
        print('going the direction')
        ping_check = self.map.ping_from_player(direction,1)
        dist = ping_check[1]
        if current_time - self.previous_time >= self.ping_delay:
            print('updating_time')
            print(dist)
            self.previous_time = current_time
            if dist != None:
                print('performing action')
                #self.view.play_echo(round(dist),direction, self.view.audio.hollow_sound)
                self.turned_on_wall = ping_check[0]
                self.wall_transparency = 30

    def process_ping(self,direction,sight_range,current_time):
        if self.controller.ping_keys[direction]:
            print('going the direction')
            ping_check = self.map.ping_from_player(direction,sight_range)
            dist = ping_check[1]
            if current_time - self.previous_time >= self.ping_delay:
                print('updating_time')
                print(dist)
                self.previous_time = current_time
                if dist != None:
                    print('performing action')
                    self.view.play_echo(round(dist),direction, self.view.audio.hollow_sound)
                    self.turned_on_wall = ping_check[0]
                    self.wall_transparency = 30

    def show_screen(self,screen):
        """Updates boolean to display the correct screen

        The function sets all screen display booleans to false and takes the referenced display screen and sets that boolean to be true

        """
        self.show_home_screen = False
        self.show_instructions = False
        self.show_credits = False
        self.game_on = False
        if screen == 'home_screen':
            self.show_home_screen = True
        elif screen == 'instructions':
            self.show_instructions = True
        elif screen == 'credits':
            self.show_credits = True
        elif screen == 'game':
            self.game_on = True

    def run_game(self):
        #EXPLAIN
        clock = pygame.time.Clock()
        #Initializes current time object
        current_time = 0

        while self.run:
            if self.show_home_screen == True:
                self.view.update_screen('home_screen')
                self.controller.read_input()
                if self.controller.hs_keys['I']:
                    self.show_screen('instructions')
                elif self.controller.hs_keys['C']:
                    self.show_screen('credits')
                elif self.controller.hs_keys['space']:
                    self.show_screen('game')

            elif self.show_instructions == True:
                self.view.update_screen('instructions')
                self.controller.read_input()
                if self.controller.hs_keys['H']:
                    self.show_screen('home_screen')
                elif self.controller.hs_keys['space']:
                    self.show_screen('game')

            elif self.show_credits == True:
                self.view.update_screen('credits')
                self.controller.read_input()
                if self.controller.hs_keys['H']:
                    self.show_screen('home_screen')

            if self.view.visual.game_on == False:
                    self.run = False

            while self.game_on == True:
                current_time = pygame.time.get_ticks()
                #print(current_time)
                #forces the frames per second (fps) of the game to be equal to 60 fps
                clock.tick(60)

                #prevents the user from providing input while they are moving
                if self.map.at_block() == True:
                    #updates the controller-
                    self.controller.read_input()

                    #process controller inputs for pings
                    self.process_ping('front',3,current_time)
                    self.process_ping('back',3,current_time)
                    self.process_ping('right',3,current_time)
                    self.process_ping('left',3,current_time)

                #process controller inputs for moving and interacting
                speed = self.map.player.speed
                if self.controller.move_keys['north']:

                    #TODO: Extract to function in player
                    #player.move("direction")
                    self.map.player.rect.move_ip(0,-speed)
                    if self.map.player_wall_collision() != None:
                            self.map.player.rect.move_ip(0,speed)
                            self.wall_collision_ping('front',current_time)
                    """#if the player runs into an npc cause the player to interact
                    if self.map.player_NPC_collision() != None:
                            self.map.player.rect.move_ip(0,speed)
                            self.NPC_collision_ping('front',current_time)"""

                elif self.controller.move_keys['south']:

                    self.map.player.rect.move_ip(0,speed)
                    if self.map.player_wall_collision() != None:
                            self.map.player.rect.move_ip(0,-speed)
                            self.wall_collision_ping('back',current_time)

                elif self.controller.move_keys['west']:

                    self.map.player.rect.move_ip(-speed,0)
                    if self.map.player_wall_collision() != None:
                            self.map.player.rect.move_ip(speed,0)
                            self.wall_collision_ping('left',current_time)

                elif self.controller.move_keys['east']:

                    self.map.player.rect.move_ip(speed,0)
                    if self.map.player_wall_collision() != None:
                            self.map.player.rect.move_ip(-speed,0)
                            self.wall_collision_ping('right',current_time)

                if self.turned_on_wall != None and self.wall_transparency >=0:
                    self.turned_on_wall.set_transparency(1 + self.wall_transparency * 8)
                    self.wall_transparency -= 1
                    print('reduce wall transparency' + str(self.wall_transparency))
                #update visuals
                self.view.update_screen('game')
                if self.view.visual.game_on == False:
                    self.game_on = False
                    self.run = False


if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init()
    m = Model()
    m.run_game()
