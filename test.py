from unittest import TestCase

from main import (
    is_cell_busy,
    point_cell,
    check_winner,
    check_draw
)


class TestTicTacToe(TestCase):

    def setUp(self):
        self.board_size = 4
        self.board = [['.' for _ in range(self.board_size)] for _ in range(self.board_size)]

    def test_is_cell_busy_and_point_cell(self):
        result = is_cell_busy(self.board, 0, 0)
        self.assertFalse(result)

        point_cell(self.board, 0, 0, 'X')
        result = is_cell_busy(self.board, 0, 0)
        self.assertTrue(result)

    def test_check_winner_rows(self):
        self.board[0] = ['X'] * self.board_size
        self.assertTrue(check_winner(self.board, 'X'))

        self.board[0] = ['X'] * (self.board_size - 1) + ['O']
        self.assertFalse(check_winner(self.board, 'X'))

    def test_check_winner_columns(self):
        for row in range(self.board_size):
            self.board[row][0] = 'X'
        self.assertTrue(check_winner(self.board, 'X'))

        self.board[0][0] = 'X'
        for row in range(1, self.board_size):
            self.board[row][0] = 'O'
        self.assertFalse(check_winner(self.board, 'X'))

    def test_check_winner_main_diagonal(self):
        for i in range(self.board_size):
            self.board[i][i] = 'X'
        self.assertTrue(check_winner(self.board, 'X'))

    def test_check_winner_anti_diagonal(self):
        for i in range(self.board_size):
            self.board[i][self.board_size - 1 - i] = 'X'
        self.assertTrue(check_winner(self.board, 'X'))

    def test_check_no_winner(self):
        self.assertFalse(check_winner(self.board, 'X'))

        self.board[0] = ['O'] * self.board_size
        self.assertFalse(check_winner(self.board, 'X'))

    def test_check_draw(self):
        self.assertFalse(check_draw(self.board))
        board = [['O' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.assertTrue(check_draw(board))

