import random


# Personagem: classe mae
class Personagem:
    """
    The `Personagem` class represents a character with attributes such as name, health, and level, and has methods for displaying details, receiving attacks, and attacking other characters.
    """

    def __init__(self, nome, vida, nivel):
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel

    def get_nome(self):
        """
        The function "get_nome" returns the value of the private attribute "__nome".
        :return: The method `get_nome` is returning the value of the private attribute `__nome`.
        """
        return self.__nome

    def get_vida(self):
        """
        The function returns the value of the private variable "vida".
        :return: The method is returning the value of the private variable "__vida".
        """
        return self.__vida

    def get_nivel(self):
        """
        The function returns the value of the private variable __nivel.
        :return: The value of the private attribute "__nivel".
        """
        return self.__nivel

    def exibir_detalhes(self):
        """
        The function "exibir_detalhes" returns a string containing the name, life, and level of an object.
        :return: The method is returning a string that displays the name, life, and level of an object.
        """
        return f"Nome: {self.get_nome()}\nVida: {self.get_vida()}\nNível: {self.get_nivel()}"

    def receber_ataque(self, dano):
        """
        The function "receber_ataque" reduces the value of the variable "__vida" by the amount of "dano" and sets it to 0 if
        it becomes negative.

        :param dano: The parameter "dano" represents the amount of damage that the object is receiving from an attack
        """
        self.__vida -= dano
        if self.__vida < 0:
            self.__vida = 0

    def atacar(self, alvo):
        """
        The function "atacar" calculates the damage based on the level of the attacker, attacks the target with that damage,
        and prints a message about the attack.

        :param alvo: The parameter "alvo" represents the target that the character is attacking. It is expected to be an
        instance of a class that has a method called "receber_ataque" and a method called "get_nome"
        """
        dano = random.randint(
            self.get_nivel() * 2, self.get_nivel() * 4
        )  # baseado no nivel
        alvo.receber_ataque(dano)
        print(f"{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano!")


# Heroi: controlado pelo usuario
class Heroi(Personagem):
    """
    The `Heroi` class is a subclass of `Personagem` that represents a hero character with a special ability.
    """

    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade

    def get_habilidade(self):
        """
        The function "get_habilidade" returns the value of the private attribute "__habilidade".
        :return: The method is returning the value of the private attribute "__habilidade".
        """
        return self.__habilidade

    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nHabilidade: {self.get_habilidade()}\n"

    def ataque_especial(self, alvo):
        """
        The function "ataque_especial" performs a special attack on a target, dealing increased damage.

        :param alvo: The parameter "alvo" represents the target of the special attack. It is expected to be an instance of a
        class that has a method called "receber_ataque" and a method called "get_nome"
        """
        dano = random.randint(
            self.get_nivel() * 5, self.get_nivel() * 8
        )  # Dano aumentado
        alvo.receber_ataque(dano)
        print(
            f"{self.get_nome()} usou a habilidade especial {self.get_habilidade()} em {alvo.get_nome()} e causou {dano} de dano!"
        )


# Inimigo: adversario do usuario
class Inimigo(Personagem):
    """
    The Inimigo class is a subclass of the Personagem class and represents an adversary with a specific type.
    """

    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo

    def get_tipo(self):
        """
        The function returns the value of the private variable "__tipo".
        :return: The method `get_tipo` is returning the value of the private attribute `__tipo`.
        """
        return self.__tipo

    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nTipo: {self.get_tipo()}\n"


class Jogo:
    """Classe orquestradora do jogo"""

    def __init__(self) -> None:
        self.heroi = Heroi(nome="Herói", vida=100, nivel=5, habilidade="Super Força")
        self.inimigo = Inimigo(nome="Morcego", vida=80, nivel=5, tipo="Voador")

    def iniciar_batalha(self):
        """Fazer a gestão da batalha em turnos"""
        print("Iniciando batalha!")
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print("\nDetalhes dos Personagens:")
            print(self.heroi.exibir_detalhes())
            print(self.inimigo.exibir_detalhes())

            input("Pressione Enter para atacar...")
            escolha = input("Escolha (1 - Ataque Normal, 2 - Ataque Especial): ")

            if escolha == "1":
                self.heroi.atacar(self.inimigo)
            elif escolha == "2":
                self.heroi.ataque_especial(self.inimigo)
            else:
                print("Escolha inválida. Escolha novamente.")

            if self.heroi.get_vida() > 0:
                # Inimigo ataca o heroi
                self.inimigo.atacar(self.heroi)

        if self.heroi.get_vida() > 0:
            print("\nParabéns você venceu a batalha!")
        else:
            print("\nVocê foi derrotado!")


# Criar instância do jogo e iniciar batalha
jogo = Jogo()
jogo.iniciar_batalha()
