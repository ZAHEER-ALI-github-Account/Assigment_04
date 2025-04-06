import pygame
import numpy as np
import sys
import math

# Constants
ROW_COUNT = 6
COLUMN_COUNT = 7
SQUARESIZE = 100
RADIUS = int(SQUARESIZE / 2 - 5)
MY_BLUE = (0, 0, 255)
MY_BLACK = (0, 0, 0)
MY_RED = (255, 0, 0)
MY_YELLOW = (255, 255, 0)
EMPTY = 0
PLAYER_1 = 1
PLAYER_2 = 2

# Create the game board (6 rows x 7 columns)
def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board

# Drop the piece in the selected column
def drop_piece(board, row, col, piece):
    board[row][col] = piece

# Get the next available row in a column
def get_next_available_row(board, col):
    for r in range(ROW_COUNT-1, -1, -1):
        if board[r][col] == EMPTY:
            return r

# Print the game board in the console (for debugging)
def print_board(board):
    print(np.flip(board, 0))

# Check if a player has won
def is_winning_move(board, piece):
    # Check horizontal locations
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
    # Check vertical locations
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
    # Check positively sloped diagonals
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True
    # Check negatively sloped diagonals
    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True
    return False

# Create the game window
def draw_board(board, screen):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, MY_BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, MY_BLACK, (int(c*SQUARESIZE + SQUARESIZE/2), int(r*SQUARESIZE + SQUARESIZE + SQUARESIZE/2)), RADIUS)
    
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == PLAYER_1:
                pygame.draw.circle(screen, MY_RED, (int(c*SQUARESIZE + SQUARESIZE/2), int(r*SQUARESIZE + SQUARESIZE + SQUARESIZE/2)), RADIUS)
            elif board[r][c] == PLAYER_2:
                pygame.draw.circle(screen, MY_YELLOW, (int(c*SQUARESIZE + SQUARESIZE/2), int(r*SQUARESIZE + SQUARESIZE + SQUARESIZE/2)), RADIUS)
    pygame.display.update()

# Main game function
def main():
    pygame.init()
    myfont = pygame.font.SysFont("monospace", 75)
    board = create_board()
    print_board(board)

    game_over = False
    turn = PLAYER_1

    screen = pygame.display.set_mode((COLUMN_COUNT*SQUARESIZE, (ROW_COUNT+1)*SQUARESIZE))
    draw_board(board, screen)

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, MY_BLACK, (0, 0, COLUMN_COUNT*SQUARESIZE, SQUARESIZE))
                posx = event.pos[0]
                pygame.draw.circle(screen, MY_RED, (posx, int(SQUARESIZE/2)), RADIUS)

            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))

                if board[ROW_COUNT-1][col] == EMPTY:
                    row = get_next_available_row(board, col)
                    drop_piece(board, row, col, turn)

                    if is_winning_move(board, turn):
                        label = myfont.render(f"Player {turn} wins!!", 1, MY_RED if turn == PLAYER_1 else MY_YELLOW)
                        screen.blit(label, (40, 10))
                        pygame.display.update()
                        game_over = True

                    turn = PLAYER_2 if turn == PLAYER_1 else PLAYER_1

                    print_board(board)
                    draw_board(board, screen)

                    if game_over:
                        pygame.time.wait(3000)

# Run the game
if __name__ == "__main__":
    main()
