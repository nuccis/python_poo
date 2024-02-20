#Definição de classe
class Carro:
    def __init__(self, tamanho) -> None:
        self.__tamanho = tamanho
    
    def olharTamanho(self):
        return f'O tamanho do carro é {self.__tamanho}.'
    def __mudarTamanho(self,tamanho):
        self.__tamanho = tamanho


#Programa principal
vanzinha = Carro('médio')
#print(vanzinha.__tamanho) -> retorna uma erro
vanzinha._Carro__mudarTamanho('Grande')
print(vanzinha.olharTamanho())
print('\n dict de vanzinha:')
print(vars(vanzinha))
print('\n dict de Carro: ')
print(vars(Carro))
