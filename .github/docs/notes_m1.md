# Anotações Módulo 1 - Introdução ao Python

> [voltar](../../README.md) para página anterior

## Sumário

- [Anotações Módulo 1 - Introdução ao Python](#anotações-módulo-1---introdução-ao-python)
  - [Sumário](#sumário)
  - [Conteúdo](#conteúdo)
    - [O que é Python?](#o-que-é-python)
    - [O que é Sintaxe?](#o-que-é-sintaxe)
    - [Variáveis](#variáveis)
    - [Números](#números)
    - [Textos (String)](#textos-string)
      - [Principais Métodos para Manipulação de String](#principais-métodos-para-manipulação-de-string)
    - [Booleanos](#booleanos)
    - [Listas](#listas)
      - [Principais Métodos para Manipulação de Listas](#principais-métodos-para-manipulação-de-listas)
    - [Tuplas](#tuplas)
    - [Dicionários](#dicionários)
      - [Principais Métodos para Manipulação de Dicionários](#principais-métodos-para-manipulação-de-dicionários)
    - [Condicionais](#condicionais)
    - [Loop `for`](#loop-for)
    - [Loop `while`](#loop-while)
    - [Funções](#funções)
    - [Exceções](#exceções)
    - [Módulos](#módulos)

## Conteúdo

### O que é Python?

Python é uma linguagem de programação de alto nível, interpretada, orientada a objetos e de propósito geral. Ela foi criada por Guido van Rossum e teve sua primeira versão lançada em 1991. Python é conhecida por sua sintaxe clara e legível, o que a torna uma escolha popular entre programadores iniciantes e experientes.

Aqui estão algumas informações relevantes sobre Python para o dia a dia do programador:

1. **Sintaxe Simples:** A sintaxe de Python é projetada para ser simples e fácil de ler. Isso facilita a escrita e a manutenção do código.

2. **Ampla Comunidade:** Python possui uma comunidade ativa e vasta, o que significa que há uma abundância de recursos online, fóruns e bibliotecas disponíveis para ajudar os programadores.

3. **Versatilidade:** Python é uma linguagem versátil que pode ser usada em uma variedade de domínios, incluindo desenvolvimento web, automação, análise de dados, inteligência artificial, aprendizado de máquina, entre outros.

4. **Bibliotecas Poderosas:** Python tem uma rica coleção de bibliotecas que simplificam tarefas comuns. Exemplos incluem NumPy e Pandas para manipulação de dados, Matplotlib e Seaborn para visualização, e Flask e Django para desenvolvimento web.

5. **Interpretação Dinâmica:** Python é uma linguagem interpretada, o que significa que você pode testar e executar partes do código rapidamente sem a necessidade de compilação.

6. **Multiplataforma:** O código Python é executável em várias plataformas, como Windows, Linux e macOS, sem a necessidade de modificações significativas.

7. **Desenvolvimento Rápido:** Devido à sua sintaxe simples e ao vasto conjunto de bibliotecas, o desenvolvimento em Python é geralmente mais rápido do que em outras linguagens.

8. **Aprendizado Fácil:** Python é frequentemente recomendado como uma primeira linguagem para aprender programação devido à sua abordagem amigável.

9. **Compreensão de Código Aberto:** Python é uma linguagem de código aberto, o que significa que o código-fonte está disponível para qualquer pessoa. Isso incentiva a colaboração e contribuição da comunidade.

10. **Automação e Scripting:** Python é amplamente utilizado para automação de tarefas e scripting devido à sua simplicidade e eficácia.

Esses são apenas alguns aspectos do Python que fazem dela uma escolha popular entre os programadores. Sua flexibilidade e poder tornam-na adequada para uma ampla gama de projetos e aplicações.

> [retornar](#anotações-módulo-1---introdução-ao-python) para o topo da página

### O que é Sintaxe?

Em programação, sintaxe refere-se à estrutura e às regras que governam a combinação de elementos individuais em uma linguagem de programação específica. No caso do Python, a sintaxe é a forma como você escreve seu código para que seja compreendido e executado corretamente pelo interpretador Python.

Aqui estão alguns aspectos fundamentais da sintaxe em Python:

1. **Indentação:** Python utiliza a indentação para delimitar blocos de código. Em vez de chaves ou palavras-chave como "begin" e "end", como em algumas linguagens, o Python usa espaços ou tabulações no início de linhas para indicar a estrutura do código. Isso ajuda a tornar o código mais legível, mas também exige consistência na indentação.

   Exemplo:

   ```python
   if x > 0:
       print("X é positivo")
   else:
       print("X é não positivo")
   ```

2. **Variáveis:** Em Python, você pode criar variáveis atribuindo valores a nomes. O tipo da variável é inferido dinamicamente. A declaração de uma variável é simples e direta:

   ```python
   nome = "ChatGPT"
   idade = 3
   pi = 3.14
   ```

3. **Comentários:** Comentários são utilizados para adicionar explicações ao código e são precedidos pelo símbolo `#`. Tudo após o `#` na mesma linha é tratado como um comentário.

   ```python
   # Isso é um comentário
   x = 10  # Isso também é um comentário
   ```

4. **Estruturas de Controle de Fluxo:** Python inclui estruturas de controle de fluxo comuns, como `if`, `else`, e `elif` para tomada de decisões, e `for` e `while` para loops.

   ```python
   if condição:
       # bloco de código se a condição for verdadeira
   else:
       # bloco de código se a condição for falsa
   ```

   ```python
   for item in lista:
       # bloco de código a ser repetido para cada item na lista
   ```

5. **Funções:** Em Python, funções são definidas com a palavra-chave `def` seguida pelo nome da função e parâmetros.

   ```python
   def saudacao(nome):
       return "Olá, " + nome + "!"
   ```

6. **Listas, Tuplas e Dicionários:** Python oferece estruturas de dados como listas, tuplas e dicionários para armazenar e organizar dados de diferentes maneiras.

   ```python
   lista = [1, 2, 3]
   tupla = (1, 2, 3)
   dicionario = {'chave': 'valor', 'outra_chave': 'outro_valor'}
   ```

7. **Importação de Módulos:** Python possui uma biblioteca rica e permite a importação de módulos para estender a funcionalidade do seu programa.

   ```python
   import math
   print(math.sqrt(25))
   ```

Esses são apenas alguns aspectos da sintaxe em Python. Familiarizar-se com esses conceitos básicos é crucial para escrever código funcional e eficiente nesta linguagem de programação.

> [retornar](#anotações-módulo-1---introdução-ao-python) para o topo da página

### Variáveis

Variáveis em Python são utilizadas para armazenar dados e informações em um programa. Aqui estão alguns aspectos importantes sobre como as variáveis funcionam em Python:

1. **Declaração de Variáveis:**
   - Em Python, você não precisa declarar explicitamente o tipo de uma variável. O tipo é inferido dinamicamente durante a execução.
   - Você pode declarar uma variável atribuindo um valor a um nome.

     ```python
     idade = 25
     nome = "Alice"
     salario = 1500.50
     ```

2. **Tipos de Dados:**
   - Python suporta vários tipos de dados, incluindo inteiros, floats, strings, listas, tuplas, conjuntos, dicionários, booleanos, entre outros.
   - A função `type()` pode ser usada para verificar o tipo de uma variável.

     ```python
     x = 5
     y = 3.14
     nome = "Python"
     
     print(type(x))    # <class 'int'>
     print(type(y))    # <class 'float'>
     print(type(nome)) # <class 'str'>
     ```

3. **Convenções de Nomenclatura:**
   - É comum seguir convenções ao nomear variáveis em Python. Geralmente, utiliza-se letras minúsculas e underscores para separar palavras em nomes de variáveis (snake_case).

     ```python
     idade_do_usuario = 30
     ```

   - Evite usar palavras-chave do Python como nomes de variáveis.

4. **Reatribuição de Variáveis:**
   - O valor de uma variável pode ser alterado ao longo do tempo, sendo reatribuído a um novo valor.

     ```python
     x = 5
     x = x + 1  # Agora, x é 6
     ```

5. **Escopo de Variáveis:**
   - Variáveis podem ser locais (definidas dentro de uma função) ou globais (definidas fora de qualquer função).
   - A regra LEGB (Local, Enclosing, Global, Built-in) determina a ordem de busca de uma variável.

     ```python
     global_var = 10

     def minha_funcao():
         local_var = 5
         print(global_var)  # Pode acessar variável global
         print(local_var)   # Pode acessar variável local

     minha_funcao()
     ```

6. **Operações com Variáveis:**
   - Variáveis podem participar de operações matemáticas e lógicas.

     ```python
     a = 5
     b = 3
     soma = a + b
     resultado = a * b
     ```

7. **Desempacotamento de Variáveis:**
   - Python permite desempacotar valores diretamente em variáveis.

     ```python
     x, y = 10, 20
     ```

8. **Referência a Objetos:**
   - Em Python, as variáveis são referências a objetos na memória. Uma variável não contém diretamente o valor, mas aponta para o local na memória onde o valor é armazenado.

     ```python
     a = [1, 2, 3]
     b = a
     ```

   - Nesse exemplo, `a` e `b` referenciam a mesma lista na memória.

Esses são alguns aspectos essenciais sobre como as variáveis funcionam em Python. Entender esses conceitos é fundamental para escrever código eficaz e compreender o comportamento do programa.

> [retornar](#anotações-módulo-1---introdução-ao-python) para o topo da página

### Números

Lidar com números em Python é uma parte essencial da programação, e a linguagem oferece diversas funcionalidades para manipulação eficiente de dados numéricos. Aqui estão algumas informações relevantes para o dia a dia do programador:

**1. Tipos de Números:**

- **Inteiros (int):** Representam números inteiros, positivos ou negativos, sem casas decimais.
- **Ponto Flutuante (float):** Representam números com casas decimais.

```python
# Exemplos
inteiro = 10
ponto_flutuante = 3.14
```

**2. Operações Básicas:**

- Python suporta as operações matemáticas básicas: adição (`+`), subtração (`-`), multiplicação (`*`), divisão (`/`), exponenciação (`**`), e divisão inteira (`//`).

```python
# Exemplos
soma = 5 + 3
subtracao = 7 - 2
multiplicacao = 4 * 6
divisao = 10 / 2
exponenciacao = 2 ** 3
divisao_inteira = 15 // 4
```

**3. Funções Matemáticas:**

- O módulo `math` fornece funções matemáticas mais avançadas, como seno, cosseno, raiz quadrada, etc.

```python
import math

# Exemplos
raiz_quadrada = math.sqrt(25)
seno_angulo = math.sin(math.radians(30))  # Convertendo graus para radianos
```

**4. Arredondamento e Formatação:**

- A função `round()` é usada para arredondar números. O método `format()` pode ser usado para formatar a saída.

```python
# Exemplos
numero_arredondado = round(3.14159, 2)  # Arredondando para 2 casas decimais
mensagem_formatada = "O resultado é {:.2f}".format(7.456)
```

**5. Conversão entre Tipos:**

- É possível converter entre inteiros e ponto flutuante usando `int()` e `float()`.

```python
# Exemplos
numero_int = int(3.14)
numero_float = float(5)
```

**6. Operações com Números Complexos:**

- Python suporta números complexos usando a unidade imaginária `j`.

```python
# Exemplo
numero_complexo = 2 + 3j
```

**7. Bibliotecas Numéricas:**

- Para tarefas mais avançadas, como manipulação de arrays numéricos, álgebra linear, e processamento científico, bibliotecas como NumPy e SciPy são amplamente utilizadas.

```python
import numpy as np

# Exemplo
array = np.array([1, 2, 3])
soma_array = np.sum(array)
```

**8. Tratamento de Erros:**

- Ao lidar com operações que podem resultar em erros (por exemplo, divisão por zero), é importante incluir tratamentos apropriados usando estruturas de controle como `try` e `except`.

```python
# Exemplo
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Erro: Divisão por zero.")
```

Estas são apenas algumas informações básicas sobre como lidar com números em Python. Dependendo do contexto do seu projeto, pode ser necessário explorar bibliotecas adicionais ou técnicas mais avançadas.

> [retornar](#anotações-módulo-1---introdução-ao-python) para o topo da página

### Textos (String)

Lidar com textos em Python é uma parte essencial do desenvolvimento de software. Existem várias operações que você pode realizar em strings (cadeias de caracteres) para manipular, analisar e exibir informações. Abaixo estão algumas informações relevantes e dicas úteis para lidar com textos em Python:

1. **Strings em Python:**
   - Strings são representadas por sequências de caracteres entre aspas simples (' '), duplas (" "), ou triplas (''' ' ou """ ").
   - Exemplo: `texto = "Olá, mundo!"`

2. **Operações básicas:**
   - Concatenação: `concatenado = string1 + string2`
   - Repetição: `repetido = string * 3`
   - Indexação: Acesso a caracteres individuais por índice, como `primeiro_caracter = string[0]`

3. **Métodos de String:**
   - Python possui muitos métodos embutidos para manipular strings, como `upper()`, `lower()`, `replace()`, `split()`, `strip()`, etc. Exemplo:

     ```python
     mensagem = "olá, mundo"
     mensagem_upper = mensagem.upper()
     ```

4. **Formatação de Strings:**
   - Você pode formatar strings de várias maneiras, incluindo a formatação antiga com `%`, a formatação com `str.format()`, e a formatação de f-strings (disponível a partir do Python 3.6). Exemplo:

     ```python
     nome = "Alice"
     idade = 25
     frase = "Olá, meu nome é {} e eu tenho {} anos.".format(nome, idade)
     ```

5. **Expressões Regulares (RegEx):**
   - O módulo `re` oferece suporte a expressões regulares, que são poderosas para encontrar padrões em strings. Exemplo:

     ```python
     import re
     padrao = re.compile(r'\d+')
     resultado = padrao.findall("Há 42 maçãs na cesta.")
     ```

6. **Manipulação de Texto Multilinha:**
   - Use aspas triplas para criar strings multilinha:

     ```python
     texto_multilinha = """Linha 1
                         Linha 2
                         Linha 3"""
     ```

7. **Leitura e Escrita de Arquivos de Texto:**
   - Para ler e escrever texto em arquivos, use as funções `open()` e métodos como `read()`, `write()`, e `close()`. Exemplo:

     ```python
     with open('arquivo.txt', 'r') as arquivo:
         conteudo = arquivo.read()
     ```

8. **Tratamento de Codificação e Decodificação:**
   - Ao lidar com diferentes codificações, use os parâmetros `encoding` e `errors` nas operações de leitura e escrita de arquivos. Exemplo:

     ```python
     with open('arquivo.txt', 'r', encoding='utf-8', errors='ignore') as arquivo:
         conteudo = arquivo.read()
     ```

9. **Manipulação Eficiente de Strings:**
   - Para manipulações complexas, considere o uso de módulos como `str.join()`, `str.splitlines()`, e `str.startswith()` para tornar o código mais eficiente e legível.

10. **Documentação e Recursos Online:**
    - A documentação oficial do Python (<https://docs.python.org/3/>) é uma excelente fonte de informações sobre manipulação de strings. Além disso, há muitos recursos online, como tutoriais e fóruns, que podem ajudar a resolver problemas específicos.

Lidar com textos em Python é uma habilidade fundamental para a programação eficaz. Compreender esses conceitos e técnicas permitirá que você crie programas mais poderosos e flexíveis.

> [retornar](#anotações-módulo-1---introdução-ao-python) para o topo da página

#### Principais Métodos para Manipulação de String

Existem vários métodos disponíveis para manipulação de strings em Python. Aqui estão alguns dos principais métodos que você pode usar:

1. **Métodos de Transformação de Caixa:**
   - `str.upper()`: Converte todos os caracteres para maiúsculas.
   - `str.lower()`: Converte todos os caracteres para minúsculas.
   - `str.capitalize()`: Converte o primeiro caractere para maiúscula.

   Exemplo:

   ```python
   texto = "olá, mundo"
   maiusculo = texto.upper()
   minusculo = texto.lower()
   capitalizado = texto.capitalize()
   ```

2. **Métodos de Busca e Substituição:**
   - `str.find(substring)`: Retorna o índice da primeira ocorrência da substring (ou -1 se não encontrar).
   - `str.replace(old, new)`: Substitui todas as ocorrências da substring antiga pela nova.

   Exemplo:

   ```python
   frase = "Python é uma linguagem poderosa"
   indice = frase.find("uma")
   substituido = frase.replace("poderosa", "versátil")
   ```

3. **Métodos de Verificação de Conteúdo:**
   - `str.startswith(prefixo)`: Verifica se a string começa com o prefixo especificado.
   - `str.endswith(sufixo)`: Verifica se a string termina com o sufixo especificado.
   - `str.contains(substring)`: Verifica se a substring está presente na string (Python 3.10+).

   Exemplo:

   ```python
   texto = "Python é uma linguagem poderosa"
   comeca_com_python = texto.startswith("Python")
   termina_com_osa = texto.endswith("osa")
   contem_linguagem = "linguagem" in texto  # Alternativa para Python 3.10+
   ```

4. **Métodos de Remoção de Espaços em Branco:**
   - `str.strip()`: Remove espaços em branco do início e do final da string.
   - `str.lstrip()`: Remove espaços em branco do início da string.
   - `str.rstrip()`: Remove espaços em branco do final da string.

   Exemplo:

   ```python
   texto = "   Espaços em branco   "
   sem_espacos = texto.strip()
   ```

5. **Métodos de Separação e Junção:**
   - `str.split(separador)`: Divide a string em uma lista de substrings com base no separador especificado.
   - `str.join(iterable)`: Junta os elementos de um iterable (por exemplo, uma lista) em uma string, usando a string como separador.

   Exemplo:

   ```python
   frase = "Python é uma linguagem poderosa"
   palavras = frase.split(" ")
   juntado = "-".join(palavras)
   ```

Esses são apenas alguns dos muitos métodos disponíveis para manipulação de strings em Python. Consulte a documentação oficial do Python para obter uma lista completa de métodos e suas descrições: [Documentação de Strings Python](https://docs.python.org/3/library/stdtypes.html#string-methods).

> [retornar](#anotações-módulo-1---introdução-ao-python) para o topo da página

### Booleanos

Em Python, os booleanos são um tipo de dado que representa valores lógicos. Eles têm apenas dois valores possíveis: `True` (Verdadeiro) e `False` (Falso). Os booleanos são fundamentais para expressar condições e lógica em programas Python. Aqui estão algumas informações relevantes para o dia a dia do programador:

1. **Operadores Lógicos:**
   - `and`: Retorna True se ambas as condições forem verdadeiras.
   - `or`: Retorna True se pelo menos uma das condições for verdadeira.
   - `not`: Inverte o valor booleano, ou seja, se a condição é True, `not` a tornará False, e vice-versa.

   Exemplo:

   ```python
   x = True
   y = False

   print(x and y)  # False
   print(x or y)   # True
   print(not x)     # False
   ```

2. **Comparadores:**
   - `==`: Igual a
   - `!=`: Diferente de
   - `<`, `>`, `<=`, `>=`: Menor que, maior que, menor ou igual a, maior ou igual a, respectivamente.

   Exemplo:

   ```python
   a = 5
   b = 10

   print(a == b)  # False
   print(a != b)  # True
   print(a < b)   # True
   ```

3. **Expressões Condicionais (if, elif, else):**
   Os booleanos são frequentemente usados em estruturas de controle de fluxo para tomar decisões no código.

   Exemplo:

   ```python
   idade = 18

   if idade >= 18:
       print("Você é maior de idade.")
   else:
       print("Você é menor de idade.")
   ```

4. **Funções e Métodos que Retornam Booleanos:**
   Muitas funções e métodos retornam valores booleanos, indicando se uma condição é atendida ou não.

   Exemplo:

   ```python
   lista = [1, 2, 3, 4, 5]

   print(3 in lista)  # True
   print(6 in lista)  # False
   ```

5. **Uso em Estruturas de Repetição:**
   Os booleanos são frequentemente usados para controlar loops (como while e for).

   Exemplo:

   ```python
   contador = 0

   while contador < 5:
       print(contador)
       contador += 1
   ```

Documentação oficial: [Python Boolean Operations](https://docs.python.org/3/library/stdtypes.html#boolean-operations)

> [retornar](#anotações-módulo-1---introdução-ao-python) para o topo da página

### Listas

Uma lista é uma estrutura de dados versátil e fundamental que permite armazenar uma coleção ordenada de elementos. As listas são mutáveis, o que significa que você pode modificar, adicionar e remover elementos após a criação da lista. Aqui estão algumas informações relevantes sobre listas em Python:

1. **Sintaxe de Criação:**
   Para criar uma lista em Python, você utiliza colchetes `[]` e separa os elementos por vírgulas. Exemplo:

   ```python
   minha_lista = [1, 2, 3, "texto", True]
   ```

2. **Acesso a Elementos:**
   Os elementos em uma lista podem ser acessados pelo índice (posição) na lista. Lembre-se de que os índices em Python começam do zero.

   ```python
   primeiro_elemento = minha_lista[0]
   ```

3. **Manipulação de Listas:**
   - Adição de elementos: Utilize o método `append()` para adicionar um elemento ao final da lista.

     ```python
     minha_lista.append(4)
     ```

   - Remoção de elementos: Use o comando `del` ou o método `remove()` para excluir elementos.

     ```python
     del minha_lista[2]  # Remove o terceiro elemento
     minha_lista.remove("texto")  # Remove o elemento com o valor "texto"
     ```

4. **Operações com Listas:**
   - Concatenação: Use o operador `+` para juntar duas listas.

     ```python
     nova_lista = minha_lista + [5, 6, 7]
     ```

   - Repetição: Utilize o operador `*` para repetir uma lista.

     ```python
     lista_repetida = minha_lista * 3
     ```

5. **Funções e Métodos Úteis:**
   - `len()`: Retorna o número de elementos em uma lista.

     ```python
     tamanho = len(minha_lista)
     ```

   - `index()`: Retorna o índice do primeiro elemento com o valor especificado.

     ```python
     indice = minha_lista.index(3)
     ```

6. **Compreensão de Lista:**
   Python suporta compreensões de lista, uma maneira concisa de criar listas usando uma única linha de código.

   ```python
   quadrados = [x**2 for x in range(1, 6)]
   ```

7. **Slice de Lista:**
   Você pode acessar partes de uma lista usando a notação de slice.

   ```python
   parte_da_lista = minha_lista[1:4]  # Retorna os elementos do índice 1 ao 3
   ```

8. **Método `sort()`:**
   O método `sort()` ordena a lista in-place. Você também pode usar a função `sorted()` para obter uma nova lista ordenada.

   ```python
   minha_lista.sort()
   ```

Para obter informações mais detalhadas e abrangentes, consulte a documentação oficial do Python sobre listas: [Documentação de Listas em Python](https://docs.python.org/3/tutorial/introduction.html#lists).

> [retornar](#anotações-módulo-1---introdução-ao-python) para o topo da página

#### Principais Métodos para Manipulação de Listas

Existem diversos métodos disponíveis para manipulação de listas em Python. Aqui estão alguns dos principais métodos que são frequentemente utilizados:

1. **`append(elemento)`:**
   Adiciona um elemento ao final da lista.

   ```python
   minha_lista = [1, 2, 3]
   minha_lista.append(4)  # Resultado: [1, 2, 3, 4]
   ```

2. **`extend(iterável)`:**
   Adiciona os elementos de um iterável (outra lista, por exemplo) ao final da lista.

   ```python
   minha_lista = [1, 2, 3]
   minha_lista.extend([4, 5, 6])  # Resultado: [1, 2, 3, 4, 5, 6]
   ```

3. **`insert(posição, elemento)`:**
   Insere um elemento em uma posição específica da lista.

   ```python
   minha_lista = [1, 2, 3]
   minha_lista.insert(1, 4)  # Resultado: [1, 4, 2, 3]
   ```

4. **`remove(elemento)`:**
   Remove o primeiro elemento na lista que tem o valor especificado.

   ```python
   minha_lista = [1, 2, 3, 2]
   minha_lista.remove(2)  # Resultado: [1, 3, 2]
   ```

5. **`pop([índice])`:**
   Remove e retorna o elemento no índice especificado. Se nenhum índice for fornecido, remove e retorna o último elemento.

   ```python
   minha_lista = [1, 2, 3]
   elemento_removido = minha_lista.pop(1)  # Resultado: elemento_removido=2, minha_lista=[1, 3]
   ```

6. **`index(elemento[, início[, fim]])`:**
   Retorna o índice do primeiro elemento com o valor especificado. Pode ser fornecido um intervalo opcional de busca.

   ```python
   minha_lista = [1, 2, 3, 2]
   índice = minha_lista.index(2)  # Resultado: índice=1
   ```

7. **`count(elemento)`:**
   Retorna o número de ocorrências do elemento na lista.

   ```python
   minha_lista = [1, 2, 3, 2]
   contagem = minha_lista.count(2)  # Resultado: contagem=2
   ```

8. **`sort(key=None, reverse=False)`:**
   Ordena a lista in-place. Os parâmetros opcionais `key` e `reverse` controlam a ordenação.

   ```python
   minha_lista = [3, 1, 4, 1, 5, 9, 2]
   minha_lista.sort()  # Resultado: minha_lista=[1, 1, 2, 3, 4, 5, 9]
   ```

9. **`reverse()`:**
   Inverte a ordem dos elementos da lista in-place.

   ```python
   minha_lista = [1, 2, 3]
   minha_lista.reverse()  # Resultado: minha_lista=[3, 2, 1]
   ```

10. **`clear()`:**
    Remove todos os elementos da lista, deixando-a vazia.

    ```python
    minha_lista = [1, 2, 3]
    minha_lista.clear()  # Resultado: minha_lista=[]
    ```

A documentação oficial do Python oferece uma visão mais completa e detalhada desses métodos: [Métodos de Listas em Python](https://docs.python.org/3/tutorial/introduction.html#lists).

> [retornar](#anotações-módulo-1---introdução-ao-python) para o topo da página

### Tuplas

Tupla é uma estrutura de dados semelhante a uma lista, mas com uma diferença fundamental: ela é imutável, o que significa que uma vez que uma tupla é criada, seus elementos não podem ser alterados, adicionados ou removidos. As tuplas são representadas por parênteses e podem conter elementos de diferentes tipos, incluindo números, strings, listas e até mesmo outras tuplas.

Aqui estão algumas características importantes das tuplas em Python e como elas podem ser úteis no dia a dia do programador:

1. **Imutabilidade:** A imutabilidade das tuplas torna-as úteis quando você quer garantir que os dados não sejam alterados acidental ou intencionalmente. Isso pode ser crucial em situações onde a integridade dos dados é essencial.

2. **Performance:** Tuplas são geralmente mais eficientes em termos de desempenho do que listas, pois a imutabilidade permite otimizações internas no interpretador Python.

3. **Atribuição Múltipla:** As tuplas podem ser usadas para realizar atribuição múltipla, o que significa que você pode atribuir valores a várias variáveis em uma única linha.

    ```python
    # Atribuição múltipla usando tuplas
    x, y, z = 1, 2, 3
    ```

4. **Retorno Múltiplo de Funções:** Uma função em Python pode retornar uma tupla, permitindo que múltiplos valores sejam retornados em uma única chamada de função.

    ```python
    def retorna_valores():
        return 1, 2, 3

    # Atribuição múltipla dos valores retornados
    a, b, c = retorna_valores()
    ```

5. **Argumentos de Funções:** As tuplas podem ser usadas para passar um número variável de argumentos para uma função.

    ```python
    def soma(*numeros):
        resultado = 0
        for numero in numeros:
            resultado += numero
        return resultado

    # Chamada da função com argumentos variáveis
    total = soma(1, 2, 3, 4)
    ```

6. **Indexação e Fatias:** Assim como listas, as tuplas suportam indexação e fatias, permitindo acesso fácil aos seus elementos.

    ```python
    tupla = (1, 2, 3, 4, 5)

    # Acessando elementos
    primeiro_elemento = tupla[0]

    # Fatiando a tupla
    sub_tupla = tupla[1:4]
    ```

7. **Uso em Dicionários:** Tuplas podem ser usadas como chaves em dicionários, enquanto listas não podem devido à sua imutabilidade.

    ```python
    dicionario = {(1, 2): 'valor'}
    ```

Em resumo, as tuplas em Python são estruturas de dados versáteis e poderosas, especialmente quando imutabilidade e atribuição múltipla são desejadas. Elas são amplamente utilizadas em situações em que a ordem e a imutabilidade dos elementos são cruciais.

Para obter informações mais detalhadas sobre tuplas em Python, consulte a [documentação oficial de Tuplas em Python](https://docs.python.org/3/tutorial/datastructures.html#tuples).

> [retornar](#anotações-módulo-1---introdução-ao-python) para o topo da página

### Dicionários

Dicionário é uma estrutura de dados que permite armazenar e organizar informações de maneira eficiente. Ele é uma coleção não ordenada de pares chave-valor, onde cada chave deve ser única. Essas chaves são usadas para acessar os valores associados a elas. Os dicionários são mutáveis, o que significa que você pode modificar, adicionar ou remover itens depois de criá-los.

Aqui estão alguns conceitos importantes sobre dicionários em Python:

1. **Sintaxe:**
   Para criar um dicionário, você utiliza a seguinte sintaxe:

   ```python
   meu_dicionario = {'chave1': valor1, 'chave2': valor2, ...}
   ```

2. **Acesso a Elementos:**
   Você pode acessar os valores de um dicionário usando a chave correspondente:

   ```python
   print(meu_dicionario['chave1'])
   ```

3. **Adição, Atualização e Remoção de Elementos:**
   - Adicionar um novo par chave-valor: `meu_dicionario['nova_chave'] = novo_valor`
   - Atualizar um valor existente: `meu_dicionario['chave1'] = novo_valor`
   - Remover um par chave-valor: `del meu_dicionario['chave1']`

4. **Verificação de Existência de Chave:**
   Você pode verificar se uma chave existe no dicionário usando o operador `in`:

   ```python
   if 'chave1' in meu_dicionario:
       print('Chave encontrada!')
   ```

5. **Funções Úteis:**
   - `keys()`: Retorna uma lista com todas as chaves do dicionário.
   - `values()`: Retorna uma lista com todos os valores do dicionário.
   - `items()`: Retorna uma lista de tuplas, cada uma contendo um par chave-valor.

6. **Iteração:**
   Você pode iterar sobre chaves, valores ou itens (pares chave-valor) em um dicionário usando loops.

   ```python
   for chave in meu_dicionario:
       print(chave, meu_dicionario[chave])
   ```

7. **Compreensão de Dicionário:**
   Assim como listas, você pode usar compreensão de dicionário para criar dicionários de forma concisa.

   ```python
   novo_dicionario = {chave: valor for chave, valor in lista_de_pares}
   ```

Dicionários são extremamente úteis para armazenar dados de forma estruturada e acessá-los de maneira eficiente. Eles são amplamente utilizados em Python para resolver uma variedade de problemas. Para informações mais detalhadas, você pode consultar a [documentação oficial de dicionários em Python](https://docs.python.org/3/tutorial/datastructures.html#dictionaries).

> [retornar](#anotações-módulo-1---introdução-ao-python) para o topo da página

#### Principais Métodos para Manipulação de Dicionários

A manipulação de dicionários em Python é facilitada por vários métodos incorporados que permitem realizar diversas operações, como adicionar elementos, remover chaves, obter valores, verificar a existência de chaves, etc. Abaixo estão alguns dos principais métodos para manipulação de dicionários:

1. **`clear()`:**
   - Remove todos os itens do dicionário.

   ```python
   meu_dicionario = {'chave1': 'valor1', 'chave2': 'valor2'}
   meu_dicionario.clear()
   print(meu_dicionario)  # Saída: {}
   ```

2. **`copy()`:**
   - Retorna uma cópia superficial do dicionário.

   ```python
   meu_dicionario = {'chave1': 'valor1', 'chave2': 'valor2'}
   copia_dicionario = meu_dicionario.copy()
   ```

3. **`get(chave, [padrao])`:**
   - Retorna o valor associado à chave, ou um valor padrão se a chave não existir.

   ```python
   meu_dicionario = {'chave1': 'valor1', 'chave2': 'valor2'}
   valor = meu_dicionario.get('chave3', 'N/A')
   print(valor)  # Saída: 'N/A'
   ```

4. **`items()`:**
   - Retorna uma lista de tuplas contendo todos os pares chave-valor do dicionário.

   ```python
   meu_dicionario = {'chave1': 'valor1', 'chave2': 'valor2'}
   lista_de_items = meu_dicionario.items()
   ```

5. **`keys()`:**
   - Retorna uma lista com todas as chaves do dicionário.

   ```python
   meu_dicionario = {'chave1': 'valor1', 'chave2': 'valor2'}
   lista_de_chaves = meu_dicionario.keys()
   ```

6. **`values()`:**
   - Retorna uma lista com todos os valores do dicionário.

   ```python
   meu_dicionario = {'chave1': 'valor1', 'chave2': 'valor2'}
   lista_de_valores = meu_dicionario.values()
   ```

7. **`pop(chave, [padrao])`:**
   - Remove a chave especificada e retorna o valor associado a ela. Se a chave não existir, retorna o valor padrão (ou levanta uma exceção se nenhum padrão for fornecido).

   ```python
   meu_dicionario = {'chave1': 'valor1', 'chave2': 'valor2'}
   valor = meu_dicionario.pop('chave1')
   print(valor)  # Saída: 'valor1'
   ```

8. **`popitem()`:**
   - Remove e retorna um par chave-valor arbitrário do dicionário.

   ```python
   meu_dicionario = {'chave1': 'valor1', 'chave2': 'valor2'}
   par = meu_dicionario.popitem()
   print(par)  # Saída: ('chave2', 'valor2')
   ```

9. **`setdefault(chave, [padrao])`:**
   - Retorna o valor associado à chave se a chave existir. Se não existir, insere a chave com o valor padrão (ou `None` se nenhum padrão for fornecido) e retorna o valor padrão.

   ```python
   meu_dicionario = {'chave1': 'valor1', 'chave2': 'valor2'}
   valor = meu_dicionario.setdefault('chave3', 'N/A')
   print(valor)  # Saída: 'N/A'
   ```

10. **`update(dicionario)`:**

- Atualiza o dicionário com pares chave-valor de outro dicionário ou de uma sequência de pares chave-valor.

   ```python
   meu_dicionario = {'chave1': 'valor1', 'chave2': 'valor2'}
   outro_dicionario = {'chave3': 'valor3', 'chave4': 'valor4'}
   meu_dicionario.update(outro_dicionario)
   ```

Existem outros métodos menos comuns e algumas variações, então recomendo sempre consultar a [documentação oficial de dicionários em Python](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) para obter informações detalhadas.

> [retornar](#anotações-módulo-1---introdução-ao-python) para o topo da página

### Condicionais

Condicionais são estruturas de controle de fluxo que permitem que um programa tome decisões com base em condições específicas. As condicionais mais comuns em Python são expressas através das palavras-chave `if`, `elif` (abreviação de "else if") e `else`. Elas são fundamentais para o desenvolvimento de lógica condicional em programas, permitindo que trechos de código sejam executados ou ignorados dependendo das condições impostas.

A estrutura básica de uma condicional em Python é a seguinte:

```python
if condição:
    # código a ser executado se a condição for verdadeira
elif outra_condição:
    # código a ser executado se a condição anterior for falsa e esta for verdadeira
else:
    # código a ser executado se nenhuma das condições anteriores for verdadeira
```

A condição é uma expressão que avalia para `True` ou `False`. Se a condição associada ao `if` for verdadeira, o bloco de código dentro desse bloco é executado. Se a condição for falsa, o interpretador Python verifica a próxima condição no `elif`, e assim por diante. Se nenhuma das condições for verdadeira, o bloco dentro do `else` (se existir) é executado.

Exemplo:

```python
idade = 20

if idade < 18:
    print("Menor de idade")
elif idade >= 18 and idade < 65:
    print("Adulto")
else:
    print("Idoso")
```

Neste exemplo, o programa imprime a mensagem apropriada com base na idade da pessoa.

Para o dia a dia do programador, condicionais são ferramentas essenciais para lidar com casos específicos, tratar diferentes situações e garantir que o código seja executado de maneira apropriada dependendo das circunstâncias.

A documentação oficial do Python pode ser encontrada em: [Documentação Oficial do Python - Estruturas de Controle de Fluxo](https://docs.python.org/3/tutorial/controlflow.html)

> [retornar](#anotações-módulo-1---introdução-ao-python) para o topo da página

### Loop `for`

Em Python, o loop `for` é uma estrutura de controle que permite iterar sobre uma sequência de elementos, como uma lista, uma tupla, uma string, um dicionário ou qualquer objeto iterável. Ele é usado para repetir um bloco de código várias vezes, com base nos elementos da sequência.

A estrutura básica de um loop `for` em Python é a seguinte:

```python
for elemento in sequencia:
    # bloco de código a ser repetido
```

Aqui está uma explicação mais detalhada:

- A palavra-chave `for` inicia a declaração do loop.
- A variável `elemento` é uma variável temporária que assume o valor de cada item na sequência em cada iteração.
- A palavra-chave `in` é usada para especificar a sequência sobre a qual o loop será iterado.
- O bloco de código indentado abaixo do loop é executado para cada elemento na sequência.

Exemplo prático utilizando uma lista:

```python
frutas = ["maçã", "banana", "uva"]

for fruta in frutas:
    print(fruta)
```

Saída:

```shell
maçã
banana
uva
```

Neste exemplo, o loop `for` itera sobre a lista de frutas, e a variável `fruta` assume o valor de cada elemento da lista em cada iteração.

Os loops `for` são uma ferramenta poderosa e versátil para processar dados em Python. Eles são frequentemente usados em conjunto com funções como `range()` para gerar sequências numéricas, e também podem ser combinados com estruturas condicionais (`if`) para criar lógica mais complexa dentro do loop.

Documentação oficial: [Looping Techniques](https://docs.python.org/3/tutorial/controlflow.html#tut-loopidioms)

> [retornar](#anotações-módulo-1---introdução-ao-python) para o topo da página

### Loop `while`

Loop `while` é uma estrutura de controle de fluxo que permite executar um bloco de código repetidamente enquanto uma condição específica for verdadeira. Ao contrário do loop `for`, que itera sobre uma sequência predefinida, o loop `while` continua a execução enquanto a expressão condicional associada for avaliada como verdadeira.

A estrutura básica de um loop `while` em Python é a seguinte:

```python
while condição:
    # Código a ser executado enquanto a condição for verdadeira
    # Atenção para evitar loops infinitos, garantindo uma mudança na condição
```

A condição é uma expressão booleana que é avaliada antes de cada execução do bloco de código dentro do loop. Se a condição for verdadeira, o bloco é executado; caso contrário, o loop é encerrado, e a execução continua com o próximo trecho de código após o loop.

Exemplo de um simples loop `while`:

```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

Neste exemplo, o loop continuará executando enquanto o valor de `contador` for menor que 5. A cada iteração, o valor de `contador` é impresso, e ele é incrementado. Quando `contador` atinge 5, a condição torna-se falsa, e o loop é encerrado.

Os loops `while` são úteis em situações em que não se conhece antecipadamente o número exato de iterações necessárias, mas sim uma condição que deve ser atendida para continuar a execução.

Lembre-se de ser cuidadoso ao usar loops `while`, pois se a condição não for alterada dentro do bloco de código, pode levar a loops infinitos, travando a execução do programa.

Documentação oficial do Python sobre loops `while`: [Python While Statements](https://docs.python.org/3/reference/compound_stmts.html#the-while-statement)

> [retornar](#anotações-módulo-1---introdução-ao-python) para o topo da página

### Funções

Em Python, uma função é um bloco de código reutilizável que realiza uma tarefa específica. Ela é definida usando a palavra-chave `def` seguida pelo nome da função, parâmetros entre parênteses e um bloco de código indentado que contém a lógica da função. Aqui estão alguns aspectos relevantes sobre funções em Python:

1. **Definição de Função:**

   ```python
   def minha_funcao(parametro1, parametro2):
       # Código da função
   ```

2. **Parâmetros e Argumentos:**
   - Parâmetros são variáveis que aceitam valores passados durante a chamada da função.
   - Argumentos são os valores reais passados para os parâmetros durante a chamada da função.

3. **Retorno de Valores:**
   - A palavra-chave `return` é usada para enviar um valor de volta ao ponto de chamada da função.

   ```python
   def somar(a, b):
       return a + b
   ```

4. **Escopo de Variáveis:**
   - As variáveis definidas dentro de uma função são locais para essa função, a menos que sejam declaradas como globais.

5. **Documentação de Funções:**
   - É uma prática comum adicionar uma docstring, um bloco de texto no início da função, para descrever seu propósito, parâmetros e valores de retorno.

6. **Funções Anônimas (Lambda):**
   - Além das funções definidas com `def`, Python suporta funções anônimas usando a expressão `lambda`.

   ```python
   quadrado = lambda x: x ** 2
   ```

7. **Módulos e Bibliotecas:**
   - Funções podem ser organizadas em módulos e bibliotecas para melhorar a modularidade e reusabilidade do código.

8. **Argumentos Padrão:**
   - Parâmetros podem ter valores padrão, permitindo chamadas de função com menos argumentos.

   ```python
   def saudacao(nome, saudacao='Olá'):
       print(f'{saudacao}, {nome}!')
   ```

9. **Recursão:**
   - Funções podem chamar a si mesmas, permitindo a implementação de recursão.

   ```python
   def fatorial(n):
       if n == 0 or n == 1:
           return 1
       else:
           return n * fatorial(n-1)
   ```

10. **Decoradores:**
    - Python suporta decoradores, que são funções que modificam o comportamento de outras funções.

    ```python
    @decorador
    def minha_funcao():
        # Código da função
    ```

Para informações mais detalhadas, consulte a [documentação oficial de funções em Python](https://docs.python.org/3/tutorial/introduction.html#functions).

> [retornar](#anotações-módulo-1---introdução-ao-python) para o topo da página

### Exceções

Em Python, exceções são eventos que ocorrem durante a execução de um programa e interrompem o fluxo normal de execução. Quando ocorre uma situação excepcional, como um erro ou condição inesperada, uma exceção é gerada. Essas exceções podem ser capturadas e tratadas pelo programador, permitindo que o código lide com erros de forma elegante e controlada.

A estrutura básica para lidar com exceções em Python envolve o uso de blocos `try`, `except` e, opcionalmente, `finally`:

```python
try:
    # Código que pode gerar uma exceção
    resultado = 10 / 0  # Exemplo de divisão por zero
except ZeroDivisionError:
    # Tratamento específico para a exceção ZeroDivisionError
    print("Erro: Divisão por zero não é permitida.")
except Exception as e:
    # Tratamento genérico para outras exceções
    print(f"Erro inesperado: {e}")
finally:
    # Bloco opcional de código que é executado sempre, independentemente de exceções
    print("Finalizando o bloco try-except-finally.")
```

No exemplo acima, se ocorrer uma divisão por zero, o programa não será encerrado abruptamente. Em vez disso, ele captura a exceção `ZeroDivisionError` e executa o bloco de código dentro do bloco `except` correspondente.

Algumas exceções comuns em Python incluem `ZeroDivisionError`, `FileNotFoundError`, `TypeError`, `ValueError`, entre outras. É possível criar suas próprias exceções personalizadas para casos específicos.

Lidar adequadamente com exceções é crucial para garantir a robustez e a confiabilidade dos programas, especialmente em situações imprevisíveis.

A documentação oficial do Python sobre exceções pode ser encontrada em: [Documentação Oficial de Exceções em Python](https://docs.python.org/3/tutorial/errors.html)

> [retornar](#anotações-módulo-1---introdução-ao-python) para o topo da página

### Módulos

Em Python, o termo "módulo" refere-se a um arquivo contendo definições e instruções Python. Os módulos podem conter funções, classes e variáveis, organizando o código de forma mais modular e reutilizável. Existem dois tipos principais de módulos: módulos integrados (ou módulos embutidos) e módulos de terceiros.

1. **Módulos Integrados (Built-in Modules):**
   - **Definição:** Módulos que fazem parte da instalação padrão do Python.
   - **Exemplos:** `math`, `random`, `datetime`, `os`.
   - **Uso:** Esses módulos estão sempre disponíveis e não requerem instalação adicional. Podem ser importados diretamente no código.

   Exemplo:

   ```python
   import math
   print(math.sqrt(25))
   ```

2. **Módulos de Terceiros:**
   - **Definição:** Módulos desenvolvidos por terceiros e não fazem parte da biblioteca padrão do Python.
   - **Instalação:** Geralmente, são instalados usando ferramentas como `pip`.
   - **Exemplos:** `requests`, `numpy`, `pandas`.
   - **Uso:** Após a instalação, podem ser importados e utilizados no código.

   Exemplo (após instalação com `pip install requests`):

   ```python
   import requests
   response = requests.get("https://www.exemplo.com")
   print(response.status_code)
   ```

3. **Instalação de Módulos de Terceiros:**
   - Utiliza-se o gerenciador de pacotes `pip`.
   - Exemplo: `pip install nome_do_pacote`.

4. **Ambientes Virtuais (Virtual Environments):**
   - **Motivo:** Para evitar conflitos entre versões de pacotes e garantir isolamento.
   - **Criação:** Utiliza-se o módulo `venv` ou `virtualenv`.
   - **Exemplo:**

     ```bash
     python -m venv meu_ambiente
     source meu_ambiente/bin/activate  # No Linux/Mac
     pip install nome_do_pacote
     ```

Ao programar em Python, é comum depender tanto de módulos integrados quanto de módulos de terceiros para estender as funcionalidades do seu código. A escolha entre eles depende dos requisitos específicos do projeto.

**Documentação Oficial:**

- [Documentação Python - Módulos](https://docs.python.org/3/tutorial/modules.html)
- [Documentação Python - Ambientes Virtuais](https://docs.python.org/3/tutorial/venv.html)

> [retornar](#anotações-módulo-1---introdução-ao-python) para o topo da página
>
> [voltar](../../README.md) para página anterior
