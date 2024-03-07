#Classes
class Aircraft:
    def __init__(self, impulso, subir, max_speed) -> None:
        self.impulso = impulso
        self.subir = subir
        self.max_speed = max_speed
    
    def especificaoes_tecnicas(self):
        print(f'Impulso: {self.impulso} kW\n'
              f'Subir: {self.subir} kg\n'
              f'Max speed: {self.max_speed} km/h')

class Helicopter(Aircraft):
    def __init__(self, impulso, subir, max_speed, num_rotors) -> None:
        super().__init__(impulso, subir, max_speed)
        self.num_rotors = num_rotors
    
    def especificaoes_tecnicas(self):
        super().especificaoes_tecnicas()
        print(f'Numero de rotores: {self.num_rotors}')


#Programa principal
aeronave = Aircraft(3589, 1000, 2000)
aeronave.especificaoes_tecnicas()

helio = Helicopter(2459, 3000, 1200, 4)
helio.especificaoes_tecnicas()