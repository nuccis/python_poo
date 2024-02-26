#Implemente um descritor chamado ProtectedAttribute que permita que um atributo seja acessado apenas para leitura, mas não para escrita. Teste o descritor em uma classe chamada Person com atributos name (que pode ser lido e escrito) e age (que só pode ser lido).
#Descritor
class ProtectedAttribute:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, type=None):
        return obj.__dict__.get(self.name)
    
    def __set__ (self, obj, value):
        if self.name in obj.__dict__: #Aqui verifica se o atributo existe na instância
            raise AttributeError('Não é possível escrever nesse atributo')
        obj.__dict__[self.name] = value
#Classe
class Person:
    age = ProtectedAttribute()

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

#Programa principal
person = Person('Let', 28)
print(person.name)
print(person.age)
person.age = 47
