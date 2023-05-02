from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title = "Maze Solver"
        self.__canvas = Canvas(self.__root, width=width, height=height)
        self.__canvas.pack()
        self.__is_window_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__is_window_running = True
        while self.__is_window_running:
            self.redraw()

    def close(self):
        self.__is_window_running = False

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, point_one, point_two):
        self.point_one = point_one
        self.point_two = point_two

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.point_one.x,
            self.point_one.y,
            self.point_two.x,
            self.point_two.y,
            fill=fill_color,
            width=2,
        )
        canvas.pack()


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
