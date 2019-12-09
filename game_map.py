import pygame
import game_object

def sample_map():
    """
    Sample map for the game
    """
    map_matrix = [
        [0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2],
        [0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2],
        [0, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2],
        [0, 0, 0, 2, 1, 1, 1, 1, 1, 2, 0],
        [0, 2, 2, 2, 2, 2, 2, 2, 1, 2, 0],
        [0, 2, 1, 2, 0, 0, 0, 2, 1, 2, 0],
        [0, 2, 1, 2, 2, 2, 2, 2, 1, 2, 0],
        [0, 2, 1, 2, 2, 4, 2, 2, 1, 2, 0],
        [0, 2, 1, 1, 1, 1, 1, 1, 1, 2, 0],
        [0, 2, 2, 2, 2, 1, 2, 2, 2, 2, 0],
        [0, 0, 0, 0, 2, 3, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0]
    ]

    return map_matrix

class GameMap():
    """
    The class which provides the map for the game with all needed objects

    Attributes:
    map -> map of the game in nested list
    pixel_size -> length of each block that builds the game on the screen. All images are scaled to this size.
    wall_group -> pygame Group that includes all the Wall object in the game
    wall_list -> list of all Wall objects 
    player -> Player object
    """

    def __init__(self, current_map=sample_map()):
        """
        Initializes GameMap object

        current_map: map depicted as nested list
        """
        self.map = current_map
        self.pixel_size = 128
        self.wall_group = pygame.sprite.Group()
        self.NPC_group = pygame.sprite.Group()
        
        #a list of the NPCs and their directories
        self.NPC_dict = {4:"reaper"}
        
        self.wall_list = self.get_walls()
        self.NPC_list = self.get_NPCs()
        self.player = self.get_player()
        self.player.speed = self.pixel_size/16
        

    def get_walls(self):
        """
        Figure out the location of each wall and creates Wall objects.
        Number 2 in nested list indicates a wall.
        Rescale all the images so that it can fit the pixel_size attribute.

        Return:
        [Wall object, Wall object, ....] -> list of Wall objects
        """
        x = 0
        y = 0
        walls = []
        for row in self.map:
            for column in row:
                if column == 2:
                    wall = game_object.Wall(x,y)
                    wall.scale_image(self.pixel_size)
                    self.wall_group.add(wall)
                    walls.append(wall)
                x += self.pixel_size
            x = 0
            y += self.pixel_size

        return walls

    def get_player(self):
        """
        Figure out the location of player and create Player object.
        Number 3 in nested list indicates a player.
        Rescale all the images so that it can fit the pixel_size attribute.

        Return:
        Player object
        """
        x = 0
        y = 0
        for row in self.map:
            for column in row:
                if column == 3:
                    player = game_object.Player(x,y)
                    player.scale_image(self.pixel_size)
                x += self.pixel_size
            x = 0
            y += self.pixel_size

        return player
    
    def get_NPCs(self):
        """
        Figure out the location of each wall and creates Wall objects.
        Number 4 in nested list indicates a NPC.
        Rescale all the images so that it can fit the pixel_size attribute.

        Return:
        [NPC object, NPC object, ....] -> list of NPC objects
        """
        x = 0
        y = 0
        NPCs = []
        for row in self.map:
            for column in row:
                if column >= 4:
                    NPC = game_object.NPC(x,y,self.NPC_dict[column])
                    NPC.scale_image(self.pixel_size)
                    self.NPC_group.add(NPC)
                    NPCs.append(NPC)
                x += self.pixel_size
            x = 0
            y += self.pixel_size

        return NPCs
    def player_wall_collision(self):
        """
        Check whether the Player object is colliding with any Wall object

        Return:
        boolean -> True or False
        """
        return self.player.collision_group(self.wall_group)

    def player_NPC_collision(self):
        """
        Check whether the Player object is colliding with any NPC object

        Return:
        boolian -> True or False
        """
        return self.player.collision_group(self.NPC_group)

    def ping_from_player(self, direction, limit):
        """
        Create a Ping object to check the distance between Player and closest Wall or NPC object in range. 

        Arguments:
        direction-> the direction to send the Ping object
        limit -> limit in blocks the maximum distance ping can travel

        Return:
        [int, Object] -> returns the distance in int, and the Colliding wall or NPC object. Returns [None, None] if nothing was hit. 
        """
        ping = game_object.Ping(self.player)
        pixel_limit = self.pixel_size * limit
        x = 0
        y = 0
        offset = 0
        return_list = []
        if direction == 'front':
            x = 0
            y = -1
        elif direction == 'back':
            x = 0
            y = 1
            offset = 1
        elif direction == 'left':
            x = -1
            y = 0
        elif direction == 'right':
            x = 1
            y = 0
            offset = 1

        for i in range(pixel_limit):
            ping.rect.move_ip(x, y)
            ping_wall = ping.collision_group(self.wall_group)
            
            if ping_wall != None:
                blocks_away = (i + offset + self.pixel_size/2)/self.pixel_size
                ping_wall.image.set_alpha(255)
                return_list.append(ping_wall)
                return_list.append(blocks_away)
                return return_list
            ping_NPC = ping.collision_group(self.NPC_group)
            if ping_NPC != None:
                blocks_away = (i + offset + self.pixel_size/2)/self.pixel_size
                ping_NPC.image.set_alpha(255)
                return_list.append(ping_NPC)
                return_list.append(blocks_away)
                return return_list

        return [None,None]

    def at_block(self):
        """
        Check whether the Player object is in the middle of the block

        Return:
        boolean -> True or False
        """
        if self.player.rect.x % self.pixel_size == 0:
            if self.player.rect.y % self.pixel_size == 0:
                return True
        return False

    def intro_pages(self, title = True, instructions = False, info = False):

        if title == True:
            # draw title screen
            pass
        elif instructions == True:
            # draw instruction page
            pass
        elif info == True:
            #draw info screen
            pass
