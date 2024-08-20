
def show_board(board):
    print('  1 2 3')
    for i, row in enumerate(board):
        print(str(i) + ' ' + ' '.join(row))


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
                    print("Игрок делает ход")
                    break
                else:
                    print("[ERROR] Введите значение от 1 до 3")
            except ValueError:
                print("[ERROR] Введите число")

        step += 1
