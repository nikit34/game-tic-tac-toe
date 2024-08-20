
def show_board(board):
    print('  1 2 3')
    for i, row in enumerate(board):
        print(str(i) + ' ' + ' '.join(row))


def is_cell_busy(board, row, col):
    if board[row][col] == '.':
        return False
    return True


def point_cell(board, row, col, player):
    board[row][col] = player


def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    return False


if __name__ == "__main__":
    board = [['.' for _ in range(3)] for _ in range(3)]
    step = 0
    players = ['O', 'X']

    while True:
        show_board(board)
        player = players[step % 2]
        print("Ход игрока: " + player)

        while True:
            try:
                row = int(input("Введите номер строки (1-3): ")) - 1
                col = int(input("Введите номер столбца (1-3): ")) - 1
                if 0 <= row < 3 and 0 <= col < 3:
                    if is_cell_busy(board, row, col):
                        print("[WARNING] Эта клетка уже занята")
                    else:
                        point_cell(board, row, col, player)
                        break
                else:
                    print("[ERROR] Введите значение от 1 до 3")
            except ValueError:
                print("[ERROR] Введите число")

        step += 1
