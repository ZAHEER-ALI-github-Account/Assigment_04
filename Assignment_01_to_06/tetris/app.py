import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Define constants
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30
BOARD_WIDTH = 10
BOARD_HEIGHT = 20
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
COLORS = [CYAN, BLUE, ORANGE, YELLOW, GREEN, RED, PURPLE]

# Shapes of Tetriminos
TETROMINOS = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]],  # Z
    [[1, 0, 0], [1, 1, 1]],  # L
    [[0, 0, 1], [1, 1, 1]]   # J
]

# Function to create the game board
def create_board():
    board = [[0] * BOARD_WIDTH for _ in range(BOARD_HEIGHT)]
    return board

# Function to draw the board
def draw_board(board):
    for y in range(BOARD_HEIGHT):
        for x in range(BOARD_WIDTH):
            pygame.draw.rect(SCREEN, BLACK, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)
            if board[y][x] != 0:
                pygame.draw.rect(SCREEN, COLORS[board[y][x] - 1], (x * BLOCK_SIZE + 1, y * BLOCK_SIZE + 1, BLOCK_SIZE - 2, BLOCK_SIZE - 2))

# Function to check for collisions
def check_collision(board, piece, offset):
    off_x, off_y = offset
    for y, row in enumerate(piece):
        for x, cell in enumerate(row):
            if cell:
                try:
                    if board[y + off_y][x + off_x] != 0:
                        return True
                except IndexError:
                    return True
    return False

# Function to place the piece on the board
def place_piece(board, piece, offset):
    off_x, off_y = offset
    for y, row in enumerate(piece):
        for x, cell in enumerate(row):
            if cell:
                board[y + off_y][x + off_x] = piece[y][x]

# Function to remove completed lines
def remove_lines(board):
    new_board = [row for row in board if any(cell == 0 for cell in row)]
    new_lines = BOARD_HEIGHT - len(new_board)
    new_board = [[0] * BOARD_WIDTH for _ in range(new_lines)] + new_board
    return new_board, new_lines

# Function to rotate the piece
def rotate_piece(piece):
    return list(zip(*piece[::-1]))

# Function to draw the text on screen
def draw_text(text, size, color, y_offset=0):
    font = pygame.font.Font(None, size)
    label = font.render(text, True, color)
    SCREEN.blit(label, (SCREEN_WIDTH // 2 - label.get_width() // 2, SCREEN_HEIGHT // 2 - label.get_height() // 2 + y_offset))

# Main game function
def main():
    board = create_board()
    clock = pygame.time.Clock()
    game_over = False

    # Start the game with a random piece
    current_piece = random.choice(TETROMINOS)
    current_color = random.choice(COLORS)
    piece_x = BOARD_WIDTH // 2 - len(current_piece[0]) // 2
    piece_y = 0

    while not game_over:
        SCREEN.fill(WHITE)
        draw_board(board)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if not check_collision(board, current_piece, (piece_x - 1, piece_y)):
                        piece_x -= 1
                elif event.key == pygame.K_RIGHT:
                    if not check_collision(board, current_piece, (piece_x + 1, piece_y)):
                        piece_x += 1
                elif event.key == pygame.K_DOWN:
                    if not check_collision(board, current_piece, (piece_x, piece_y + 1)):
                        piece_y += 1
                elif event.key == pygame.K_UP:
                    rotated = rotate_piece(current_piece)
                    if not check_collision(board, rotated, (piece_x, piece_y)):
                        current_piece = rotated

        # Drop the piece one step down
        if not check_collision(board, current_piece, (piece_x, piece_y + 1)):
            piece_y += 1
        else:
            place_piece(board, current_piece, (piece_x, piece_y))
            board, lines_cleared = remove_lines(board)
            current_piece = random.choice(TETROMINOS)
            piece_x = BOARD_WIDTH // 2 - len(current_piece[0]) // 2
            piece_y = 0
            if check_collision(board, current_piece, (piece_x, piece_y)):
                game_over = True

        # Draw the current piece
        for y, row in enumerate(current_piece):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(SCREEN, current_color, (piece_x * BLOCK_SIZE + x * BLOCK_SIZE, piece_y * BLOCK_SIZE + y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

        # Draw the game over screen
        if game_over:
            draw_text("GAME OVER", 50, RED)

        pygame.display.flip()
        clock.tick(10)

    pygame.quit()
    quit()

# Run the game
if __name__ == "__main__":
    main()
