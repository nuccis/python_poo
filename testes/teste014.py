from datetime import datetime

#Classes
class Employee:
    company = 'Dog Inc' #Esse é um atributo de classe, e ele irá guardar o nome da empresa, o que é comum a todas as instâncias.

    def __init__(self, name, birth_date) -> None:
        self.name = name
        self.birth_date = birth_date

    def compute_age(self):
        today = datetime.today()
        age = today.year - self.birth_date.year
        if (today.month < self.birth_date.month) or (today.month == self.birth_date.month and today.day < self.birth_date.day):
            age -= 1
        return age
    
    def __str__(self) -> str:
        return f'{self.name} is {self.compute_age()} years old'
    
    def __repr__(self) -> str:
        return(f'{type(self).__name__}('
               f'name = {self.name}, '
               f'birth_date = {self.birth_date.strftime('%Y/%m/%d')})')
    
    @classmethod
    def from_dict(cls, data_dict):
        return cls(**data_dict)
        
    @property
    def birth_date(self):
        return self._birth_date
    
    @birth_date.setter
    def birth_date(self, value):
        self._birth_date = datetime.fromisoformat(value)

#Programa Principal
roberta = Employee('Roberta', '1999-05-02')
print(roberta.compute_age())

lista_func = [{'name':'Julia', 'birth_date':'2005-05-12'},{'name':'Fernanda', 'birth_date':'2004-08-21'}, {'name':'Renata', 'birth_date':'2002-02-03'}]
funcionarias = []
for v in lista_func:
    funcionaria = Employee.from_dict(v)
    funcionarias.append(funcionaria)

print(funcionarias)

#Printar o __str__
print('\nFuncionárias:')
for v in funcionarias:
    print(v)

#Printar o __repr__
print('\nFuncionárias:')
for v in funcionarias:
    print(repr(v))

#Printar o __dict__
print('\nFuncionárias:')
for v in funcionarias:
    print(vars(v))