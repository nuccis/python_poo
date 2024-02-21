#Criação de classe
class SampleClass:
    class_attr = 100

    def __init__(self, instance_attr) -> None:
        self.instance_attr = instance_attr
    
    def method(self):
        print(f'Atributo de classe: {self.class_attr}')
        print(f'Atributo de instância: {self.instance_attr}')


#Programa principal
caso1 = SampleClass(12)
caso1.method()
print('\nDict da classe SampleClass: ')
print(SampleClass.__dict__)
print('\nDict da instância caso1: ')
print(caso1.__dict__)