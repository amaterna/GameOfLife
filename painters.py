from grid import Grid
from grid import ALIVE_CELL
from grid import DEAD_CELL
from time import sleep
import pygame


class Painter:
    def draw(self, grid):
        pass

    def process_input(self):
        pass

    def update(self):
        pass


class AsciiPainter(Painter):
    def draw(self, grid):
        # sleep(0.2)
        world = grid.get_world()
        header = '_' * grid.size_x
        print(header)
        for y in range(grid.size_y):
            line = ''
            for x in range(grid.size_x):
                if world[x][y] == ALIVE_CELL:
                    line += 'X'
                else:
                    line += ' '
            print(line)


class PyGamePainter(Painter):
    def __init__(self, size_x, size_y):
        pygame.init()
        pygame.display.set_caption("Demo")
        self.cell_size = 10
        self.screen = pygame.display.set_mode((size_x*self.cell_size, size_y*self.cell_size))

    def process_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                quit()

    def draw(self, grid):
        self.screen.fill((10, 10, 10))
        sleep(0.2)
        world = grid.get_world()
        for y in range(grid.size_y):
            line = ''
            for x in range(grid.size_x):
                color = pygame.Color(0, 0, 0)
                if world[x][y] == ALIVE_CELL:
                    color = pygame.Color(255, 255, 255)

                rect = pygame.Rect(x*self.cell_size, y*self.cell_size, self.cell_size, self.cell_size)
                pygame.draw.rect(self.screen, color,
                                 rect)
            # print(line)
        pygame.display.flip()

