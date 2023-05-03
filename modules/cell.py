from modules.gui import Point, Line


class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = None
        self.__x2 = None
        self.__y1 = None
        self.__y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        # handle left wall
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, "white")
        # handle right wall
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, "white")
        # handle top wall
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, "white")
        # handle bottom wall
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, "white")

    def draw_move(self, to_cell, undo=False):
        # change this first
        fill_color = None
        if undo:
            fill_color = "gray"
        else:
            fill_color = "red"

        x_mid = (self.__x1 + self.__x2) / 2
        y_mid = (self.__y1 + self.__y2) / 2

        to_x_mid = (to_cell.__x1 + to_cell.__x2) / 2
        to_y_mid = (to_cell.__y1 + to_cell.__y2) / 2

        # moving left
        if self.__x1 > to_cell.__x1:
            line = Line(Point(self.__x1, y_mid), Point(x_mid, y_mid))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_x_mid, to_y_mid), Point(to_cell.__x2, to_y_mid))
            self._win.draw_line(line, fill_color)

        # moving right
        elif self.__x1 < to_cell.__x1:
            line = Line(Point(x_mid, y_mid), Point(self.__x2, y_mid))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_cell.__x1, to_y_mid), Point(to_x_mid, to_y_mid))
            self._win.draw_line(line, fill_color)

        # moving up
        elif self.__y1 > to_cell.__y1:
            line = Line(Point(x_mid, y_mid), Point(x_mid, self.__y1))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_x_mid, to_cell.__y2), Point(to_x_mid, to_y_mid))
            self._win.draw_line(line, fill_color)

        # moving down
        elif self.__y1 < to_cell.__y1:
            line = Line(Point(x_mid, y_mid), Point(x_mid, self.__y2))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_x_mid, to_y_mid), Point(to_x_mid, to_cell.__y1))
            self._win.draw_line(line, fill_color)
