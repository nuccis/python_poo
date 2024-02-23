#Crie um descritor chamado PositiveNumber que garanta que o valor de um atributo seja sempre um número positivo. Teste o descritor criado em uma classe chamada Product com um atributo price.

#Criação do descritor
class PositiveNumber:
    def __set_name__(self, owner, name):
        self.name = name
    
    def __get__(self, obj, type=None):
        return obj.__dict__.get(self.name)
    
    def __set__(self, obj, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError ('Era esperado um valor positivo')
        obj.__dict__[self.name] = value

#Criação da classe
class Product:
    price = PositiveNumber()


#Programa principal
leite = Product()
leite.price = 1
print(f'O preço do leite é {leite.price}')
