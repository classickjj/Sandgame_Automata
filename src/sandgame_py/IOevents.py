import settings
import particle
from board import draw_game_board

def set_particle(event, canvas):
    # Get the cell coordinates based on the mouse click event
    x = event.x // settings.cell_width
    y = event.y // settings.cell_height

    # Get the currently selected particle type
    current_particle_type = settings.particle_types[settings.current_particle_index]

    # Set the particle type on the game board at the specified cell
    settings.game_board[x][y] = particle.Particle(current_particle_type)

    # Redraw the game board to reflect the updated particle
    draw_game_board(canvas, settings.game_board, settings.cell_width, settings.cell_height)


def change_particle_type(event, canvas):
    # Update the current_particle_index based on mouse wheel rotation
    delta = event.delta
    settings.current_particle_index += int(delta / 120)  # Assumes each wheel click changes the index by 1


    # Wrap around to the beginning or end of the particle_types list
    if settings.current_particle_index < 0:
        settings.current_particle_index = len(settings.particle_types) - 1
    elif settings.current_particle_index >= len(settings.particle_types):
        settings.current_particle_index = 0

    # Display the currently selected particle type
    print("Current Particle Type:", settings.particle_types[settings.current_particle_index])

    # Redraw the game board to reflect the updated particle type
    draw_game_board(canvas, settings.game_board, settings.cell_width, settings.cell_height)

    return settings.current_particle_index


