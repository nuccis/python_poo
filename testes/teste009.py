#Classe
class Point:
    __slots__ = ('x', 'y')
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

#Programa principal
point = Point(4 ,8)
print(f'x = {point.x}')
print(f'y = {point.y}')
#point.__dict__ #retorna um AttributeError
#point.z = 7 #também retorna um AttributeError