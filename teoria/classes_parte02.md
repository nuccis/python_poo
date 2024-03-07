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