from modules.point import Point
from modules.line import Line

class Cell:
    def __init__(
        self,
        has_left_wall,
        has_right_wall,
        has_top_wall,
        has_bottom_wall,
        x1,
        x2,
        y1,
        y2,
        win,
    ):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        self.__win = win

    def __draw_handler(self, wall, point_one, point_two):
        if wall:
            line = Line(point_one, point_two)
            self.__win.draw_line(line, "black")

    def draw(self):
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
        color = None
        if undo:
            color = "gray"
        else:
            color = "red"

        center_one_x = (self.__x1 + self.__x2) / 2
        center_one_y = (self.__y1 + self.__y2) / 2

        center_two_x = (to_cell.__x1 + to_cell.__x2) / 2
        center_two_y = (to_cell.__y1 + to_cell.__y2) / 2

        point_one = Point(center_one_x, center_one_y)
        point_two = Point(center_two_x, center_two_y)

        line = Line(point_one, point_two)
        self.__win.draw_line(line, color)