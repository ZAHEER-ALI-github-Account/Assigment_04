import time
import math

# Print the board
def print_board(board):
    for row in board:
        print('| ' + ' | '.join(row) + ' |')

# Check for a win
def check_winner(board, player):
    # Rows, columns, and diagonals
    for row in board:
        if all(s == player for s in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

# Check if board is full
def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

# Get valid user input
def get_move(player):
    while True:
        try:
            row = int(input(f"Player {player}, enter row (0-2): "))
            col = int(input(f"Player {player}, enter col (0-2): "))
            if row in range(3) and col in range(3):
                return row, col
            else:
                print("Invalid input. Enter numbers 0, 1, or 2.")
        except ValueError:
            print("Please enter valid numbers.")

# Main game loop
def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    print("🎮 Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        row, col = get_move(current_player)

        if board[row][col] != ' ':
            print("That spot is taken. Try again.")
            continue

        board[row][col] = current_player
        print_board(board)

        if check_winner(board, current_player):
            print(f"🎉 Player {current_player} wins!")
            break

        if is_board_full(board):
            print("🤝 It's a tie!")
            break

        current_player = 'O' if current_player == 'X' else 'X'
        time.sleep(0.5)

if __name__ == "__main__":
    play_game()
