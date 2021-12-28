from game_of_life import GameOfLife
from painters import AsciiPainter
from painters import PyGamePainter

if __name__ == "__main__":
    # painter = AsciiPainter()
    size_x = 40
    size_y = 30
    painter = PyGamePainter(size_x, size_y)
    game = GameOfLife(painter)
    game.run()
