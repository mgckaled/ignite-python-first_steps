# Anotações Módulo 2 - Programação Orientada a Objetos

> [voltar](../../README.md) para página anterior

## Sumário

- [Anotações Módulo 2 - Programação Orientada a Objetos](#anotações-módulo-2---programação-orientada-a-objetos)
  - [Sumário](#sumário)
  - [Conteúdo](#conteúdo)
    - [O que é POO?](#o-que-é-poo)
      - [Herança](#herança)
      - [Polimorfismo](#polimorfismo)
      - [Encapsulamento](#encapsulamento)
      - [Abstração](#abstração)
      - [Herança Múltipla](#herança-múltipla)
    - [Decoradores](#decoradores)
    - [Criação de Classes em Python](#criação-de-classes-em-python)
  - [Dicas Importantes](#dicas-importantes)
    - [Uso do `self`](#uso-do-self)
    - [Uso da classe `NotImplementedError`](#uso-da-classe-notimplementederror)

## Conteúdo

### O que é POO?

POO em Python refere-se à Programação Orientada a Objetos em Python. A Programação Orientada a Objetos (POO) é um paradigma de programação que utiliza conceitos como classes e objetos para organizar o código de maneira mais modular, reutilizável e estruturada. Em Python, POO é suportada de forma nativa, e é uma abordagem muito poderosa para resolver problemas complexos.

1. **Classe:** Uma classe é um modelo para criar objetos. Define propriedades e comportamentos que os objetos criados a partir dela terão.

    ```python
    class Carro:
        def __init__(self, modelo, cor):
            self.modelo = modelo
            self.cor = cor

        def acelerar(self):
            print(f"{self.modelo} acelerando...")
    ```

2. **Objeto:** Um objeto é uma instância de uma classe. É uma entidade que possui características específicas e pode realizar ações.

    ```python
    meu_carro = Carro("Sedan", "Azul")
    meu_carro.acelerar()
    ```

3. **Atributos:** Propriedades da classe que armazenam dados.

    ```python
    print(meu_carro.modelo)  # Saída: Sedan
    print(meu_carro.cor)     # Saída: Azul
    ```

4. **Métodos:** Funções dentro de uma classe que definem o comportamento dos objetos.

    ```python
    meu_carro.acelerar()  # Saída: Sedan acelerando...
    ```

5. **Herança:** Um mecanismo que permite que uma classe herde características de outra classe.

    ```python
    class CarroEsportivo(Carro):
        def turbo(self):
            print("Turbo ativado!")

    carro_esportivo = CarroEsportivo("Esportivo", "Vermelho")
    carro_esportivo.acelerar()  # Herda o método da classe pai
    carro_esportivo.turbo()     # Novo método específico
    ```

6. **Encapsulamento:** Restrição do acesso direto aos atributos de uma classe, incentivando o uso de métodos para acessar e modificar esses atributos.

    ```python
    class ContaBancaria:
        def __init__(self, saldo):
            self.__saldo = saldo  # Atributo privado

        def get_saldo(self):
            return self.__saldo

        def depositar(self, valor):
            self.__saldo += valor

    conta = ContaBancaria(1000)
    print(conta.get_saldo())  # Saída: 1000
    conta.depositar(500)
    print(conta.get_saldo())  # Saída: 1500
    ```

Utilizar a POO proporciona uma estrutura mais organizada, reutilizável e fácil de entender para o código. Para obter mais informações, você pode consultar a [documentação oficial do Python sobre Programação Orientada a Objetos](https://docs.python.org/3/tutorial/classes.html).

> [retornar](#anotações-módulo-2---programação-orientada-a-objetos) para o topo da página

#### Herança

A herança é um conceito fundamental na programação orientada a objetos (POO) em Python, assim como em muitas outras linguagens de programação. Ela permite que uma classe herde atributos e métodos de outra classe, promovendo a reutilização de código e a criação de hierarquias de classes.

A classe que é herdada é chamada de classe base ou classe mãe, e a classe que herda é chamada de classe derivada ou classe filha. A classe derivada pode estender ou modificar o comportamento da classe base, adicionando novos métodos, sobrescrevendo métodos existentes ou adicionando novos atributos.

Principais conceitos de herança em Python:

1. **Sintaxe:**

   ```python
   class ClasseBase:
       # Atributos e métodos da classe base

   class ClasseDerivada(ClasseBase):
       # Atributos e métodos adicionais ou modificados
   ```

2. **Acesso a membros da classe base:**
   - Os membros públicos (atributos e métodos) da classe base são acessíveis diretamente pela classe derivada.

3. **Método `super()`:**
   - Utilizado para chamar um método da classe base a partir da classe derivada.

   ```python
   class ClasseBase:
       def metodo(self):
           print("Método da ClasseBase")

   class ClasseDerivada(ClasseBase):
       def metodo(self):
           super().metodo()
           print("Método da ClasseDerivada")
   ```

4. **Sobrescrita de métodos:**
   - A classe derivada pode fornecer uma implementação específica para um método já definido na classe base.

5. **Herança Múltipla:**
   - Em Python, uma classe pode herdar de mais de uma classe, permitindo maior flexibilidade na criação de hierarquias.

   ```python
   class ClasseBase1:
       # ...

   class ClasseBase2:
       # ...

   class ClasseDerivada(ClasseBase1, ClasseBase2):
       # ...
   ```

6. **MRO (Method Resolution Order):**
   - A ordem na qual as classes base são pesquisadas para encontrar um método é determinada pelo MRO. Pode ser acessado usando `ClasseDerivada.__mro__`.

   ```python
   print(ClasseDerivada.__mro__)
   ```

No dia a dia do programador, a herança é usada para criar hierarquias de classes, promovendo a reutilização de código e facilitando a manutenção do software. No entanto, o uso excessivo de herança pode levar a um código complexo e difícil de entender. É importante equilibrar a reutilização de código com a modularidade e clareza do design.

Link para a documentação oficial de Python sobre herança: [Python - Herança](https://docs.python.org/3/tutorial/classes.html#inheritance)

> [retornar](#anotações-módulo-2---programação-orientada-a-objetos) para o topo da página

#### Polimorfismo

Polimorfismo é um dos quatro pilares da programação orientada a objetos (POO), juntamente com encapsulamento, herança e abstração. Em termos simples, o polimorfismo permite que objetos de diferentes classes sejam tratados de maneira uniforme, desde que implementem métodos ou atributos comuns. Em Python, o polimorfismo é frequentemente associado ao conceito de "duck typing", que se refere à capacidade de um objeto ser usado com base em seu comportamento, em vez de sua classe ou tipo específico.

Existem dois tipos principais de polimorfismo em Python: polimorfismo de sobrecarga e polimorfismo de interface.

1. **Polimorfismo de Sobrecarga (ou Ad-hoc):**
   - Refere-se à capacidade de uma classe fornecer implementações específicas de métodos que são comuns a todas as classes base.
   - O polimorfismo de sobrecarga em Python é alcançado por meio da utilização de funções ou métodos com o mesmo nome, mas diferentes tipos ou números de parâmetros.
   - Exemplo:

    ```python
    class Calculadora:
        def soma(self, a, b):
            return a + b

        def concatena(self, a, b):
            return str(a) + str(b)

    calc = Calculadora()
    resultado_soma = calc.soma(2, 3)
    resultado_concat = calc.concatena("Olá, ", "Mundo!")
    ```

2. **Polimorfismo de Interface (ou por Subtipo):**
   - Refere-se à capacidade de diferentes classes implementarem uma mesma interface (métodos ou atributos) de maneiras diferentes.
   - Em Python, não há necessidade explícita de declarar interfaces, pois a linguagem permite que classes diferentes implementem métodos comuns de maneiras diferentes.
   - Exemplo:

    ```python
    class Animal:
        def fazer_som(self):
            pass

    class Cachorro(Animal):
        def fazer_som(self):
            return "Au Au!"

    class Gato(Animal):
        def fazer_som(self):
            return "Miau!"

    def faz_barulho(animal):
        return animal.fazer_som()

    dog = Cachorro()
    cat = Gato()

    print(faz_barulho(dog))  # Saída: Au Au!
    print(faz_barulho(cat))  # Saída: Miau!
    ```

No dia a dia do programador, o polimorfismo em Python proporciona flexibilidade e reutilização de código. Ele permite que você escreva código mais genérico, tornando-o menos dependente de tipos específicos e mais adaptável a mudanças. Isso facilita a manutenção do código e o torna mais robusto.

A documentação oficial do Python pode ser encontrada no site oficial: [Documentação Oficial do Python](https://docs.python.org/3/)

> [retornar](#anotações-módulo-2---programação-orientada-a-objetos) para o topo da página

#### Encapsulamento

O encapsulamento é um dos princípios fundamentais da Programação Orientada a Objetos (POO) e refere-se à ideia de agrupar os dados (atributos) e os métodos (funções) que operam nesses dados em uma única unidade, chamada de classe. O principal objetivo é ocultar os detalhes de implementação internos da classe, fornecendo uma interface externa consistente e controlada para interagir com os objetos.

Em Python, o encapsulamento é implementado através do uso de convenções e modificadores de acesso. Embora Python não tenha modificadores de acesso estritos como algumas outras linguagens de programação (por exemplo, public, private, protected), a comunidade Python segue uma convenção de nomenclatura para indicar a visibilidade de um atributo ou método. Os principais são:

1. **Público:** Atributos ou métodos sem um sublinhado são considerados públicos e podem ser acessados de qualquer lugar, tanto dentro como fora da classe.

    ```python
    class Exemplo:
        def metodo_publico(self):
            return "Método público"
        
        atributo_publico = "Atributo público"
    ```

2. **Protegido:** Atributos ou métodos com um sublinhado único no início (como `_atributo_protegido`) são considerados protegidos. Embora ainda possam ser acessados, a convenção sugere que eles não devem ser usados fora da classe ou de suas subclasses.

    ```python
    class Exemplo:
        def _metodo_protegido(self):
            return "Método protegido"
        
        _atributo_protegido = "Atributo protegido"
    ```

3. **Privado:** Atributos ou métodos com dois sublinhados no início (como `__atributo_privado`) são considerados privados. A intenção é torná-los inacessíveis fora da classe.

    ```python
    class Exemplo:
        def __metodo_privado(self):
            return "Método privado"
        
        __atributo_privado = "Atributo privado"
    ```

É importante notar que essas são apenas convenções, e Python confia na responsabilidade do programador para respeitá-las. A linguagem não impede o acesso direto a atributos ou métodos, mesmo que sejam considerados privados.

O encapsulamento em Python, portanto, é mais uma questão de convenção e boas práticas do que uma aplicação rigorosa de restrições de acesso. Isso permite uma maior flexibilidade, mas também requer uma disciplina cuidadosa por parte dos desenvolvedores para garantir o uso correto e seguro das classes.

Aqui está o link para a documentação oficial do Python, onde você pode encontrar mais informações sobre encapsulamento e outros conceitos relacionados à programação orientada a objetos em Python: [Documentação Oficial do Python - Classes](https://docs.python.org/3/tutorial/classes.html)

> [retornar](#anotações-módulo-2---programação-orientada-a-objetos) para o topo da página

#### Abstração

Em programação orientada a objetos (POO), a abstração é um dos pilares fundamentais, juntamente com encapsulamento, herança e polimorfismo. A abstração refere-se à capacidade de representar conceitos complexos de forma simplificada, permitindo que os desenvolvedores foquem nos aspectos relevantes de um objeto e ignorem detalhes menos importantes.

No contexto de POO em Python, a abstração é implementada por meio de classes e objetos. Uma classe é uma estrutura que encapsula dados (atributos) e comportamentos (métodos) relacionados a um determinado conceito. Um objeto é uma instância de uma classe, representando uma entidade específica.

Vamos explorar como a abstração é aplicada no dia a dia do programador em Python:

1. **Definição de Classes:** Ao projetar um sistema, os programadores identificam entidades e conceitos relevantes, representando-os como classes. Por exemplo, se estivermos desenvolvendo um sistema bancário, poderíamos ter classes como `ContaBancaria`, `Cliente`, etc.

   ```python
   class ContaBancaria:
       def __init__(self, numero_conta, saldo):
           self.numero_conta = numero_conta
           self.saldo = saldo

       def depositar(self, valor):
           self.saldo += valor

       def sacar(self, valor):
           if valor <= self.saldo:
               self.saldo -= valor
           else:
               print("Saldo insuficiente.")
   ```

2. **Criação de Objetos:** Os objetos são instâncias de classes, representando entidades específicas no sistema. Por exemplo, podemos criar uma conta bancária para um cliente específico.

   ```python
   conta_cliente1 = ContaBancaria(numero_conta="12345", saldo=1000.0)
   ```

3. **Chamada de Métodos:** Os métodos de uma classe representam os comportamentos associados a essa entidade. No exemplo acima, podemos depositar e sacar dinheiro usando os métodos `depositar` e `sacar` da classe `ContaBancaria`.

   ```python
   conta_cliente1.depositar(500.0)
   conta_cliente1.sacar(200.0)
   ```

4. **Abstração de Detalhes Internos:** O programador pode interagir com as classes e objetos sem se preocupar com os detalhes internos da implementação. Isso permite uma visão mais simplificada e focada nos conceitos relevantes.

A documentação oficial do Python é uma excelente fonte para aprender mais sobre abstração e outros conceitos de POO na linguagem. Aqui está o link para a documentação oficial do Python: [Documentação Oficial do Python](https://docs.python.org/3/)

> [retornar](#anotações-módulo-2---programação-orientada-a-objetos) para o topo da página

#### Herança Múltipla

A herança múltipla em programação orientada a objetos (POO) é um conceito que permite que uma classe herde atributos e métodos de mais de uma classe pai. Em Python, uma linguagem que suporta herança múltipla, uma classe pode ser derivada de várias classes pai. Isso oferece flexibilidade, mas também pode introduzir complexidade no código.

Aqui estão algumas informações relevantes sobre herança múltipla em Python:

1. **Sintaxe:**
   - A sintaxe para herança múltipla em Python é bastante direta. Ao definir uma nova classe, você pode listar várias classes pai separadas por vírgulas, como no exemplo abaixo:

     ```python
     class ClasseFilha(ClassePai1, ClassePai2, ClassePai3):
         # corpo da classe filha
     ```

2. **Ordem de Resolução de Métodos (MRO):**
   - Python usa o conceito de MRO para determinar a ordem em que as classes pai são percorridas ao procurar por métodos ou atributos. A função `mro()` pode ser usada para visualizar a ordem de resolução de métodos.

     ```python
     print(ClasseFilha.mro())
     ```

3. **Problemas Potenciais:**
   - A herança múltipla pode levar a problemas de ambiguidade se houver métodos ou atributos com o mesmo nome em classes pai diferentes.
   - A complexidade aumenta à medida que mais classes pai são envolvidas, tornando a hierarquia mais difícil de entender e manter.

4. **Mixins:**
   - Os mixins são classes pequenas e especializadas que fornecem funcionalidades específicas. Eles são frequentemente usados em herança múltipla para compartilhar funcionalidades entre diferentes classes sem criar uma hierarquia profunda.

5. **Uso Prático:**
   - Herança múltipla é frequentemente usada para modelar objetos do mundo real que têm características de várias fontes.
   - Em frameworks e bibliotecas, herança múltipla é usada para criar classes que herdam funcionalidades de várias classes base.

6. **Super():**
   - A função `super()` é usada para chamar métodos das classes pai de forma mais explícita, evitando chamadas diretas e melhorando a manutenção do código.

   ```python
   class ClasseFilha(ClassePai1, ClassePai2):
       def metodo_na_classe_filha(self):
           super().metodo_na_classe_filha()  # chama o método da primeira classe pai
   ```

**Documentação Oficial:** [Documentação Python - Herança Múltipla](https://docs.python.org/3/tutorial/classes.html#multiple-inheritance)

> [retornar](#anotações-módulo-2---programação-orientada-a-objetos) para o topo da página

### Decoradores

Em Python, decoradores são uma forma poderosa e flexível de modificar ou estender o comportamento de funções ou métodos. Eles são comumente usados para encapsular funcionalidades adicionais em torno de funções existentes sem modificar diretamente o código fonte dessas funções. Decoradores são aplicados usando a sintaxe `@decorator` acima da definição de uma função.

Aqui estão alguns conceitos e informações relevantes sobre decoradores em Python:

1. **Funções de ordem superior:**
   - Em Python, funções são tratadas como cidadãos de primeira classe, o que significa que podem ser passadas como argumentos para outras funções e até mesmo retornadas por outras funções. Essa característica é fundamental para entender decoradores.

2. **Sintaxe de Decorador:**
   - Decoradores são funções que aceitam uma função como argumento e retornam uma nova função modificada. A sintaxe básica é `@decorator` antes da definição da função.

   ```python
   @decorator
   def minha_funcao():
       # corpo da função
   ```

3. **Exemplo Simples:**
   - Um exemplo básico de decorador seria um que imprime uma mensagem antes e depois da execução de uma função:

   ```python
   def meu_decorador(funcao):
       def wrapper():
           print("Antes da execução da função.")
           funcao()
           print("Depois da execução da função.")
       return wrapper

   @meu_decorador
   def minha_funcao():
       print("Executando minha função.")

   minha_funcao()
   ```

   Neste exemplo, `meu_decorador` é o decorador que modifica o comportamento de `minha_funcao`.

4. **Múltiplos Decoradores:**
   - Você pode aplicar vários decoradores a uma única função. A ordem na qual eles são aplicados importa.

   ```python
   @decorador1
   @decorador2
   def minha_funcao():
       # corpo da função
   ```

5. **Decoradores Incorporados:**
   - Python possui alguns decoradores incorporados úteis, como `@staticmethod`, `@classmethod` e `@property`, que são comumente usados em programação orientada a objetos.

6. **Documentação Oficial:**
   - Para obter informações mais detalhadas e exemplos, consulte a documentação oficial do Python sobre decoradores em [Python Decorators](https://docs.python.org/3/glossary.html#term-decorator).

Decoradores são uma ferramenta poderosa e versátil em Python, e eles são comumente usados em frameworks e bibliotecas para adicionar funcionalidades extra de uma maneira limpa e modular. Eles podem tornar o código mais legível, reutilizável e fácil de manter.

> [retornar](#anotações-módulo-2---programação-orientada-a-objetos) para o topo da página

### Criação de Classes em Python

Em programação orientada a objetos (POO), as classes são uma parte fundamental. Elas fornecem uma maneira de estruturar e organizar código, permitindo a criação de objetos que possuem características (atributos) e comportamentos (métodos). No contexto de Python, as classes são a base para a implementação de POO.

Aqui estão alguns conceitos e informações relevantes sobre classes em Python:

1. **Definição de Classe:**
   - Uma classe é uma estrutura para representar um conceito no código, abstraindo dados e operações relacionadas a esse conceito.

2. **Objetos:**
   - Uma vez que uma classe é definida, você pode criar instâncias dessa classe, que são chamadas de objetos. Os objetos são instâncias específicas da classe.

3. **Atributos:**
   - Atributos são variáveis que armazenam dados associados a uma classe ou objeto. Eles representam as características do objeto.

4. **Métodos:**
   - Métodos são funções definidas dentro da classe e operam nos atributos do objeto. Eles representam o comportamento do objeto.

5. **Encapsulamento:**
   - Em Python, o encapsulamento não é estritamente aplicado como em algumas linguagens, mas convenções são seguidas. Atributos e métodos podem ser públicos, protegidos ou privados.

6. **Herança:**
   - A herança permite que uma classe herde atributos e métodos de outra. Isso promove a reutilização de código e a criação de hierarquias de classes.

7. **Polimorfismo:**
   - O polimorfismo permite que objetos de diferentes classes sejam tratados de maneira uniforme. Isso é alcançado através da implementação de métodos com o mesmo nome em classes diferentes.

8. **Construtores e Destrutores:**
   - O método `__init__` é um construtor, utilizado para inicializar os atributos quando um objeto é criado. O método `__del__` é um destrutor, usado para realizar ações de limpeza antes que o objeto seja removido.

Exemplo de uma classe simples em Python:

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

# Criando um objeto da classe Pessoa
pessoa1 = Pessoa("Alice", 25)

# Chamando o método da classe
pessoa1.apresentar()
```

Para mais detalhes, consulte a [documentação oficial do Python sobre classes](https://docs.python.org/3/tutorial/classes.html).

> [retornar](#anotações-módulo-2---programação-orientada-a-objetos) para o topo da página

## Dicas Importantes

### Uso do `self`

Em Python, o `self` é uma convenção usada para representar a instância atual de uma classe em métodos. Ele é um parâmetro implícito que faz referência ao próprio objeto criado a partir da classe. Ao utilizar o `self` corretamente, você garante o acesso aos atributos e métodos da instância da classe. Aqui estão algumas informações relevantes sobre o uso do `self` no contexto de Programação Orientada a Objetos (POO) em Python:

1. **Definição de Métodos:**
   - Ao definir métodos dentro de uma classe, o primeiro parâmetro deve ser `self`.
   - O `self` representa a instância atual da classe e permite o acesso aos seus atributos e métodos.

   ```python
   class MinhaClasse:
       def meu_metodo(self):
           # Uso do self para acessar atributos da instância
           print(f"Acesso a atributos: {self.atributo}")
   ```

2. **Acesso a Atributos:**
   - Use o `self` para acessar atributos da instância dentro dos métodos.
   - O `self` permite distinguir entre variáveis de instância e variáveis locais no escopo do método.

   ```python
   class MinhaClasse:
       def __init__(self, atributo):
           self.atributo = atributo

       def meu_metodo(self):
           print(f"Acesso a atributo: {self.atributo}")
   ```

3. **Chamada de Métodos:**
   - Ao chamar métodos dentro da própria classe, use o `self`.
   - Isso é útil para reutilizar código e garantir que o método acesse corretamente os atributos da instância.

   ```python
   class MinhaClasse:
       def __init__(self, atributo):
           self.atributo = atributo

       def meu_metodo(self):
           print(f"Acesso a atributo: {self.atributo}")

       def outro_metodo(self):
           # Chamada de um método dentro da própria classe usando self
           self.meu_metodo()
   ```

4. **Referência a Outros Métodos e Atributos:**
   - Utilize o `self` para referenciar outros métodos e atributos da instância.
   - Isso facilita a leitura e compreensão do código.

   ```python
   class MinhaClasse:
       def __init__(self, atributo):
           self.atributo = atributo

       def meu_metodo(self):
           print(f"Acesso a atributo: {self.atributo}")

       def outro_metodo(self):
           # Referência a outro método usando self
           self.meu_metodo()
   ```

5. **Instância vs. Classe:**
   - `self` refere-se à instância da classe, enquanto o nome da classe (sem instância) é usado para acessar atributos ou métodos estáticos.

   ```python
   class MinhaClasse:
       atributo_estatico = "Atributo estático"

       def __init__(self, atributo):
           self.atributo = atributo

       def meu_metodo(self):
           print(f"Acesso a atributo: {self.atributo}")

   # Acesso a atributo estático sem instância
   print(MinhaClasse.atributo_estatico)
   ```

Ao usar o `self` de maneira consistente e apropriada, você torna seu código mais legível e fácil de manter. O `self` é uma parte essencial da POO em Python, proporcionando uma referência à instância atual da classe.

Para informações mais detalhadas, consulte a [documentação oficial do Python sobre classes](https://docs.python.org/3/tutorial/classes.html).

> [retornar](#anotações-módulo-2---programação-orientada-a-objetos) para o topo da página

### Uso da classe `NotImplementedError`

A classe `NotImplementedError` em Python é geralmente utilizada para sinalizar que um método em uma classe não foi implementado, deixando a responsabilidade para as subclasses fornecerem uma implementação específica. Isso é particularmente útil em programação orientada a objetos (POO) quando você está definindo uma interface ou uma classe base com métodos que devem ser implementados pelas subclasses.

Aqui está um exemplo básico de como você pode usar a `NotImplementedError`:

```python
class Animal:
    def make_sound(self):
        raise NotImplementedError("Subclasses devem implementar o método make_sound")


class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Snake(Animal):
    pass  # Aqui a NotImplementedError será levantada se tentarmos criar uma instância de Snake
```

Neste exemplo, a classe `Animal` define um método `make_sound` que é marcado com `NotImplementedError`. As subclasses, como `Dog` e `Cat`, fornecem implementações específicas desse método. No entanto, se tentarmos criar uma instância da classe `Snake` sem fornecer uma implementação para `make_sound`, a `NotImplementedError` será levantada.

Ao utilizar a `NotImplementedError`, você está deixando claro para outros programadores (ou para você mesmo no futuro) que essa parte do código precisa ser implementada em subclasses antes que a funcionalidade completa da classe base possa ser utilizada.

Lembre-se de que a `NotImplementedError` não é estritamente necessária; você também pode simplesmente não fornecer uma implementação para o método na classe base. No entanto, usar `NotImplementedError` adiciona uma camada adicional de clareza e documentação no código.

Por fim, aqui está o link para a documentação oficial do Python, onde você pode encontrar mais detalhes sobre a classe `NotImplementedError` e outros aspectos da linguagem: [Documentação oficial do Python - NotImplementedError](https://docs.python.org/3/library/exceptions.html#NotImplementedError)

> [retornar](#anotações-módulo-2---programação-orientada-a-objetos) para o topo da página
>
> [voltar](../../README.md) para página anterior
