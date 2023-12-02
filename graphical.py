import matplotlib.pyplot as plt
import numpy as np

def display_board(board, show_ships=True):
    fig, ax = plt.subplots()
    ax.set_xticks(np.arange(0.5, len(board[0]), 1))
    ax.set_yticks(np.arange(0.5, len(board), 1))
    ax.set_xticklabels([chr(c) for c in range(ord('A'), ord('A') + len(board[0]))])
    ax.set_yticklabels([str(i+1) for i in range(len(board))])
    ax.grid(which='both')

    # Color codes: water = lightblue, ship = gray, hit = red, miss = white
    color_map = {'~': 'lightblue', 'S': 'gray' if show_ships else 'lightblue', 'H': 'red', 'M': 'white'}

    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            ax.add_patch(plt.Rectangle((x, y), 1, 1, color=color_map[cell]))

    plt.gca().invert_yaxis()  # Invert y axis to match traditional grid
    plt.show()
    print("hello")

# Additional functions as needed
