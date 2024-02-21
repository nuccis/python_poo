#Definição de classe
class Person:
    pass

#Definição de dado
john = {
    "name": "John Doe",
    "position": "Python Developer",
    "department": "Engineering",
    "salary": 80000,
    "hire_date": "2020-01-01",
    "is_manager": False,
}

#Programa Principal
print('\nPerson dict:')
print(vars(Person))

john_person = Person()

for key, value in john.items():
    setattr(john_person, key, value)

print('\nJohn dict:')
print(vars(john_person))

jane_person = Person()
jane_person.name = 'Jane Doe'
jane_person.job = 'Data Engineer'
print('\nJane dict:')
print(jane_person.__dict__)

#Há a possibilidade de adicionar métodos dinamicamente tbm

def __init__(self, name, job):
    self.name = name
    self.job = job

Person.__init__ = __init__
print('\nPerson dict:')
print(vars(Person))

let = Person('Leticia', 'Engineer')
print('\nlet dict:')
print(vars(let))
