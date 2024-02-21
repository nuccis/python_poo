#Criação de classe
class Lapis:
    num_instanc = 0
    def __init__(self) -> None:
        type(self).num_instanc += 1 #A função type retorna a classe ou o tipo de self, que nesse caso seria Lapis.


#Programa principal
lapis01 = Lapis()
lapis02 = Lapis()
lapis03 = Lapis()

print(Lapis.num_instanc)#Posso olhar o atributo de classe através da classe
print(lapis01.num_instanc)#ou através de uma de suas instâncias

#Não é possível modificar um atributo de classe através de suas instâncias. Fazendo isso irá apenas criar um novo atributo da instância que irá sobrescrecer o atributo da classe.

