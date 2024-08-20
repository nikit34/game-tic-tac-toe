
def show_board(board):
    n = len(board)
    print('  ' + ' '.join(str(i + 1) for i in range(n)))
    for i, row in enumerate(board):
        print(str(i + 1) + ' ' + ' '.join(row))


def is_cell_busy(board, row, col):
    if board[row][col] == '.':
        return False
    return True


def point_cell(board, row, col, player):
    board[row][col] = player


def check_winner(board, player):
    count_columns = len(board)

    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(count_columns):
        if all(board[row][col] == player for row in range(count_columns)):
            return True

    if all(board[i][i] == player for i in range(count_columns)):
        return True

    if all(board[i][count_columns - 1 - i] == player for i in range(count_columns)):
        return True

    return False


def check_draw(board):
    return all(cell != '.' for row in board for cell in row)


if __name__ == '__main__':
    board_size = int(input('Введите размер строки (например, 3 для 3x3): '))
    if board_size < 2:
        raise ValueError('Размер поля должен быть больше 2')

    board = [['.' for _ in range(board_size)] for _ in range(board_size)]
    step = 0
    players = ['O', 'X']

    while True:
        show_board(board)
        player = players[step % 2]
        print('Ход игрока: ' + player)

        while True:
            try:
                row = int(input('Введите номер строки (1-' + str(board_size) + '): ')) - 1
                col = int(input('Введите номер столбца (1-' + str(board_size) + '): ')) - 1
                if 0 <= row < board_size and 0 <= col < board_size:
                    if is_cell_busy(board, row, col):
                        print('[WARNING] Эта клетка уже занята')
                    else:
                        point_cell(board, row, col, player)
                        break
                else:
                    print('[ERROR] Введите значение от 1 до ' + str(board_size))
            except ValueError:
                print('[ERROR] Введите число')

        if check_winner(board, player):
            show_board(board)
            print('Игрок ' + player + ' выиграл!')
            break

        if check_draw(board):
            show_board(board)
            print('Ничья!')
            break

        step += 1
