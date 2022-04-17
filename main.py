# github push
size_board = 3
game_board = [[0 for i in range(size_board)] for j in range(size_board)]


def create_board(board):
    for i in range(size_board):
        for j in range(size_board):
            if board[i][j] == 0:
                board[i][j] = i * size_board + j + 1
            print(f'| {board[i][j]}', end=' ')
        print('|')


def to_list(board):
    list_board = []
    for i in range(size_board):
        for j in range(size_board):
            list_board.append(board[i][j])
    return list_board


def player_input(board, switch):
    list_board = to_list(board)
    check = True
    while check:
        place_number = input(f'Select place for {switch}: ')
        try:
            place_number = int(place_number)
        except ValueError:
            print(f'Not correct value, try again')
            continue
        if 1 <= place_number <= size_board * size_board and place_number in list_board and str(
                list_board[place_number - 1]) not in "XO":
            for i in range(size_board):
                if place_number in board[i]:
                    board[i][board[i].index(place_number)] = switch
                    check = False
        else:
            print(f'Select free place in range 1..9')


def check_winner(board, switch):
    diagonal_1, diagonal_2 = (True, True)
    for i in range(size_board):
        horizontal, vertical = (True, True)
        diagonal_1 = diagonal_1 and (board[i][i] == switch)
        diagonal_2 = diagonal_2 and (board[size_board - i - 1][i] == switch)
        for j in range(size_board):
            horizontal = horizontal and (board[i][j] == switch)
            vertical = vertical and (board[j][i] == switch)
        if horizontal or vertical:
            return True
    if diagonal_1 or diagonal_2:
        return True
    return False


def main(board):
    create_board(board)
    counter = 0
    switch_xo = 'X'
    while counter < size_board * size_board:
        if switch_xo == 'X':
            player_input(board, switch_xo)
            if counter > size_board and check_winner(board, switch_xo):
                create_board(board)
                print(f'Winner is player {switch_xo}!')
                break
            create_board(board)
            switch_xo = 'O'
        elif switch_xo == 'O':
            player_input(board, switch_xo)
            if counter > size_board and check_winner(board, switch_xo):
                create_board(board)
                print(f'Winner is player {switch_xo}!')
                break
            create_board(board)
            switch_xo = 'X'
        counter += 1
        if counter == 9:
            print('DRAW!!!')


if __name__ == '__main__':
    main(game_board)
