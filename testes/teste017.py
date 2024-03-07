#Classes
class Trabalhador:
    def __init__(self, nome, endereco, salario_hora) -> None:
        self.nome = nome
        self.endereco = endereco
        self.salario_hora = salario_hora
    
    def mostrar_perfil(self):
        print('== Perfil do Trabalhador ==\n'
              f'Nome: {self.nome}\n'
              f'Endereço: {self.endereco}\n'
              f'Salário hora: {self.salario_hora}')
    
    def calcular_salario(self, horas=40):
        return self.salario_hora * horas


class Gerente(Trabalhador):
    def __init__(self, nome, endereco, salario_hora, hora_bonus) -> None:
        super().__init__(nome, endereco, salario_hora)
        self.hora_bonus = hora_bonus
    
    def calcular_salario(self, horas=40):
        return (self.salario_hora + self.hora_bonus) * horas


#Programa principal
let = Trabalhador('Leticia', 'Rua 01', 18)
print(f'Salario semanal: {let.calcular_salario()}')

lea = Gerente('Lea', 'Rua 02', 18, 8)
print(f'Salario semanal: {lea.calcular_salario()}')