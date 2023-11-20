class Cylinder:
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius
    
    def volume(self):
        volume = 3.14 * (self.radius * self.radius) * self.height