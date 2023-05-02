from modules.window import Window
from modules.cell import Cell

def main():
    win = Window(800, 600)
    cell_one = Cell(True, False, True, True, 10, 100, 50, 100, win)
    cell_one.draw()

    cell_two = Cell(False, True, True, True, 300, 500, 200, 400, win)
    cell_two.draw()

    cell_three = Cell(True, True, False, True, 200, 400, 50, 150, win)
    cell_three.draw()

    cell_one.draw_move(cell_two)
    cell_three.draw_move(cell_one)
    cell_three.draw_move(cell_two)
    win.wait_for_close()


main()
