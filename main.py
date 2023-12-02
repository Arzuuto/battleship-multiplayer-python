import sys
from network import Network
from board import Board, read_ship_file
from player import Player
from graphical import display_board

def main():
    if len(sys.argv) == 2:
        # Start as server
        ship_file = sys.argv[1]
        network = Network()
        network.start_server()
        # Additional code to set up the game board using ship_file
        
        # Example: receive a message from client
        client_message = network.receive()
        print(f"Message from client: {client_message}")

    elif len(sys.argv) == 3:
        # Start as client
        ip_address = sys.argv[1]
        ship_file = sys.argv[2]
        network = Network(host=ip_address)
        network.connect_to_server()
        # Additional code to set up the game board using ship_file
        
        # Example: send a message to server
        message = "Hello, server!"
        network.send(message)

    else:
        print("Usage: main.py [ip_address] ship_file")
        sys.exit(1)

    board = Board()
    player = Player(board)
    ships = read_ship_file(ship_file)
    for ship in ships:
        if not board.place_ship(ship):
            print("Error placing ship at" + str(ship.positions))
            sys.exit(1)
    game_over = False
    is_server = True
    display_board(board.grid, show_ships=True)
    while not game_over:
        if is_server:
            pass
        else:
            pass
    # Here you can add the main game loop, handle game logic, etc.

    # Close the network connection at the end
    network.close_connection()

if __name__ == "__main__":
    main()
