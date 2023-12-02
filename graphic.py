import matplotlib.pyplot as plt
import numpy as np

class GameGraphics:
    def __init__(self, board_size):
        self.board_size = board_size
        plt.ion()
        self.fig, (self.ax1, self.ax2) = plt.subplots(1, 2, figsize=(10, 5))
        self.ax1.set_title("Own Board")
        self.ax2.set_title("Enemy Board")
        plt.show(block=False)

    def update_board(self, ax, board):
        ax.clear()
        ax.set_xticks(np.arange(0, self.board_size, 1))
        ax.set_xticklabels([chr(i+ord('A')) for i in range(self.board_size)])
        ax.set_yticks(np.arange(0, self.board_size, 1))
        ax.set_yticklabels([str(i+1) for i in range(self.board_size)])
        ax.xaxis.tick_top()
        ax.grid(which='both')

        color_map = {'~': 'lightblue', 'S': 'gray', 'H': 'red', 'M': 'white'}
        for y, row in enumerate(board):
            for x, cell in enumerate(row):
                color = color_map.get(cell, 'lightblue')
                ax.add_patch(plt.Rectangle((x, y), 1, 1, color=color))

        ax.invert_yaxis()

    def update_plots(self, own_board, enemy_board):
        self.update_board(self.ax1, own_board)
        self.update_board(self.ax2, enemy_board)
        plt.draw()
        plt.pause(0.1)
