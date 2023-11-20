import math

class Line:
    
    def __init__(self, coordenadas1, coordenadas2):
        self.coordenadas1 = coordenadas1
        self.coordenadas2 = coordenadas2
    
    def distance(self):
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        return distance

coordenada1 = input("Informe a coordenada 1")
coordenada2 = input("Informe a coordenada 2")

line = Line(coordenada1, coordenada2)