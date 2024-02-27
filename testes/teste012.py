#Classe
class Pizza:
    def __init__(self, ingredients) -> None:
        self.ingredients = ingredients
    
    def __repr__(self):
        return f'Pizza ({self.ingredients})'
    
    @classmethod
    def margherita(cls):
        return cls (['mozzarella', 'tomatoes'])# Está retornando uma nova instância de pizza com os ingredientes listados
    
    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham']) # Está retornando uma nova instância de pizza com os ingredientes listados


#Programa principal
pizzaria = Pizza('queijo')
print(pizzaria)
print(type(pizzaria))
pizza_marguerita = pizzaria.margherita()
print(pizza_marguerita)
print(type(pizza_marguerita))
pizza_pro = pizzaria.prosciutto()
print(pizza_pro)
print(type(pizza_pro))