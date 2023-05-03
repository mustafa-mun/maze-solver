from modules.point import Point
from modules.line import Line


class Cell:
    def __init__(self, win = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = None
        self.__x2 = None
        self.__y1 = None
        self.__y2 = None
        self.__win = win

    def __draw_handler(self, wall, point_one, point_two):
        if wall:
            line = Line(point_one, point_two)
            self.__win.draw_line(line, "black")

    def draw(self, x1, x2, y1, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        # handle left wall
        self.__draw_handler(
            self.has_left_wall, Point(self.__x1, self.__y1), Point(self.__x1, self.__y2)
        )
        # handle right wall
        self.__draw_handler(
            self.has_right_wall,
            Point(self.__x2, self.__y1),
            Point(self.__x2, self.__y2),
        )
        # handle bottom wall
        self.__draw_handler(
            self.has_bottom_wall,
            Point(self.__x1, self.__y1),
            Point(self.__x2, self.__y1),
        )
        # handle top wall
        self.__draw_handler(
            self.has_top_wall, Point(self.__x1, self.__y2), Point(self.__x2, self.__y2)
        )

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
            self.__win.draw_line(line, fill_color)
            line = Line(Point(to_x_mid, to_y_mid), Point(to_cell.__x2, to_y_mid))
            self.__win.draw_line(line, fill_color)

        # moving right
        elif self.__x1 < to_cell.__x1:
            line = Line(Point(x_mid, y_mid), Point(self.__x2, y_mid))
            self.__win.draw_line(line, fill_color)
            line = Line(Point(to_cell.__x1, to_y_mid), Point(to_x_mid, to_y_mid))
            self.__win.draw_line(line, fill_color)

        # moving up
        elif self.__y1 > to_cell.__y1:
            line = Line(Point(x_mid, y_mid), Point(x_mid, self.__y1))
            self.__win.draw_line(line, fill_color)
            line = Line(Point(to_x_mid, to_cell.__y2), Point(to_x_mid, to_y_mid))
            self.__win.draw_line(line, fill_color)

        # moving down
        elif self.__y1 < to_cell.__y1:
            line = Line(Point(x_mid, y_mid), Point(x_mid, self.__y2))
            self.__win.draw_line(line, fill_color)
            line = Line(Point(to_x_mid, to_y_mid), Point(to_x_mid, to_cell.__y1))
            self.__win.draw_line(line, fill_color)


