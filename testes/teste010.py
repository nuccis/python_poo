#Classe
class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.started = False
        self.speed = 0
        self.max_speed = 200

    def start(self):
        print("Starting the car...")
        self.started = True

    def stop(self):
        print("Stopping the car...")
        self.started = False
    
    def accelerate(self, value):
        if not self.started:
            print('O carro não está ligado!')
            return
        if self.speed + value <= self.max_speed:
            self.speed += value
        else:
            self.speed = self.max_speed
        print(f'Acelerando o carro para {self.speed} km/h...')
    
    def brake(self, value):
        if self.speed - value >= 0:
            self.speed -= value
        else:
            self.speed = 0
        print(f'Freiando o carro para {self.speed} km/h...')

#Programa principal
rebeca = Car('Ford', 'Ka', 2013, 'Branco')
rebeca.accelerate(30)
rebeca.start()
rebeca.accelerate(30)
rebeca.brake(20)
rebeca.stop()
