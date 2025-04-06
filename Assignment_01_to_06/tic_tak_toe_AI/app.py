import math

# Display the board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Check if someone has won
def check_winner(board):
    # Check rows, columns and diagonals
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    return None

# Check if the board is full
def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == 'O':
        return 1
    elif winner == 'X':
        return -1
    elif is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

# AI move using minimax
def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    if move:
        board[move[0]][move[1]] = 'O'

# Main game loop
def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        # Player move
        row = int(input("Enter your row (0, 1, 2): "))
        col = int(input("Enter your col (0, 1, 2): "))
        if board[row][col] != ' ':
            print("That spot is taken. Try again.")
            continue
        board[row][col] = 'X'

        print_board(board)

        if check_winner(board) == 'X':
            print("You win!")
            break
        elif is_full(board):
            print("It's a draw!")
            break

        print("AI is making a move...")
        best_move(board)
        print_board(board)

        if check_winner(board) == 'O':
            print("AI wins!")
            break
        elif is_full(board):
            print("It's a draw!")
            break

# Entry point
if __name__ == "__main__":
    main()
