#Criação de classe

class DigitoNumerico: #Aqui eu estou criando a classe descritora
    def __set_name__(self, owner, name):
        self.name = name
    
    def __get__(self, obj, type=None) -> object:
        return obj.__dict__.get(self.name) or 0
    
    def __set__(self, obj, value) -> None:
        obj.__dict__[self.name] = value

class Numerico:
    numero = DigitoNumerico() #Aqui o nome da variavel, no caso 'numero', será sempre passado como parâmetro para o name do metodo __set_name__.

#Programa principal
    
numero01 = Numerico()
numero02 = Numerico()
numero03 = Numerico()
numero01.numero = 4
numero02.numero = 7
print(f'Numero 01 = {numero01.numero}')
print(numero01.__dict__)
print(f'Numero 02 = {numero02.numero}')
print(numero02.__dict__)
print(f'Numero 03 = {numero03.numero}')
print(numero03.__dict__)