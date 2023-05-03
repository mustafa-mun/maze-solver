from modules.cell import Cell
import time


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self.__create_cells()
        self.__break_entrence_and_exit()

    def __create_cells(self):
        # populate cells
        for i in range(self.__num_cols):
            list = []
            for j in range(self.__num_rows):
                list.append(Cell(self._win))
            self._cells.append(list)
        # draw cells
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__draw_cell(i, j)

      
    def __draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self.__x1 + i * self.__cell_size_x
        y1 = self.__y1 + j * self.__cell_size_y
        x2 = x1 + self.__cell_size_x
        y2 = y1 + self.__cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self.__animate()

    def __animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def __break_entrence_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)
        last_column = self._cells[len(self._cells) - 1]
        last_column[len(last_column) - 1].has_bottom_wall = False
        self.__draw_cell(self.__num_cols - 1, self.__num_rows - 1)
