class Ship:
    def __init__(self, size, positions):
        self.size = size
        self.positions = positions
        self.hits = 0

    def hit(self):
        self.hits += 1

    def is_sunk(self):
        return self.hits == self.size

def parse_position(position):
    row = int(position[1:]) - 1
    col = ord(position[0].upper()) - ord('A')
    return (row, col)

def get_ship_positions(start, end):
    start_row, start_col = parse_position(start)
    end_row, end_col = parse_position(end)
    positions = []

    # Check if the ship is placed horizontally or vertically
    if start_row == end_row:  # Horizontal
        for col in range(start_col, end_col + 1):
            positions.append((start_row, col))
    else:  # Vertical
        for row in range(start_row, end_row + 1):
            positions.append((row, start_col))
    
    return positions

def read_ship_file(file_path):
    ships = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(':')
            size = int(parts[0])
            start, end = parts[1], parts[2]

            positions = get_ship_positions(start, end)
            ships.append(Ship(size, positions))
            
    return ships
