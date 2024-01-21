"""
Nesta aula, vamos mergulhar no mundo da programação orientada a objetos (POO). 
Uma linguagem de programação orientada a objetos adota e implementa os princípios 
e conceitos da POO. Essas linguagens, como Python, Java, C++, C Sharp e Ruby, permitem 
que os programadores criem softwares de forma modular, reutilizável e mais fácil de 
entender e manter. A POO é um paradigma de programação que se baseia na organização 
dos programas em torno de objetos, que são instâncias de classes. 
As classes são modelos que definem a estrutura e o comportamento dos objetos. 
Dentro das classes, podemos descrever atributos e métodos, que são as ações 
que os objetos podem realizar. O construtor é um método especial que 
nos permite definir os atributos da classe.
"""


class Pessoa:
    """
    The class "Pessoa" represents a person with a name and age, and has a method to greet.
    """

    def __init__(self, nome, idade) -> None:
        """
        The above function is a constructor that initializes the attributes "nome" and "idade" of an object.

        :param nome: The parameter "nome" is used to store the name of an object. It is a string that represents the name ofthe object
        :param idade: The parameter "idade" represents the age of an object or entity
        """

        self.nome = nome
        self.idade = idade

    def saudacao(self):
        """
        The function returns a greeting message with the name and age of the person.
        :return: a string that includes the name and age of the object.
        """

        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."


# Objetos
pessoa1 = Pessoa("Alice", 30)
mensagem = pessoa1.saudacao()
print(mensagem)

pessoa2 = Pessoa(nome="Rodrigo", idade=32)
mensagem = pessoa2.saudacao()
print(mensagem)
