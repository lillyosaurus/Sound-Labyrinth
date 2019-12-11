import view
import game_map as gm
import controller as c
import pygame
import visual
import game_map
import game_object
import pyttsx3

class Model:
    """
    The class used to display the game on to a screen.

    Attributes:
    map -> GameMap object with all required objects to play the game
    view -> View object with required objects to display visuals and play audio
    controller -> Controller object with functions for interpreting key presses
    ping_delay -> integer value for milliseconds to wait before checking for a new ping
    footstep_delay -> integer value for milliseconds to wait before playing next footstep sound
    current_time -> current time in milliseconds
    previous_time -> time in milliseconds for previous ping
    footstep_previous_time -> time in milliseconds for previous footstep
    footstep_count -> counter to track which audio file to play for footsteps
    animation_step -> counter to track animation of moving feet
    turned_on_wall ->
    turned_on_NPC ->
    wall_transparency ->
    NPC_transparency ->
    audio_loop -> boolean for reading text on the screen
    show_home_screen -> boolean for displaying the home screen
    show_instructions -> boolean for displaying the instructions
    show_credits -> boolean for displaying the credits
    game_on -> boolean to determine whether to display the game
    run -> boolean for running the game
    """

    def __init__(self):
        """Initalize the Model class with default variable values"""
        self.map = gm.GameMap()
        self.view = view.View(self.map)
        self.controller = c.Controller()

        self.ping_delay = 600
        self.footstep_delay = 100
        self.current_time = 0
        self.previous_time = 0
        self.footstep_previous_time = 0
        self.footstep_count = 0
        self.animation_step = 0

        self.turned_on_wall = None
        self.turned_on_NPC = None
        self.wall_transparency = 0
        self.NPC_transparency = 0

        self.audio_loop = True
        self.show_home_screen = True
        self.show_instructions = False
        self.show_credits = False
        self.game_on = False
        self.run = True

    def footstep_audio(self):
        """Call function to play footstep sound
        """
        self.view.play_footsteps(self.current_time,self.footstep_previous_time,self.footstep_delay,self.footstep_count)

    def wall_collision_ping(self,direction):
        """Pings wall when a player runs into it

        This function takes a direction of ping and sight range and displays the
        wall at the correct distance and plays the sound at the correct volume

        Key Arguments:
            direction -> string indicating direction of ping
        Return values: None
        """

        ping_check = self.map.ping_from_player(direction,1)
        dist = ping_check[1]
        if self.current_time - self.previous_time >= self.ping_delay:
            self.previous_time = self.current_time
            if dist != None:
                self.turned_on_wall = ping_check[0]
                self.wall_transparency = 30

    def NPC_collision_ping(self,direction):
        """Pings NPC when a player runs into it

        Key Arguments:
            direction -> string indicating direction of ping
        Return values: None
        """
        ping_check = self.map.ping_from_player(direction,1)
        dist = ping_check[1]
        if self.current_time - self.previous_time >= self.ping_delay:
            self.previous_time = self.current_time
            if dist != None:
                self.turned_on_NPC = ping_check[0]
                self.NPC_transparency = 30

    def process_ping(self,direction,sight_range):
        """Processes ping

        This function takes a direction of ping and sight range and displays the
        wall at the correct distance and plays the sound at the correct volume

        Key Arguments:
            direction -> string indicating direction of ping
            sight_range -> integer value for number of blocks visible
        Return values: None
        """
        if self.controller.ping_keys[direction]:
            ping_check = self.map.ping_from_player(direction,sight_range)
            dist = ping_check[1]
            if self.current_time - self.previous_time >= self.ping_delay:
                self.previous_time = self.current_time
                if dist != None:
                    self.view.play_echo(round(dist),direction, self.view.audio.hollow_sound)
                    self.turned_on_wall = ping_check[0]
                    self.wall_transparency = 30
                    self.turned_on_NPC = ping_check[0]
                    self.NPC_transparency = 30

    def show_screen(self,screen):
        """Updates boolean to display the correct screen

        The function sets all screen display booleans to false and takes the
        referenced display screen and sets that boolean to be true. It also
        resets the audio loop to read the screen when switched.

        Key Arguments:
            screen -> string indicating which screen to display
        Return values: None
        """
        self.audio_loop = True

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

    def check_for_change_screens(self,instruct,home,cred,game):
        """Sets which key presses to look for and switches screen if keypress detected

        Key Arguments:
            instruct-> boolean for looking for key press for instruction page
            home -> boolean for looking for key press for home screen
            cred -> boolean for looking for key press for credits page
            game -> boolean for looking for key press for game
        Return values: None
        """
        self.controller.read_input()
        if instruct == True:
            if self.controller.hs_keys['I']:
                self.show_screen('instructions')
        if home == True:
            if self.controller.hs_keys['H']:
                self.show_screen('home_screen')
        if cred == True:
            if self.controller.hs_keys['C']:
                self.show_screen('credits')
        if game == True:
            if self.controller.hs_keys['space']:
                self.show_screen('game')


    def run_game(self):
        """Run game
        """
        #Create clock object
        clock = pygame.time.Clock()

        #Initializes audio engine for text to speech
        audio_engine = pyttsx3.init()
        audio_engine.setProperty('rate',200)
        audio_engine.setProperty('rate',0.9)
        audio_engine.setProperty('voice', 'english+f1')


        while self.run:

            #Navigates home, instruction and credit pages
            if self.show_home_screen == True:
                self.view.update_screen('home_screen')
                if self.audio_loop == True:
                    #self.view.audio.home_screen_audio(audio_engine)
                    self.audio_loop = False
                self.check_for_change_screens(instruct=True, home=False, cred=True, game=True)
            elif self.show_instructions == True:
                self.view.update_screen('instructions')
                if self.audio_loop == True:
                    #self.view.audio.instruction_page_audio(audio_engine)
                    self.audio_loop = False
                self.check_for_change_screens(instruct=False, home=True, cred=True, game=True)
            elif self.show_credits == True:
                self.view.update_screen('credits')
                if self.audio_loop == True:
                    #self.view.audio.credits_page_audio(audio_engine)
                    self.audio_loop = False
                self.check_for_change_screens(instruct=False, home=True, cred=False, game=False)


            #if self.view.visual.game_on == False:
            #self.run = False

            while self.game_on == True:
                self.current_time = pygame.time.get_ticks()
                #printself.current_time)
                #forces the frames per second (fps) of the game to be equal to 60 fps
                clock.tick(60)

                if self.animation_step == 16:
                    self.animation_step = 0

                #prevents the user from providing input while they are moving
                if self.map.at_block() == True:
                    #updates the controller-
                    self.controller.read_input()

                    #process controller inputs for pings
                    self.process_ping('front',3)
                    self.process_ping('back',3)
                    self.process_ping('right',3)
                    self.process_ping('left',3)

                #process controller inputs for moving and interacting
                speed = self.map.player.speed
                if self.controller.move_keys['north']:

                    #TODO: Extract to function in player
                    #player.move("direction")
                    self.map.player.rect.move_ip(0,-speed)
                    if self.map.player_wall_collision() != None:
                            self.map.player.rect.move_ip(0,speed)
                            self.wall_collision_ping('front')
                    elif self.map.player_NPC_collision() != None:
                            self.map.player.rect.move_ip(0,speed)
                            self.NPC_collision_ping('front')
                    else:
                        self.animation_step += 1
                        if self.animation_step % 2 == 0:
                            self.map.player.set_image('north',int(self.animation_step/2))
                            self.footstep_audio()

                    """#if the player runs into an npc cause the player to interact
                    if self.map.player_NPC_collision() != None:
                            self.map.player.rect.move_ip(0,speed)
                            self.NPC_collision_ping('front')"""

                elif self.controller.move_keys['south']:

                    self.map.player.rect.move_ip(0,speed)
                    if self.map.player_wall_collision() != None:
                            self.map.player.rect.move_ip(0,-speed)
                            self.wall_collision_ping('back')
                    elif self.map.player_NPC_collision() != None:
                            self.map.player.rect.move_ip(0,speed)
                            self.NPC_collision_ping('back')
                    else:
                        self.animation_step += 1
                        if self.animation_step % 2 == 0:
                            self.map.player.set_image('south',int(self.animation_step/2))
                            self.footstep_audio()

                elif self.controller.move_keys['west']:

                    self.map.player.rect.move_ip(-speed,0)
                    if self.map.player_wall_collision() != None:
                            self.map.player.rect.move_ip(speed,0)
                            self.wall_collision_ping('left')
                    elif self.map.player_NPC_collision() != None:
                            self.map.player.rect.move_ip(0,speed)
                            self.NPC_collision_ping('left')
                    else:
                        self.animation_step += 1
                        if self.animation_step % 2 == 0:
                            self.map.player.set_image('west',int(self.animation_step/2))
                            self.footstep_audio()

                elif self.controller.move_keys['east']:

                    self.map.player.rect.move_ip(speed,0)
                    if self.map.player_wall_collision() != None:
                            self.map.player.rect.move_ip(-speed,0)
                            self.wall_collision_ping('right')
                    elif self.map.player_NPC_collision() != None:
                            self.map.player.rect.move_ip(0,speed)
                            self.NPC_collision_ping('right')
                    else:
                        self.animation_step += 1
                        if self.animation_step % 2 == 0:
                            self.map.player.set_image('east',int(self.animation_step/2))
                            self.footstep_audio()

                if self.turned_on_wall != None and self.wall_transparency >=0:
                    self.turned_on_wall.set_transparency(1 + self.wall_transparency * 8)
                    #self.wall_transparency -= 1
                if self.turned_on_NPC != None and self.NPC_transparency >=0:
                    self.turned_on_NPC.set_transparency(1 + self.NPC_transparency * 8)
                    #self.NPC_transparency -= 1

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
