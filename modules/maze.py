from modules.cell import Cell
import time


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []
        self.__x1_temp = x1  # this needs a better solution
        self.__y1_temp = y1  # this needs a better solution
        self.__create_cells()

    def __animate(self):
        if self.__win is None:
            return
        self.__win.redraw()
        time.sleep(0.05)

    def __draw_cell(self, i, j):
        if self.__win is None:
            return
        x1 = self.__x1 + i * self.__cell_size_x
        y1 = self.__y1 + j * self.__cell_size_y
        x2 = x1 + self.__cell_size_x
        y2 = y1 + self.__cell_size_y
        self.__cells[i][j].draw(x1, y1, x2, y2)
        self.__animate()

    def __create_cells(self):
        # create 2d cell list
        for i in range(self.__num_cols):
            list = []
            for j in range(self.__num_rows):
                list.append(Cell(self.__win))
            self.__cells.append(list)

        # draw cells
        for i in range(len(self.__cells)):
            for j in range(len(self.__cells)):
                self.__draw_cell(i, j)
            self.__y1 = self.__y1_temp
            self.__x1 = self.__x1_temp
