import IOevents
import settings
from board import run_board

if __name__ == "__main__":
    run_board()

    # Register the change_particle_type function from IOevents module to handle mouse wheel events on the canvas
    settings.canvas.bind("<MouseWheel>", lambda event: IOevents.change_particle_type(event, settings.canvas))

    # Register the set_particle function from IOevents module to handle left-click events on the canvas
    settings.canvas.bind("<Button-1>", lambda event: IOevents.set_particle(event, settings.canvas))

    settings.root.mainloop()
    
