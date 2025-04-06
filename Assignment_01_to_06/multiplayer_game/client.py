import socket
import threading
import pygame

# Initialize Pygame
pygame.init()

# Define constants for the game window
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 5
LINE_COLOR = (0, 0, 0)
BOARD_COLOR = (255, 255, 255)

# Initialize Pygame screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe Multiplayer")

# Create the game grid
def draw_grid():
    screen.fill(BOARD_COLOR)
    pygame.draw.line(screen, LINE_COLOR, (WIDTH//3, 0), (WIDTH//3, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * WIDTH//3, 0), (2 * WIDTH//3, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT//3), (WIDTH, HEIGHT//3), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * HEIGHT//3), (WIDTH, 2 * HEIGHT//3), LINE_WIDTH)

# Function to display the current board on screen
def display_board(board):
    font = pygame.font.Font(None, 60)
    for i, spot in enumerate(board):
        x = (i % 3) * (WIDTH // 3) + WIDTH // 6
        y = (i // 3) * (HEIGHT // 3) + HEIGHT // 6
        text = font.render(spot, True, (0, 0, 0))
        screen.blit(text, (x - text.get_width() // 2, y - text.get_height() // 2))

# Handle receiving data from the server
def receive():
    global board, current_player
    while True:
        message = client.recv(1024).decode()
        if message:
            if "wins" in message or "draw" in message:
                print(message)
                pygame.quit()
                quit()
            print(message)

# Function to handle player's move
def make_move():
    global board, current_player
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = pos[1] // (HEIGHT // 3), pos[0] // (WIDTH // 3)
                move = row * 3 + col
                if board[move] == ' ':
                    client.send(str(move).encode())  # Send move to server
                    board[move] = current_player
                    current_player = 'O' if current_player == 'X' else 'X'
                    return

# Connect to the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5555))  # Connect to the server

# Start thread to receive messages
threading.Thread(target=receive, daemon=True).start()

# Initialize game state
board = [' ' for _ in range(9)]
current_player = 'X'

# Main game loop
while True:
    draw_grid()
    display_board(board)
    make_move()
    pygame.display.update()
