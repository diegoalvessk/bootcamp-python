class Cylinder:
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius
    
    def volume(self):
        volume = 3.14 * (self.radius * self.radius) * self.height

        return volume
    
    def area(self):
        area = self.height + (2 * 3.14) * (self.radius * self.radius)

        return area

height = float(input("Informe a altura do cilindro" + " "))
radius = float(input("Informe o raio do cilindro" + " "))

cilindro = Cylinder(height, radius)
print("O volume do cilindro é " , " " , cilindro.volume())
print("A area do cilindro é " , " " , cilindro.area())