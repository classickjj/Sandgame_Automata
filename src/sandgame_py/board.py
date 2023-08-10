import tkinter as tk
import settings
import particle


################################################### GAMEBOARD ##############################################################################

# create a gameboard with a grid, size x * y, and the given particlettype -> in my case always created with air particles
def create_game_board(type, x, y):
    game_board = [[particle.Particle(type, row, col) for col in range(y)] for row in range(x)]
    return game_board


# function to draw the gameboard / draw changes on the gameboard ---- TODO: do i actually need to give cell_w and cell_h? i dont think so ... 
def draw_game_board(canvas, game_board, cell_width, cell_height):
   
    # Draw individual cells
    for cell in settings.changed_cells:
        row, col = cell
             
        particle = game_board[row][col]  # Get the particle at the current position
        particle_color = particle.color  # Get the color of the particle

        # values regarding position needed to draw individual cells
        x1 = row * cell_width + 2
        y1 = col * cell_height + 2
        x2 = x1 + cell_width
        y2 = y1 + cell_height 

        # draw a (filled) rectangle (cell) at specified coordinates with given color (and if specified with cell border) 
        canvas.create_rectangle(x1, y1, x2, y2, outline="", fill=particle_color)
    
    #clear the updated cells list after drawing them 
    settings.changed_cells.clear()

    # when done print msg in console
    #print("Game board updated")
    

################################################### WINDOW/BOARD SETUP #####################################################################

# function to "run" the whole "board" including the game canvas and other things that need to be displayed
# for example the position of the mouse in the grid of cells, buttons, etc.
def add_cells_to_draw():
    for row in settings.nextGen_game_board:
        for prtcle in row:
            # Access and work with the particle object
            # For example, you can print its type, row, and column:
            posi = prtcle.get_pos()
            settings.changed_cells.append(posi)
            #print(f"Type: {prtcle.type}, Row: {prtcle.x_pos}, Col: {prtcle.y_pos} added")
    print("\t\t\t>>>> initial particles added to changed cells")

def run_board():
     
    # Set the dimensions of the (whole) window
    window_width = settings.game_board_width + 200  # Extra width for buttons and status bars
    window_height = settings.game_board_height + 10

    # debug print statement
    print("\t\t>>> dimensions set, starting window creation")

    # Create the window
    settings.root.geometry(f"{window_width}x{window_height}")
    print("\t\t>>> window was created")

    # set the position of the game-canvas in the application window
    settings.canvas.pack(side=tk.LEFT)

    # postion Extra buttons and status bars
    settings.posi_label.pack(side=tk.BOTTOM, anchor=tk.S)
    settings.type_color_label.pack(side=tk.BOTTOM, anchor=tk.S)
    settings.type_label.pack(side=tk.BOTTOM, anchor=tk.S)
    settings.button_label.pack(side=tk.TOP, anchor=tk.N)
    print("\t\t>>> packing done")
  
    #first time initialise all cells to be "changed" (because right now the "draw" function only operates on the changed cells list)
    add_cells_to_draw()

    # Draw the game board
    draw_game_board(settings.canvas, settings.nextGen_game_board, settings.cell_width, settings.cell_height)
    print("\t\t>>> gameboard setup finished and drawn")