class Box:
    def __init__(self):
        self.text = ""
        self.colour = "white"  # Default color

    def set_text(self, text):
        self.text = text

    def set_colour(self, colour):
        self.colour = colour

    def get_text(self):
        return self.text

    def get_colour(self):
        return self.colour

    def reset(self):
        self.set_text("")
        self.set_colour("white")
