#Implemente um descritor chamado ObservedAttribute que imprima uma mensagem toda vez que um atributo for acessado ou modificado. Teste o descritor em uma classe chamada Rectangle com atributos width e height.

#Descritor
class ObservedAttribute:
    def __set_name__(self, owner, name):
        self.name = name
    
    def __get__(self, obj, type=None):
        print(f'Acessando o atributo {self.name}')
        return obj.__dict__.get(self.name)
    
    def __set__(self, obj, value):
        print(f'Configurando o valor {self.name}')
        obj.__dict__[self.name] = value

#Classe
class Rectangle:
    largura = ObservedAttribute()
    comprimento = ObservedAttribute()

#Programa principal
retangulo = Rectangle()
retangulo.largura = 20
retangulo.comprimento = 10
print(f'O comprimento é: {retangulo.comprimento}')
print(f'A largura é: {retangulo.largura}')