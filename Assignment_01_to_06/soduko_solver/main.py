def print_board(board):
    """Print the Sudoku board."""
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))


def find_empty(board):
    """Return the row, column of an empty cell (represented by 0)."""
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return i, j
    return None


def is_valid(board, num, row, col):
    """Check if it's valid to place a number in the given position."""
    # Check the row
    if num in board[row]:
        return False

    # Check the column
    for r in range(len(board)):
        if board[r][col] == num:
            return False

    # Check the 3x3 subgrid
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if board[r][c] == num:
                return False

    return True


def solve(board):
    """Solve the Sudoku puzzle using backtracking."""
    empty = find_empty(board)
    if not empty:
        return True  # Puzzle solved

    row, col = empty

    for num in range(1, 10):  # Try numbers 1-9
        if is_valid(board, num, row, col):
            board[row][col] = num

            if solve(board):
                return True  # Solution found, recurse

            # Backtrack if no solution found
            board[row][col] = 0

    return False  # No solution found, backtrack


def main():
    # Sample Sudoku puzzle (0's represent empty spaces)
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("Original Sudoku Puzzle:")
    print_board(board)

    if solve(board):
        print("\nSolved Sudoku Puzzle:")
        print_board(board)
    else:
        print("No solution exists!")


if __name__ == "__main__":
    main()
