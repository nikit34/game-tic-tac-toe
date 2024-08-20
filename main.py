



if __name__ == "__main__":
    board = [['.' for _ in range(3)] for _ in range(3)]
    print('  1 2 3')
    for i, row in enumerate(board):
        print(str(i) + ' ' + ' '.join(row))
