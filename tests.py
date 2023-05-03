import unittest
from modules.maze import Maze
from modules.window import Window

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_with_odd_nums(self):
        num_cols = 11
        num_rows = 11
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    
    def test_maze_crete_with_window(self):
        w = Window(1024,768)
        m1 = Maze(0, 0, 8, 8, 50, 50, w)
        self.assertEqual(m1._win, w)


if __name__ == "__main__":
    unittest.main()
