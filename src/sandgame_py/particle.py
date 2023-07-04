class Particle:
    def __init__(self, particle_type):
        self.particle_type = particle_type
        self.color = self.get_color()

    def get_color(self):
        # Return the color based on the particle type
        if self.particle_type == "Stone":
            return "gray"
        elif self.particle_type == "Sand":
            return "yellow"
        elif self.particle_type == "Water":
            return "blue"
        elif self.particle_type == "Air":
            return "light grey"  
        else:
            return "black" # Default color for unknown particle types
    



