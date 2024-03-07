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
