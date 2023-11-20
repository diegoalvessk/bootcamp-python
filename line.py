import math

class Line:
    
    def __init__(self, coordenada1, coordenada2, coordenada3, coordenada4):
        self.coordenada1 = coordenada1
        self.coordenada2 = coordenada2
        self.coordenada3 = coordenada3
        self.coordenada4 = coordenada4
    
    def distance(self):
        distance = math.sqrt((self.coordenada2 - self.coordenada1)**2 + (self.coordenada4 - self.coordenada3)**2)
        return distance

    def slope(self):
        if self.coordenada3 - self.coordenada1 != 0:  # Evita divisão por zero
            slope = (self.coordenada4 - self.coordenada2) / (self.coordenada3 - self.coordenada1)
            return slope
        else:
            return "Indefinido (divisão por zero)"

coordenada1 = int(input("Informe a coordenada 1: "))
coordenada2 = int(input("Informe a coordenada 2: "))
coordenada3 = int(input("Informe a coordenada 3: "))
coordenada4 = int(input("Informe a coordenada 4: "))

line = Line(coordenada1, coordenada2, coordenada3, coordenada4)

print("A distância entre as duas coordenadas é:", line.distance())

slope_result = line.slope()
print("O declive entre as duas coordenadas é:", slope_result)
