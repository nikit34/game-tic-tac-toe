from unittest import TestCase

from main import is_cell_busy, point_cell, check_winner


class TestTicTacToe(TestCase):

    def setUp(self):
        self.board = [['.' for _ in range(3)] for _ in range(3)]

    def test_make_check_busy_and_point_cell(self):
        result = is_cell_busy(self.board, 0, 0)
        self.assertFalse(result)

        point_cell(self.board, 0, 0, 'X')
        result = is_cell_busy(self.board, 0, 0)
        self.assertTrue(result)

    def test_check_winner_rows(self):
        self.board[0] = ['X', 'X', 'X']
        self.assertTrue(check_winner(self.board, 'X'))

        self.board[0] = ['X', 'O', 'X']
        self.assertFalse(check_winner(self.board, 'X'))

    def test_check_winner_columns(self):
        self.board = [
            ['X', '.', '.'],
            ['X', '.', '.'],
            ['X', '.', '.']
        ]
        self.assertTrue(check_winner(self.board, 'X'))

        self.board = [
            ['X', '.', '.'],
            ['O', '.', '.'],
            ['X', '.', '.']]
        self.assertFalse(check_winner(self.board, 'X'))
