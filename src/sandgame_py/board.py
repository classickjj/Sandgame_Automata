import tkinter as tk
import settings
import particle

################################################### GAMEBOARD ##############################################################################

# create a gameboard with a grid, size x * y, and the given particlettype -> in my case always created with air particles
def create_game_board(type, x, y):
    game_board = [[particle.Particle(type, row, col) for col in range(y)] for row in range(x)]
    return game_board


# function to draw the gameboard / draw changes on the gameboard
def draw_game_board(canvas, game_board, cell_width, cell_height):
    # Set the background color for the game board
    #board_background_color = "light grey"
    #canvas.create_rectangle(0, 0, len(game_board) * cell_width, len(game_board[0]) * cell_height, fill=board_background_color, outline="")

    # debugging outputs
    #print("gb * cell-w:")
    #print(len(game_board) * cell_width)

    #print("gb[0] * cell-h")
    #print(len(game_board[0]) * cell_height)

    # Draw individual cells
    for cell in settings.changed_cells:
        row, col = cell
        
        # printstatement for debugging
        #print(f"x: {row}, y: {col} ist in der liste")
        
        particle = game_board[row][col]  # Get the particle at the current position
        particle_color = particle.color  # Get the color of the particle

        # values regarding position needed to draw individual cells
        x1 = row * cell_width + 2
        y1 = col * cell_height + 2
        x2 = x1 + cell_width
        y2 = y1 + cell_height 

        # for now only way to display all grid borders, otherwise top and left side of board is missing its edges
        #if row == 0:  # Top row
        #    x1 -= 1
        #if col == 0:  # Leftmost column
        #    y1 -= 1

        # draw a (filled) rectangle (cell) at specified coordinates with given color (and if specified with cell border) 
        canvas.create_rectangle(x1, y1, x2, y2, outline="", fill=particle_color)

    # when done print msg in console
    print("Game board updated")
    
    #TODO: i think here clear 
    settings.changed_cells.clear()
    print("after clear")

################################################### WINDOW/BOARD SETUP #####################################################################

# function to "run" the whole "board" including the game canvas and other things that need to be displayed
# for example the position of the mouse in the grid of cells, buttons, etc.
def run_board():
     
    # Set the dimensions of the (whole) window
    window_width = settings.game_board_width + 200  # Extra width for buttons and status bars
    window_height = settings.game_board_height + 10

    # debug print statement
    print("dimensions set, starting window creation")

    # Create the window
    settings.root.geometry(f"{window_width}x{window_height}")
    print("window was created")

    # set the position of the game-canvas in the application window
    settings.canvas.pack(side=tk.LEFT)
    print("canvas positioned left side of app window")

    # postion Extra buttons and status bars
    settings.posi_label.pack(side=tk.BOTTOM, anchor=tk.SE)
    
    #first time initialise all cells to be "changed" (because right now the "draw" function only operates on the changed cells list)
    for row in settings.nextGen_game_board:
        for prtcle in row:
            # Access and work with the particle object
            # For example, you can print its type, row, and column:
            posi = (prtcle.x_pos, prtcle.y_pos)
            settings.changed_cells.append(posi)
            #print(f"Type: {prtcle.type}, Row: {prtcle.x_pos}, Col: {prtcle.y_pos} added")
    print("initial particles added to changed cells")

    # Draw the game board
    draw_game_board(settings.canvas, settings.nextGen_game_board, settings.cell_width, settings.cell_height)
    print("gameboard setup finished")
    # the current selected particle should not be in console but in label like the mouse-position
    print("Currently selected particle type:", settings.particle_types[settings.current_particle_index])