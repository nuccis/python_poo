import math

#Classes
class Pizza:
    def __init__(self, radius, ingredients) -> None:
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self) -> str:
        return (f'{type(self).__name__} (radius = {self.radius}, 'f'ingredients = {self.ingredients})')
    
    def area(self):
        return self.circle_area(self.radius)
    
    @staticmethod
    def circle_area(r):
        return f'{(r ** 2 * math.pi):.2f}'

#Programa principal

pizzaria = Pizza(8, ['Mozzarella', 'tomatoes'])
print(pizzaria)
print(pizzaria.area())
print(pizzaria.circle_area(2))