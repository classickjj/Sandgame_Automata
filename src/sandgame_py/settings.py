# settings
import tkinter as tk
import particle

game_board_width = 1282
game_board_height = 722

cell_width = 80
cell_height = 80

def create_game_board(row, col):
    game_board = [[particle.Particle("Air") for _ in range(col)] for _ in range(row)]
    print("created game board")
    return game_board

game_board = create_game_board(game_board_height, game_board_width)

root = tk.Tk()
canvas = tk.Canvas(root, width=game_board_width, height=game_board_height)

particle_types = ["Stone", "Sand", "Water"]
current_particle_index = 0