class MinhaClasse:
    """
    MinhaClasse is a simple class with a class attribute and an instance method.

    Attributes:
        valor (int): A class attribute with a default value of 10.
        nome (str): An instance attribute representing the name.

    Methods:
        metodo_instancia(): A method that returns a string with the name of the instance.
    """

    valor = 10  # Atributo de classe

    def __init__(self, nome) -> None:
        self.nome = nome  # Atributo da instância

    # requer uma instância para ser chamado
    def metodo_instancia(self):
        """
        The function "metodo_instancia" is a method that returns a string with the name of the instance.
        :return: The method is returning a string that includes the name attribute of the instance.
        """
        return f"Método de instância chamado para {self.nome}"

    @classmethod
    def metodo_classe(cls):
        """
        The function `metodo_classe` is a class method that returns a string with the value of the class attribute `valor`.

        :param cls: The parameter "cls" is a reference to the class itself. It is used to access class attributes and
        methods
        :return: The method is returning a string that includes the value of the class attribute "valor".
        """
        return f"Método de classe chamado para valor={cls.valor}"

    @staticmethod
    def metodo_estatico():
        """
        The above function is a static method that returns a string.
        :return: The method is returning the string "Método estático chamado".
        """
        return "Método estático chamado"


obj = MinhaClasse(nome="Classe Exemplo")
print(obj.metodo_instancia())
print(MinhaClasse.valor)
print(MinhaClasse.metodo_classe())
print(MinhaClasse.metodo_estatico())


class Carro:
    """
    Carro is a class representing a car with attributes such as marca, modelo, and ano.

    Attributes:
        marca (str): The brand or manufacturer of the car.
        modelo (str): The model name of the car.
        ano (int): The manufacturing year of the car.

    Methods:
        __init__(self, marca, modelo, ano): The constructor method for initializing the Carro object with marca, modelo,
        and ano.
        criar_carro(cls, configuracao): A class method that takes a string "configuracao" as input and splits it into
        three parts (marca, modelo, ano), then returns an instance of the class "cls" with those values.
    """

    def __init__(self, marca, modelo, ano) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    @classmethod
    def criar_carro(cls, configuracao):
        """
        The function "criar_carro" takes a string "configuracao" as input and splits it into three parts (marca, modelo,
        ano), then returns an instance of the class "cls" with those values.

        :param cls: The parameter `cls` is a reference to the class itself. It is used when creating a new instance of the
        class
        :param configuracao: The `configuracao` parameter is a string that contains the information needed to create a car
        object. It is expected to be in the format "marca,modelo,ano", where:
        :return: The method is returning an instance of the class with the specified configuration.
        """
        marca, modelo, ano = configuracao.split(",")
        return cls(marca, modelo, int(ano))


CONFIGURACAO_1 = "Toyota, Corolla,2022"
carro1 = Carro.criar_carro(CONFIGURACAO_1)
print(f"Marca: {carro1.marca}\nModelo: {carro1.modelo}\nAno: {carro1.ano}")


# The class "Matematica" contains a static method "somar" that takes two parameters and returns their sum.
class Matematica:
    """
    The class "Matematica" contains a static method "somar" that takes two parameters and returns their sum.
    """

    @staticmethod
    def somar(a, b):
        """
        The function "somar" takes two parameters, "a" and "b", and returns their sum.

        :param a: The first parameter, `a`, is a variable that represents the first number to be added in the sum
        :param b: The parameter "b" is the second number that will be added to the first number "a" in the function "somar"
        :return: the sum of the two input parameters, `a` and `b`.
        """
        return a + b


print(Matematica.somar(a=10, b=15))
