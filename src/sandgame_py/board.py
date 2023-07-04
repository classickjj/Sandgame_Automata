import tkinter as tk
import settings
import particle

def draw_game_board(canvas, game_board, cell_width, cell_height):
    # Set the background color for the game board
    board_background_color = "light grey"
    canvas.create_rectangle(0, 0, len(game_board) * cell_width, len(game_board[0]) * cell_height, fill=board_background_color, outline="")

    # Draw individual cells
    for row in range(len(game_board)):
        for col in range(len(game_board[row])):
            x1 = row * cell_width + 3
            y1 = col * cell_height + 3
            x2 = x1 + cell_width 
            y2 = y1 + cell_height 

            particle = game_board[row][col]  # Get the particle at the current position
            particle_color = particle.color  # Get the color of the particle

            # for now only way to display all grid borders , otherwise top and left side of board is missing its edges
            if row == 0:  # Top row
                x1 -= 1
            if col == 0:  # Leftmost column
                y1 -= 1

            canvas.create_rectangle(x1, y1, x2, y2, outline="", fill=particle_color)

    print("drawn board grid")


def run_board():
    
    # hier eventuell einmal erste initiale board erstellung -> alle zellen werden gesetzt und danach nur noch in updateform...
     
    # Set the dimensions of the window
    window_width = settings.game_board_width + 200  # Extra width for buttons and status bars
    window_height = settings.game_board_height + 10

    print("dimensions set, starting window creation")

    settings.root.title("Sand Game")

    # Add window close event handler
    def on_closing():
        settings.root.destroy()

    settings.root.protocol("WM_DELETE_WINDOW", on_closing)


    # Create the window
    settings.root.geometry(f"{window_width}x{window_height}")
    print("window was created")

    # Create the canvas for the game board
    
    settings.canvas.pack(side=tk.LEFT)
    print("canvas was created")

    # Create extra buttons and status bars
    # ...

    # Draw the game board
    draw_game_board(settings.canvas, settings.game_board, settings.cell_width, settings.cell_height)
    print("gameboard drawn")

    #settings.root.mainloop()