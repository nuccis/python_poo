import math

class Circle:
    def __init__(self, radius) -> None:
        self.radius = radius

    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if not isinstance(value, int | float) or value <= 0:
            raise ValueError('Positive number expected')
        self._radius = value

    def calculate_area(self):
        return round(math.pi * self._radius**2, 2)
    

#Programa principal

circulo = Circle(2)
print(circulo.radius)
print(circulo.__dict__)
print(circulo.calculate_area())