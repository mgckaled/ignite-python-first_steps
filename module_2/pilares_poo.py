from abc import ABC, abstractmethod

print("\nExemplo de herança:")


class Animal:
    """Representa um animal.

    Esta classe é a classe base para diferentes tipos de animais.
    Fornece métodos básicos como 'andar' e 'emitir_som'.

    Attributes:
        nome (str): O nome do animal.

    Methods:
        __init__(self, nome: str) -> None:
            Inicializa um novo animal com o nome fornecido.

        andar(self) -> None:
            Faz o animal andar e imprime uma mensagem.

        emitir_som(self) -> None:
            Método abstrato para emitir um som. Deve ser implementado
            pelas subclasses.

    """

    def __init__(self, nome: str) -> None:
        """Inicializa um novo animal com o nome fornecido.

        Args:
            nome (str): O nome do animal.
        """
        self.nome = nome

    def andar(self) -> None:
        """Faz o animal andar e imprime uma mensagem."""
        return print(f"O animal {self.nome} andou")

    def emitir_som(self) -> None:
        """Método abstrato para emitir um som.

        Este método deve ser implementado pelas subclasses.
        """
        raise NotImplementedError("Subclasses devem implementar este método.")


class Cachorro(Animal):
    """Representa um cachorro, uma subclasse de Animal.

    Esta classe herda da classe Animal e implementa o método
    'emitir_som' para representar o som de um cachorro.

    Methods:
        emitir_som(self) -> str:
            Retorna o som característico de um cachorro.

    """

    def emitir_som(self) -> str:
        """Retorna o som característico de um cachorro."""
        return "Au, au"


class Gato(Animal):
    """Representa um gato, uma subclasse de Animal.

    Esta classe herda da classe Animal e implementa o método
    'emitir_som' para representar o som de um gato.

    Methods:
        emitir_som(self) -> str:
            Retorna o som característico de um gato.

    """

    def emitir_som(self) -> str:
        """Retorna o som característico de um gato."""
        return "Miau!"


dog = Cachorro(nome="Rex")
cat = Gato(nome="Felix")
cat.andar()
dog.emitir_som()

print("\nExemplo de polimorfismo")
animais = [dog, cat]

for animal in animais:
    print(f"{animal.nome} faz: {animal.emitir_som()}")

print("\nExemplo de encapsulamento:")


class ContaBancaria:
    """Representa uma conta bancária.

    Esta classe permite realizar operações básicas em uma conta bancária,
    como depósito, saque e consulta de saldo.

    Atributos:
    __saldo (float): Saldo da conta bancária (atributo privado).

    Métodos:
    __init__(self, saldo: float) -> None:
        Inicializa a conta bancária com um saldo inicial.

    depositar(self, valor: float) -> None:
        Realiza um depósito na conta bancária.

    sacar(self, valor: float) -> None:
        Realiza um saque na conta bancária.

    consultar_saldo(self) -> float:
        Retorna o saldo atual da conta bancária.
    """

    def __init__(self, saldo: float) -> None:
        """Inicializa a conta bancária com um saldo inicial.

        Args:
        saldo (float): Saldo inicial da conta bancária.
        """
        self.__saldo = saldo

    def depositar(self, valor: float) -> None:
        """Realiza um depósito na conta bancária.

        O valor do depósito deve ser maior que zero.

        Args:
        valor (float): Valor a ser depositado na conta.
        """
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor: float) -> None:
        """Realiza um saque na conta bancária.

        O valor do saque deve ser maior que zero e não pode exceder o saldo atual.

        Args:
        valor (float): Valor a ser sacado da conta.
        """
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor

    def consultar_saldo(self) -> float:
        """Retorna o saldo atual da conta bancária.

        Returns:
        float: Saldo atual da conta bancária.
        """
        return self.__saldo


conta = ContaBancaria(saldo=1000)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
conta.depositar(valor=500)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
conta.depositar(valor=-500)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
conta.sacar(valor=2000)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")

conta_do_zezinho = ContaBancaria(saldo=50)

print("\nExemplo de abstração:")


class Veiculo(ABC):
    """Classe abstrata representando um veículo."""

    @abstractmethod
    def ligar(self):
        """Método abstrato para ligar o veículo."""
        raise NotImplementedError("Subclasses devem implementar este método.")

    @abstractmethod
    def desligar(self):
        """Método abstrato para desligar o veículo."""
        raise NotImplementedError("Subclasses devem implementar este método.")


class Carro(Veiculo):
    """Classe que representa um carro, derivada da classe Veiculo."""

    def __init__(self, modelo: str, cor: str) -> None:
        """Inicializador da classe Carro.

        Args:
            modelo (str): O modelo do carro.
            cor (str): A cor do carro.
        """
        self.modelo = modelo
        self.cor = cor
        self.ignicao = False  # Indica se o carro está ligado ou desligado

    def ligar(self):
        """Método para ligar o carro.

        Returns:
            str: Mensagem indicando que o carro foi ligado usando a chave.
        """
        if not self.ignicao:
            self.ignicao = True
            return f"{self.modelo} {self.cor} ligado usando a chave"
        else:
            return f"{self.modelo} {self.cor} já está ligado"

    def desligar(self):
        """Método para desligar o carro.

        Returns:
            str: Mensagem indicando que o carro foi desligado usando a chave.
        """
        if self.ignicao:
            self.ignicao = False
            return f"{self.modelo} {self.cor} desligado usando a chave"
        else:
            return f"{self.modelo} {self.cor} já está desligado"


# Exemplo de uso
meu_carro_1 = Carro(modelo="Civic", cor="preto")
meu_carro_2 = Carro(modelo="Gol", cor="branco")

print(meu_carro_1.ligar())  # Saída: Civic preto ligado usando a chave
print(meu_carro_1.desligar())  # Saída: Civic preto desligado usando a chave
print(meu_carro_1.desligar())  # Saída: Civic preto já está desligado

print(meu_carro_2.ligar())
print(meu_carro_2.desligar())
print(meu_carro_2.desligar())
