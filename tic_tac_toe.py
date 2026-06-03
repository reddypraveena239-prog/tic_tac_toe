import math

board = [' ' for _ in range(9)]


def print_board():
    print()
    for i in range(3):
        print(board[i * 3] + " | " + board[i * 3 + 1] + " | " + board[i * 3 + 2])
        if i < 2:
            print("--+---+--")
    print()


def check_winner(player):
    winning_positions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for position in winning_positions:
        if all(board[i] == player for i in position):
            return True
    return False


def check_draw():
    return ' ' not in board


def minimax(is_maximizing):
    if check_winner('O'):
        return 1
    if check_winner('X'):
        return -1
    if check_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score


def ai_move():
    best_score = -math.inf
    move = 0

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(False)
            board[i] = ' '

            if score > best_score:
                best_score = score
                move = i

    board[move] = 'O'


def player_move():
    while True:
        try:
            move = int(input("Enter position (1-9): ")) - 1

            if 0 <= move <= 8 and board[move] == ' ':
                board[move] = 'X'
                break
            else:
                print("Invalid move! Try again.")
        except ValueError:
            print("Please enter a number.")


print("=== Tic-Tac-Toe Game ===")
print("You are X")
print("AI is O")

while True:
    print_board()

    player_move()

    if check_winner('X'):
        print_board()
        print("Congratulations! You win.")
        break

    if check_draw():
        print_board()
        print("It's a draw!")
        break

    print("AI is making a move...")
    ai_move()

    if check_winner('O'):
        print_board()
        print("AI wins!")
        break

    if check_draw():
        print_board()
        print("It's a draw!")
        break