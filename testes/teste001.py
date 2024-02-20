#Definição de Classes
class ClassName: #Primeira letra sempre maiúscula
    #class body
    pass

class Casa:
    def __init__(self, cor) -> None:
        self.cor = cor
    
    def mostrar_cor(self):
        return self.cor


#Código principal
casinha = Casa('amarelo')
print(f'A cor da casinha é: {casinha.mostrar_cor()}')
casinha.cor = 'azul'
print(f'A cor da casinha é: {casinha.mostrar_cor()}')
print('\n dict de casinha:')
print(vars(casinha))
print('\n dict de Casa: ')
print(vars(Casa))