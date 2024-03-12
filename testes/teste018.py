from abc import ABC, abstractmethod
from math import pi

#Classe Abstrata
#A não implementação de um método abstrato por uma de suas subclasses retorna um TypeError.
class Shape(ABC):
    @abstractmethod # Declara que é um método abstrato
    def get_area(self):
        pass

    @abstractmethod # Declara que é um método abstrato
    def get_perimeter(Self):
        pass

#Classes
class Circle(Shape):
    def __init__(self, radius) -> None:
        self.radius = radius
    
    def get_area(self):
        return pi * self.radius**2

    def get_perimeter(Self):
        return 2 * pi * Self.radius


class Square(Shape):
    def __init__(self, side) -> None:
        self.side = side

    def get_area(self):
        return self.side ** 2
    
    def get_perimeter(Self):
        return 4 * Self.side
    

#Programa Principal
circulo = Circle(4)
print(circulo.get_area())
print(circulo.get_perimeter())

quadrado = Square(2)
print(quadrado.get_area())
print(quadrado.get_perimeter())