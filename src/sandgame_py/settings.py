# settings
import tkinter as tk
import board


############################################## APPLICATION SETTINGS ######################################################

print("> starting game")
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
print(f"\t>> board dimensions: {cells_number_w} x {cells_number_h} cells (-> width x height)") 

# initiate empty list that stores position of cells that change state from one generation to the next
changed_cells = list()

# input helper
is_mouse_held = False
is_game_started = False

# initiate types of particles that are available to the player and set a (publicly accesable) index for the list
particle_types = ["Stone", "Sand", "Water"]
current_particle_index = 0

# initiate TWO gameboards! one that holds the current generation, and one for the next generation
current_game_board = board.create_game_board("Air", cells_number_w, cells_number_h)
print("\t>> created current game board")

nextGen_game_board = board.create_game_board("Air", cells_number_w, cells_number_h)
print("\t>> created next gen board")

# set root, title, application-window-size, labels for application, etc.
root = tk.Tk()

# set title of the application
root.title("Sand Game")

# Create the canvas for the game board
# game canvas -> +2 added to the dimensions are needed to draw/display top rows and left most columns cell border (idk why really)
canvas = tk.Canvas(root, width=game_board_width+0, height=game_board_height+0, bg="green")
print("\t>> game canvas created")

################################################## LABEL AND BUTTONS ###############################################################

# label showing mouse pos. this is is the default, when no posi was ever "touched" by the player, see how text updates in IOevents
posi_label = tk.Label(root, text="x:  , y:  ", font=("Calibri", 16))

# labels to show selected particle type 
type_label = tk.Label(root, text=f"{particle_types[current_particle_index]}", font=("Calibri", 14))
type_color_label = tk.Label(root, width=2, bg="gray")

#button label
button_label = tk.Label(root)

# start/pause button
def start_button_clicked():
    global is_game_started
    if not is_game_started: 
        print("game started/continued")
        start_pause_button.config(text="Pause")
        is_game_started = True
        #TODO Call update function here
    else:
        print("game stopped/paused")
        start_pause_button.config(text="Continue")
        is_game_started = False
        #TODO Pause update function here
    
start_pause_button = tk.Button(button_label, text="Start", command=start_button_clicked)

# reset/restart button 
def reset_button_clicked():   

    changed_cells.clear()
    start_pause_button.config(text="Start")
                                 
    global current_game_board
    current_game_board.clear()

    global nextGen_game_board
    nextGen_game_board.clear()

    current_game_board = board.create_game_board("Air", cells_number_w, cells_number_h)
    #print("created current game board after reset")

    nextGen_game_board = board.create_game_board("Air", cells_number_w, cells_number_h)
    #print("created next gen board after reset")
    
    board.add_cells_to_draw()
    board.draw_game_board(canvas, nextGen_game_board, cell_width, cell_height)

    posi_label.config(text="x:  , y:  ")
    global current_particle_index
    current_particle_index = 0

    global is_game_started
    is_game_started = False

    type_label.config(text=f"{particle_types[current_particle_index]}")
    type_color_label.config(bg="gray")

reset_button = tk.Button(button_label, text="Reset", command=reset_button_clicked)

start_pause_button.pack(side=tk.LEFT, anchor=tk.W)
reset_button.pack(side=tk.RIGHT, anchor=tk.E)

