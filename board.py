from ship import read_ship_file

class Board:
    def __init__(self):
        self.own_board = [
            ['~' for _ in range(8)] for _ in range(8)
        ]
        self.enemy_board = [
            ['~' for _ in range(8)] for _ in range(8)
        ]
        self.ships = []

    def setup_ships(self, ship_file):
        ships = read_ship_file(ship_file)
        for ship in ships:
            if not self.place_ship(ship):
                print("Error placing ship at" + str(ship.positions))
                return False
        return True

    # Check if there is a ship at a position given
    def is_occupied(self, position):
        row, col = position
        return self.own_board[row][col] == 'S'
    
    # Check and place ship on our own board
    def place_ship(self, ship):
        for position in ship.positions:
            if self.is_occupied(position):
                print("Error: Overlapping ships at" + position)
                return False
        
        for position in ship.positions:
            self.own_board[position[0]][position[1]] = 'S'
        self.ships.append(ship)
        return True
    
    # Check all our ships and try to find if the position is the same as given in the parameter
    def find_ship_by_position(self, position):
        for ship in self.ships:
            if position in ship.positions:
                return ship
        return None


    def receive_attack(self, position): # need to improve this
        row, col = map(int, position.split(','))
        print("Attack on " + str(position))
        if self.own_board[row][col] == 'S':
            self.own_board[row][col] = 'H'
            ship = self.find_ship_by_position((int(row), int(col)))
            if ship:
                ship.hit()
                return 'Sunk'
            return 'Hit'
        else:
            self.own_board[row][col] == "M"
            return 'Miss'
    
    def update_enemy_board(self, network, attack_position):
        result = network.receive()
        if result is not None:
            if result == "Hit":
                self.enemy_board[attack_position[0]][attack_position[1]] = 'H'
            elif result == "Miss":
                self.enemy_board[attack_position[0]][attack_position[1]] = 'M'
            elif result == "Sunk":
                self.enemy_board[attack_position[0]][attack_position[1]] = 'H'
            elif result == "Win":
                print("You win")

    def all_ships_sunk(self):
        return all(ship.is_sunk() for ship in self.ships)
