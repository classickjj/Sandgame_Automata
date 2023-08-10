import settings
import particle
from board import draw_game_board

########################################### USER I/O HANDLING ##########################################################################

def on_mouse_down(event):
    settings.is_mouse_held = True
    set_particle(event)  # Apply the function on mouse down
    #print("mouse held down")

def on_mouse_up(event):
    settings.is_mouse_held = False
    #print("mouse released")

def handle_mouse_motion(event):
    if settings.is_mouse_held:
        set_particle(event)
        #print("moving")

    mouse_posi(event)

def set_particle(event):
    # Get the cell coordinates based on the mouse click event
    x = event.x // settings.cell_width
    y = event.y // settings.cell_height

    # Get the currently selected particle type
    current_particle_type = settings.particle_types[settings.current_particle_index]

    # Set the particle type on the game board at the specified cell
    #if (x, y) not in settings.changed_cells:
    settings.nextGen_game_board[x][y] = particle.Particle(current_particle_type, x, y)
    settings.changed_cells.append((x, y))

    #print("set '" + current_particle_type + "' particle at x: " + str(x) + ", y: " + str(y))

    # Redraw the game board to reflect the updated particle
    draw_game_board(settings.canvas, settings.nextGen_game_board, settings.cell_width, settings.cell_height)
   

def get_part_color(text):
        if text == "Stone":
            return "gray"
        elif text == "Sand":
            return "yellow"
        elif text == "Water":
            return "blue" 

def change_particle_type(event):
    # Update the current_particle_index based on mouse wheel rotation
    delta = event.delta
    settings.current_particle_index += int(delta / 120)  # Assumes each wheel click changes the index by 1

    # Wrap around to the beginning or end of the particle_types list
    if settings.current_particle_index < 0:
        settings.current_particle_index = len(settings.particle_types) - 1
    elif settings.current_particle_index >= len(settings.particle_types):
        settings.current_particle_index = 0

    # Display the currently selected particle type
    settings.type_label.config(text=f"{settings.particle_types[settings.current_particle_index]}")
    settings.type_color_label.config(bg=get_part_color(settings.particle_types[settings.current_particle_index]))


def mouse_posi(event):
    # Returns current (cell-)position of mouse in cell grid and displays it
    x = event.x // settings.cell_width
    y = event.y // settings.cell_height

    # Update the position display
    settings.posi_label.config(text=f"x: {x}, y: {y}")

########################################### REGISTER EVENTS TO USER INPUTS #############################################################

# Register the set_particle function to handle left-click events on the canvas
settings.canvas.bind("<Button-1>", on_mouse_down)
settings.canvas.bind("<ButtonRelease-1>", on_mouse_up)

# Register the change_particle_type function to handle mouse wheel events on the canvas
settings.canvas.bind("<MouseWheel>", lambda event: change_particle_type(event))

# Register the mouse_posi function to handle mouse position
settings.canvas.bind("<Motion>", handle_mouse_motion)

########################################### HANDLE WINDOW CLOSING ######################################################################

# Add window close event handler
def on_closing():
    print("> window closed")
    settings.root.destroy()
    
settings.root.protocol("WM_DELETE_WINDOW", on_closing)