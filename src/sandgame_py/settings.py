# settings
import tkinter as tk
import board

############################################## APPLICATION SETTINGS ######################################################

# size of the actual game "canvas"
game_board_width = 1280
game_board_height = 720

# cell size ... (needs to be common divider of the width and height value for fully used canvas since its 16:9 formnat and not a square)
# maybe can find a more dynamic way, if game canvas size is changed , or cell size is adjustable in app (at some point in the future)
cell_width = 4
cell_height = 4

# compute number of cells on the board given the set parameters for canvas and cell size 
cells_number_w = game_board_width // cell_width
cells_number_h = game_board_height // cell_height
# for debugging: print the computed values to console
print("cell width: " + str (cells_number_w) + ", cell height: " + str (cells_number_h)) 

# initiate empty list that stores position of cells that change state from one generation to the next
changed_cells = list()

# initiate types of particles that are available to the player and set a (publicly accesable) index for the list
particle_types = ["Stone", "Sand", "Water"]
current_particle_index = 0

# initiate TWO gameboards! one that holds the current generation, and one for the next generation
current_game_board = board.create_game_board("Air", cells_number_w, cells_number_h)
print("created current game board")

nextGen_game_board = board.create_game_board("Air", cells_number_w, cells_number_h)
print("created next gen board")

# set root, title, application-window-size, labels for application, etc.
root = tk.Tk()

# set title of the application
root.title("Sand Game")

# Create the canvas for the game board
# game canvas -> +2 added to the dimensions are needed to draw/display top rows and left most columns cell border (idk why really)
canvas = tk.Canvas(root, width=game_board_width+0, height=game_board_height+0, bg="green")
print("game canvas created")


# this is is the default, when no posi was ever "touched" by the player, see how text updates in IOevents
# in other words, this is just a filler in the beginning!
posi_label = tk.Label(root, text="x:  , y:  ", font=("Calibri", 16))