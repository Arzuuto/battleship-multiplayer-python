from ship import parse_position
class Gameplay:
    def __init__(self, board, network, is_my_turn):
        self.board = board
        self.network = network
        self.is_my_turn = is_my_turn

    def check_for_win(self):
        if self.board.all_ships_sunk():
            self.network.send("Win")
            print("You lose !")
            return True
        else:
            return False

    # Player loop turn
    def handle_player_turn(self, ax1, ax2, graphics):
        print("It's your turn")
        row, col = self.get_attack_coordinates()
        self.network.send(str(row) + "," + str(col))
        self.is_my_turn = False
        self.board.update_enemy_board(self.network, (row, col))
        graphics.update_plots(self.board.own_board, self.board.enemy_board)
        return self.check_for_win()

    # Enemy loop turn
    def handle_enemy_turn(self, ax1, ax2, graphics):
        print("Waiting for enemy turn.")
        response = self.network.receive()
        if response == "Win":
            print("You win !")
            return True
        if response:
            message = self.board.receive_attack(response)
            self.network.send(message)
            self.is_my_turn = True
            graphics.update_plots(self.board.own_board, self.board.enemy_board)
        return self.check_for_win()

    # Get player input
    def get_attack_coordinates(self):
        while True:
            attack = input("Enter attack coordinates (e.g., A1): ").upper()
            if len(attack) >= 2 and attack[0] in 'ABCDEFGHIJ' and attack[1:].isdigit():
                row, col = parse_position(attack)
                if 0 <= row < 8 and 0 <= col < 8:
                    return row, col
            print("Invalid coordinates. Please try again.")
