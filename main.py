from modules.window import Window
from modules.cell import Cell
from modules.maze import Maze


def main():
    win = Window(800, 600)
    maze = Maze(5, 5, 10, 10, 75, 75, win)
    win.wait_for_close()


main()
