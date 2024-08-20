from unittest import TestCase

from main import is_cell_busy, point_cell


class TestTicTacToe(TestCase):

    def setUp(self):
        self.board = [['.' for _ in range(3)] for _ in range(3)]

    def test_make_check_busy_and_point_cell(self):
        result = is_cell_busy(self.board, 0, 0)
        self.assertFalse(result)

        point_cell(self.board, 0, 0, 'X')
        result = is_cell_busy(self.board, 0, 0)
        self.assertTrue(result)

