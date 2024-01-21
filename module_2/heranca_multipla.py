class Animal:
    """Representa um animal genérico.

    Esta classe é a classe base para outros tipos de animais.
    """

    def __init__(self, nome):
        """Inicializa um novo animal.

        Parameters:
        - nome (str): O nome do animal.
        """
        self.nome = nome

    def emitir_som(self):
        """Método abstrato para emitir um som.

        Este método deve ser implementado pelas classes filhas para representar
        o som específico do animal.
        """
        raise NotImplementedError("Subclasses devem implementar este método.")

    def mover(self):
        """Método para simular o movimento do animal.

        Returns:
        str: Uma mensagem indicando que o animal está se movendo.
        """
        return f"{self.nome} está se movendo."

    def dormir(self):
        """Método para simular o sono do animal.

        Returns:
        str: Uma mensagem indicando que o animal está dormindo.
        """
        return f"{self.nome} está dormindo."


class Mamifero(Animal):
    """Representa um mamífero.

    Esta classe herda de Animal e adiciona funcionalidades específicas para mamíferos.
    """

    def amamentar(self):
        """Realiza a amamentação.

        Returns:
        str: Uma mensagem indicando que o mamífero está amamentando.
        """
        return f"{self.nome} está amamentando."

    def emitir_som(self):
        """Método abstrato para emitir um som.

        Este método deve ser implementado pelas classes filhas para representar
        o som específico do animal.
        """
        raise NotImplementedError("Subclasses devem implementar este método.")


class Ave(Animal):
    """Representa uma ave.

    Esta classe herda de Animal e adiciona funcionalidades específicas para aves.
    """

    def voar(self):
        """Realiza o voo.

        Returns:
        str: Uma mensagem indicando que a ave está voando.
        """
        return f"{self.nome} está voando."

    def emitir_som(self):
        """Método abstrato para emitir um som.

        Este método deve ser implementado pelas classes filhas para representar
        o som específico do animal.
        """
        raise NotImplementedError("Subclasses devem implementar este método.")


class Morcego(Mamifero, Ave):
    """Representa um morcego.

    Esta classe herda de Mamifero e Ave, combinando características de ambos.
    """

    def emitir_som(self):
        """Emite um som ultrassônico.

        Returns:
        str: Uma mensagem indicando que morcegos emitem sons ultrassônicos.
        """
        return "Morcegos emitem sons ultrassônicos."


morcego = Morcego(nome="Batman")

# Acessando métodos da classe base `Animal`
print("Nome do morcego:", morcego.nome)
print("Som do morcego:", morcego.emitir_som())

# Acessando métodos das classes `Mamifero` e `Ave`
print("Morcego amamentando:", morcego.amamentar())
print("Morcego voando:", morcego.voar())
print(morcego.mover())
print(morcego.dormir())
