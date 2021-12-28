from grid import Grid
from grid import ALIVE_CELL
from grid import DEAD_CELL

import numpy as np
import random


class GameOfLife:

    def __init__(self, painter, size_x=40, size_y=30):
        self.grid = Grid(size_x, size_y)
        # self.grid.set_cell(0, 0, ALIVE_CELL)
        # self.grid.set_cell(0, 1, ALIVE_CELL)
        # self.grid.set_cell(1, 0, ALIVE_CELL)

        # self.grid.set_cell(6, 6, ALIVE_CELL)
        # self.grid.set_cell(7, 6, ALIVE_CELL)
        # self.grid.set_cell(8, 6, ALIVE_CELL)
        #
        # self.grid.set_cell(6, 7, ALIVE_CELL)
        #
        # self.grid.set_cell(7, 8, ALIVE_CELL)

        # self.grid.set_cell(2, 7, ALIVE_CELL)
        # self.grid.set_cell(3, 7, ALIVE_CELL)
        # self.grid.set_cell(4, 7, ALIVE_CELL)

        for i in range(200):
            x = random.randint(0, size_x-1)
            y = random.randint(0, size_y-1)
            self.grid.set_cell(x, y, ALIVE_CELL)

        self.painter = painter
        self.neighborhood = np.array([[-1, 1],  [0, 1],  [1, 1],
                                     [-1, 0],  [1, 0],
                                     [-1, -1], [0, -1], [1, -1]])

        self.neighborhood = np.array([[-3, 0], [-2, 0], [-1, 0], [1, 0], [2, 0], [3, 0]])

        # self.neighborhood = np.array([[0, 1], [-1, 0], [1, 0], [0, -1]])

        self.painter.draw(self.grid)

    def update(self):
        world = self.grid.get_world()
        size_x = self.grid.size_x
        size_y = self.grid.size_y
        new_world = np.zeros((size_x, size_y))

        for x in range(self.grid.size_x):
            for y in range(self.grid.size_y):
                alive_counter = 0
                dead_counter = 0
                for neighbour in self.neighborhood:
                    x_n = neighbour[0]
                    y_n = neighbour[1]
                    neighbour_x = x + x_n
                    neighbour_y = y + y_n
                    if neighbour_x >= size_x:
                        neighbour_x -= size_x
                    elif neighbour_x <= -1:
                        neighbour_x += size_x - 1

                    if neighbour_y >= size_y:
                        neighbour_y -= size_y
                    elif neighbour_y <= -1:
                        neighbour_y += size_y - 1

                    state = world[neighbour_x][neighbour_y]
                    if state == ALIVE_CELL:
                        alive_counter += 1
                current_state = world[x][y]

                # print(f'({x}:{y}) curr_state: {current_state} {alive_counter}')

                if current_state == DEAD_CELL and alive_counter == 3:
                    new_world[x][y] = ALIVE_CELL
                elif current_state == ALIVE_CELL:
                    if alive_counter == 2 or alive_counter == 3:
                        new_world[x][y] = ALIVE_CELL
                    else:
                        new_world[x][y] = DEAD_CELL

        self.grid.update_world(new_world)
        self.painter.draw(self.grid)

    def run(self):
        while True:
            self.painter.process_input()
            self.update()
