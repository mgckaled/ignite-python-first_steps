# Condição verdadeira
# True
# Condição Falsa
# False

VERDADEIRO = True
FALSO = False

# Condicionais
# se condicao
# else = se não
if VERDADEIRO:
    print("Bloco IF vai ser executado")
else:
    print("Bloco ELSE não será executado")

# Operadores lógicos: and e or

# AND
if VERDADEIRO and VERDADEIRO:
    print("Bloco será executado")

if VERDADEIRO and FALSO:
    print("Bloco não será executado")

if FALSO and FALSO:
    print("Bloco não será executado")

# OR
if VERDADEIRO or FALSO:
    print("Bloco OR vai ser executado")

if FALSO or FALSO:
    print("Bloco OR não vai ser executado")

if VERDADEIRO or VERDADEIRO:
    print("Bloco OR vai ser executado")
