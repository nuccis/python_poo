### Definição  
Em resumo, uma classe serve de forma que pode ser usada para criar vários objetos.  
Uma classe possui **atributos**, que é conhecido por guardar o estado de um objeto, e também possui **métodos**, que definem os diferentes comportadamentos do objeto.  
- atributos: cor, altura, tamanho...
- métodos: correr, andar, dirigir, acender_a_luz...

### Pilares da POO
1. **Herança:** a herança permite que uma classe adquira as propriedades e métodos de outra classe. A reutilização de código é o principal benefício.
1. **Abstração:** trata-se de esconder os detalhes da implementação dentro de algo, às vezes um protótipo, às vezes em uma função.
exemplo:  
Vamos criar uma máquina de café:  

    1. Como criá-la com abstração:  
        - Ter um botão escrito "Fazer café"
    1. Como criá-la sem abstração:
        - Ter um botão escrito "Adicionar água fria à chaleira"
        - Ter um botão escrito "Ferver a água"
        - Ter um botão escrito "Adicionar uma cápsula de café"
        - Ter um botão escrito "Passar a água pela cápsula de café"

1. **Encapsulamento:** é a ação de colocar algo dentro ou como se estivesse em uma cápsula. Remover o acesso a partes do seu código e tornar as coisas privada é exatamente o que o Encapsulamento faz. Limita o acesso à determinados dados.
1. **Polimorfismo:** é a condição de ocorrer de várias formas diferentes. Ou seja, o polimorfismo consiste na alteração do funcionamento interno de um método herdado de um objeto pai. Exemplo: temos um objeto genérico “Eletrodoméstico”. Esse objeto possui um método, ou ação, “Ligar()”. Temos dois objetos, “Televisão” e “Geladeira”, que não irão ser ligados da mesma forma. Assim, precisamos, para cada uma das classes filhas, reescrever o método “Ligar()”.  

### Definindo uma classe em Python

Podemos definir uma classe da seguinte maneira:  
    
    class ClassName:  
        # Class body  
        pass

Podemos definir os atributos na inicialização do objeto através do método \_\_init__. Exemplo de classe:  
  
    import math

    class Circle:
        def __init__(self, radius):
            self.radius = radius #atributo

        def calculate_area(self): #método
            return round(math.pi * self.radius ** 2, 2)

Acessar métodos e atributos:  
  
    obj.attribute_name

    obj.method_name()