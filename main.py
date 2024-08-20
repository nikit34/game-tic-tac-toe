
def show_board(board):
    print('  1 2 3')
    for i, row in enumerate(board):
        print(str(i) + ' ' + ' '.join(row))


if __name__ == "__main__":
    board = [['.' for _ in range(3)] for _ in range(3)]

    while True:
        show_board(board)
