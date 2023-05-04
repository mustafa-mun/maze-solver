import unittest
from modules.maze import Maze
from modules.gui import Window


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

    # def test_maze_crete_with_window(self):
    #     w = Window(1024, 768)
    #     m1 = Maze(0, 0, 8, 8, 10, 10, w)
    #     self.assertEqual(m1._win, w)

    def test_maze_break_entrance_and_exit(self):
        m1 = Maze(20, 20, 10, 10, 50, 50)
        self.assertEqual(m1._cells[0][0].has_top_wall, False)
        last_column = m1._cells[len(m1._cells) - 1]
        self.assertEqual(last_column[len(last_column) - 1].has_bottom_wall, False)

    def test_reset_cell_visit(self):
        m1 = Maze(20, 20, 10, 10, 50, 50)
        is_all_resetted = True

        for col in m1._cells:
            for cell in col:
                if cell.visited == True:
                    is_all_resetted = False
                    
        self.assertEqual(is_all_resetted, True)

if __name__ == "__main__":
    unittest.main()
