from modules.window import Window
from modules.cell import Cell
from modules.maze import Maze


def main():
    win = Window(800, 600)
    maze = Maze(20, 20, 3, 3, 50, 50, win)
    win.wait_for_close()


main()
