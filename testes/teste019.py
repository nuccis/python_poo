#Classe
class Veiculo:
    def __init__(self, make, model, year) -> None:
        self.make = make
        self.model = model
        self.year = year
        self._started = False
    
    def start(self):
        print('Starting engine...')
        self._started = True
    
    def stop(self):
        print('Stopping engine...')
        self._started = False

class Carro(Veiculo):
    def __init__(self, make, model, year, num_seats) -> None:
        super().__init__(make, model, year)
        self.num_seats = num_seats
    
    def drive(self):
        print(f'Dirigindo meu "{self.make} - {self.model}" na estrada.')
    
    def __str__(self) -> str:
        return f'"{self.make} - {self.model}" tem {self.num_seats} assentos'


class Moto(Veiculo):
    def __init__(self, make, model, year, num_wheels) -> None:
        super().__init__(make, model, year)
        self.num_wheels = num_wheels
    
    def drive(self):
        print(f'Pilotando minha "{self.make} - {self.model}" na estrada.')
        
    def __str__(self) -> str:
        return f'"{self.make} - {self.model}" tem {self.num_wheels} rodas'


#Programa Principal

ford_ka = Carro('Ford','Ka', 2013, 5)
mt_07 = Moto('Yamaha', 'MT-07', 2022, 2)

for vei in [ford_ka, mt_07]:
    vei.drive()
#alteração