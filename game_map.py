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
        [0, 2, 1, 2, 0, 0, 0, 2, 1, 2, 0],
        [0, 2, 1, 2, 2, 2, 2, 2, 1, 2, 0],
        [0, 2, 1, 1, 1, 3, 1, 1, 1, 2, 0],
        [0, 2, 2, 2, 2, 1, 2, 2, 2, 2, 0],
        [0, 0, 0, 0, 2, 1, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0]
    ]

    return map_matrix

class GameMap():
    """Map of the game"""

    def __init__(self, current_map=sample_map()):
        """
        Initializes GameMap object

        current_map: map depicted as nested list
        """
        # map of the game in matrix form.
        self.map = current_map
        self.pixel_size = 64
        self.wall_list = self.get_walls()
        self.player = self.get_player()

    def get_walls(self):
        x = 0
        y = 0
        walls = []
        for row in self.map:
            for column in row:
                if column == 2:
                    wall = game_object.Wall(x,y)
                    wall.scale_image(self.pixel_size)
                    walls.append(wall)
                x += self.pixel_size
            x = 0
            y += self.pixel_size
        
        return walls
    
    def get_player(self):
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