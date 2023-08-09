########################################################## PARTICLES ##########################################################
class Particle:
    # "constructor" for a particle
    def __init__(self, type, x_pos, y_pos):
        self.type  = type
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.color = self.get_color()
    
    # get/set the color of the Particle determined by its type
    def get_color(self):
    
        if self.type == "Stone":
            return "gray"
        elif self.type == "Sand":
            return "yellow"
        elif self.type == "Water":
            return "blue"
        elif self.type == "Air":
            return "light grey"  
        else:
            # Default color for unknown particle types
            return "black" 

    # get the position of a particle (right now only needed for debugging)
    def get_pos(self):
        #returns tuple of x- and y-coordinates like so -> {x-coord, y-coord}
        pos = (self.x_pos, self.y_pos)
        return pos