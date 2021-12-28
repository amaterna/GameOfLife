import numpy as np

DEAD_CELL = 0
ALIVE_CELL = 1


class Grid:
    def __init__(self, size_x=40, size_y=10):
        self.size_x = size_x
        self.size_y = size_y
        self.world = np.zeros((size_x, size_y))

    def set_cell(self, x, y, value):
        self.world[x][y] = value

    def get_world(self):
        return self.world

    def update_world(self, world):
        self.world = world
