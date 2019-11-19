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
        self.wall_group = pygame.sprite.Group()
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
                    self.wall_group.add(wall)
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

    def player_wall_collision(self):
        return self.player.collision_group(self.wall_group)

    #TODO: return distance and wall hit

    def ping_from_player(self, direction, limit):
        ping = game_object.Ping(self.player)
        pixel_limit = self.pixel_size * limit
        x = 0
        y = 0
        offset = 0
        if direction == 'up':
            x = 0
            y = -1
        elif direction == 'down':
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
                return blocks_away

        return None

    def at_block(self):
        if self.player.rect.x % self.pixel_size == 0:
            if self.player.rect.y % self.pixel_size == 0:
                return True
        return False
