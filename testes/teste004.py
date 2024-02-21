#Criação de classe
class Carro:
    def __init__(self, make, model, year, color) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.started = False
        self.speed = 0
        self.max_speed = 200


#Programa principal
print('Toyota Camry:')
toyota_camry = Carro('Toyota', 'Camry',2022, 'Red')
print(toyota_camry.color)
print(toyota_camry.year)
print('Ford Ka:')
ford_Ka = Carro('Ford', 'KA', 2013, 'Branco')
print(ford_Ka.color)
print(ford_Ka.model)