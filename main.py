import pygame

class Map:
    """A class which stores the information about the objects on the map"""
    def __init__(w,h):
        self.width = w
        self.height = h

class Model:

    def __init__(w,h):
        self.map = Map(w,h)
        self.view = View(self.map)
        self.controller = Controller()


class View:

    def __init__(map):
        self.map = map

class Controller:
    pass
