from network import Network
from board import Board
from gameplay import Gameplay
from graphic import GameGraphics
import sys

def main():
    # Check if the user know how to start the program
    if len(sys.argv) < 2:
        print("Usage: main.py [ip_address] [port] ship_file")
        sys.exit(1)

    ship_file = sys.argv[-1]  # The last argument is always the ship file
    network = Network()

    # Determine if this is the server or the client
    if len(sys.argv) == 2:
        # Start as server (host)
        network.start_server()
        is_my_turn = True
    else:
        # Start as client (connecting to host)
        ip_address = sys.argv[1]
        port = int(sys.argv[2])
        network = Network(host=ip_address)
        network.connect_to_server(port)
        is_my_turn = False

    # Setup the game
    board = Board()
    if not board.setup_ships(ship_file): # Parse and check ship file
        print("Failed to set up ships. Exiting game.")
        sys.exit(1)
    gameplay = Gameplay(board, network, is_my_turn)
    graphics = GameGraphics()
    graphics.update_plots(board.own_board, board.enemy_board) # Show matplotlib

    # Game loop
    game_over = False
    while not game_over:
        if gameplay.is_my_turn:
            game_over = gameplay.handle_player_turn(graphics.ax1, graphics.ax2, graphics)
        else:
            game_over = gameplay.handle_enemy_turn(graphics.ax1, graphics.ax2, graphics)

    network.close_connection()

if __name__ == "__main__":
    main()