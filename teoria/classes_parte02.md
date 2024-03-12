## Classes - Parte 02
### Usando heranças e construindo hierarquias de classe
Herança consiste na criação de relacionamentos hierárquicos entre classes, onde as classes filhas herdam atributos e métodos de sua classe pai. Em Python, uma classe pode ter vários pais ou, mais amplamente, ancestrais.  
Abaixo temos a sintaxe básica de uma herança:

    class Parent:
        # Parent's definition goes here...
        pass

    class Child(Parent):
        # Child definitions goes here...
        pass

Uma hierarquia de classe é um conjunto de classes intimamente relacionadas que são conectadas através de herança e organizadas em uma estrutura semelhante a uma árvore.  
A classe ou as classes no topo da hierarquia são as classes bases, enquanto as classes abaixo são classes derivadas ou subclasses.  
Abaixo temos um diagrama de classe para melhor exemplificar hierarquia de classe:
![Hierarquia de Classe](/teoria/image/hierarquia_de_classes.png)

Além da herança temos outras relação entre classes, como por exemplo:
- **Composição**: expressa uma relação **has-a do tipo forte**. Por exemplo, um robo tem um braço. Se o robo deixar de existir, então o braço deixa de existir também;
- **Agregação**: expressa uma relação **has-a do tipo fraca**. Por exemplo, uma universidade tem um instrutor. Se a universidade deixar de existir, o instrutor não deixará de existir;

### Métodos Estendidos vs Métodos Sobrescritos
Quando um método fornecido pela classe mãe não nos atende ou atende de maneira muito básica, podemos usar dois recursos:
- **Estender** um método herdado na subclasse, o que significa que você irá reusar a funcionalidade fornecidade pela superclasse e adicionar novas funcionalidades.
- **Sobrescrever** um método herdado na subclasse, o que significa que você irá descartar completamente a funcionalidade advinda da superclasse e forneça uma nova funcionalidade em uma subclasse.  
Olhar exemplos de aplicação nos testes 16 e 17.

### Herança múltipla
Este tipo de herança permite a você criar classes que herdam de vários pais. A subclasse irá ter acesso aos atributos e métodos de todos os seus pais.  
Esse recurso deve ser usando com muito cuidado, pois podem ocasionar problemas como o "problema do diamante".  
Quando estamos utilizando múltipla herança, podemos nos deparar com situações onde uma classe herda de duas ou mais classes que tem a mesma classe base. Isto é conhecido como o "problema do diamante". O real problema aparece quando múltiplos pais fornecem versões específicas do mesmo método. Neste caso, seria difícil determinar qual versão do método a subclasse iria utilizar.  
![mro](/teoria/image/mro.png)  
Para resolver este problema Python implementa um algoritmo chamado "method resolution order (MRO)". Este algoritmo diz ao programa como procurar por um método em um contexto de múltipla herança. Em geral, Python procura por métodos e atributos seguindo a seguinte ordem:  

1. The current class;
1. The leftmost superclasses;
1. The superclass listed next, from left to right, up to the last superclass;
1. The superclasses of inherited classes;
1. The object class;  

No exemplo ilustrativo abaixo, quando chamamos **D().method()**, ele retorna **B.method**.  
![mro_1](/teoria/image/mro_1.png)

Pode-se também checar o atual MRO de uma dada classe utilizando o atributo especial .\_\_mro__:
![mro_2](/teoria//image/mro_2.png)  

### Mixin Classes
Uma classe mixin fornece métodos que você pode reutilizar em várias classes. Classes mixin não definem novos tipos, logo elas não
se destinam a serem instanciadas.  
![mixin](/teoria/image/mixin.png)  

### Usando alternativas à Herança
#### 1.1. Herança
É um tipo de relação **is-a (é-um/uma)**. Por exemplo:
- O Gato (classe) **é um** Mamífero (classe);
- O Carro (classe) **é um** Veículo (classe).

Neste tipo de relação uma classe deriva de outra, consequentemente herdando os atributos de sua classe-mãe e todas anteriores à ela (caso exista).  
Exemplo de código utilizando herança:

    class Animal:
        def __init__(self, name, sex, habitat):
            self.name = name
            self.sex = sex
            self.habitat = habitat

    class Mammal(Animal):
        unique_feature = "Mammary glands"

#### 1.2. Composição
É um tipo forte de relação **has-a (tem-um/uma)**. Por exemplo: 

- Um Funcionário(classe) **tem uma** Identidade (classe);
- Um Robo (classe) **tem um** Braço (classe).  

Neste tipo de relação, caso o Funcionário ou o Robo deixe de exister, a Identidade e o Braço, respectivamente, deixarão de existir.  
Exemplo de código utilizando composição:

    class Salary:
        def __init__(self, monthly_income):
            self.monthly_income = monthly_income
    
        def get_total(self):
            return (self.monthly_income*12)
    
    class Employee:
        def __init__(self, monthly_income, bonus):
            self.monthly_income = monthly_income
            self.bonus = bonus
            self.obj_salary = Salary(self.monthly_income)
    
        def annual_salary(self):
            return "Total: " + str(self.obj_salary.get_total() + self.bonus) + ' €' 

#### 1.3. Agregação
É um tipo de relação **has-a (tem-um/uma)**, porém suave. Por exemplo:

- Uma Universidade (classe) **tem um** Instrutor (classe);
- Um Barbaro (classe) **tem uma** Adaga (classe).

Neste tipo de relação, caso a Universidade ou o Barbaro deixe de existir, o Instrutor e a Adaga, respectivamente, **NÃO** deixarão de existir.  
Exemplo de código utilizando agregação:

    class Salary: 
        def __init__(self, pay, bonus): 
            self.pay = pay 
            self.bonus = bonus 
    
        def annual_salary(self): 
            return (self.pay*12)+self.bonus 

    class Employee: 
        def __init__(self, name, age, sal): 
            self.name = name 
            self.age = age 
            self.agg_salary = sal   #Agregação 
    
        def total_sal(self): 
            return self.agg_salary.annual_salary()

    salary = Salary(10000, 1500)
    emp = Employee('Vi', 25, salary) #a instância emp de Employee recebe o objeto salary como um de seus parâmetros de inicialização

### Criando Abstract Base Classes (ABCs) e interfaces
Em determinadas situações queremos criar uma hierarquia de classe na qual todas as classes implementem uma interface predefinida ou API (Interface de Programação de Aplicativos), ou seja, queremos definir um conjunto específico de métodos e atributos públicos que todas as classes participantes da hierarquia devem implementar. Em Python nós utilizamos o módulo abc.  
Uma classe ABC não pode ser instanciada diretamente, ela funciona como um template para a criação das outras classes.  
**Olhar o teste 018 para exemplo de código.**

### Desbloqueando polimorfismo com interfaces comuns
Polimorfismo é quando você pode usar objetos de diferentes classes de forma intercambiável porque eles compartilham uma interface comum.
Como no nosso teste 015, podemos mudar o método .ride() para .drive na classe Motocicleta, e assim ter uma interface comum entre Motocicleta e Carro. Podendo assim utilizar as duas de forma intercambiável, como no exemplo abaixo:  
![polimorfismo](/teoria/image/polimorfismo.png)
