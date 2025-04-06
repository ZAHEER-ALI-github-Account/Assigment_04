import socket
import threading

# Game state
board = [' ' for _ in range(9)]  # Tic-Tac-Toe board
current_player = 'X'  # X always starts

# Function to broadcast messages to all clients
def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message)
            except:
                clients.remove(client)

# Function to handle each client connection
def handle_client(client_socket, addr):
    global current_player
    print(f"[NEW CONNECTION] {addr} connected.")
    
    # Send welcome message to the client
    client_socket.send("Welcome to Tic-Tac-Toe! You are Player " + current_player + "\n".encode())
    
    while True:
        try:
            # Wait for move from client
            message = client_socket.recv(1024).decode()
            if message:
                print(f"[{addr}] {message}")

                # Make move on the board
                move = int(message)
                if board[move] == ' ':
                    board[move] = current_player
                    broadcast(f"Player {current_player} played at position {move}\n".encode(), client_socket)
                    
                    # Check for win or draw
                    if check_win():
                        broadcast(f"Player {current_player} wins!\n".encode(), client_socket)
                        break
                    elif ' ' not in board:
                        broadcast("It's a draw!\n".encode(), client_socket)
                        break
                    
                    # Switch player
                    current_player = 'O' if current_player == 'X' else 'X'
                else:
                    client_socket.send("Invalid move. Try again.\n".encode())
        except:
            # If connection is lost, handle it here
            clients.remove(client_socket)
            break

# Function to check if a player has won
def check_win():
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]               # Diagonals
    ]
    
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
            return True
    return False

# Set up the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 5555))  # Listen on all IPs on port 5555
server.listen()

clients = []

print("[SERVER STARTED] Waiting for connections...")

# Accept new client connections
while True:
    client_socket, addr = server.accept()
    clients.append(client_socket)
    
    # Start a new thread for each client
    client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
    client_thread.start()
