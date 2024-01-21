class Contato:
    """Representa um contato na agenda."""

    def __init__(self, nome, telefone, email, favorito=False):
        """
        Inicializa um objeto Contato.

        Args:
            nome (str): Nome do contato.
            telefone (str): Número de telefone do contato.
            email (str): Endereço de e-mail do contato.
            favorito (bool, opcional): Indica se o contato é favorito. Padrão é False.
        """
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.favorito = favorito


class Agenda:
    """Representa uma agenda de contatos."""

    def __init__(self):
        """Inicializa uma agenda vazia."""
        self.contatos = []

    def adicionar_contato(self, contato):
        """
        Adiciona um contato à agenda.

        Args:
            contato (Contato): Objeto Contato a ser adicionado à agenda.
        """
        self.contatos.append(contato)

    def mostrar_contatos(self):
        """Mostra todos os contatos na agenda."""
        for i, contato in enumerate(self.contatos, 1):
            print(
                f"{i}. {contato.nome} - {contato.telefone} - {contato.email} {'(Favorito)' if contato.favorito else ''}"
            )

    def editar_contato(self, indice, novo_contato):
        """
        Edita um contato na agenda.

        Args:
            indice (int): Índice do contato a ser editado.
            novo_contato (Contato): Novo objeto Contato que substituirá o contato existente.
        """
        self.contatos[indice] = novo_contato

    def marcar_favorito(self, indice):
        """
        Alterna o status de favorito de um contato.

        Args:
            indice (int): Índice do contato a ter o status de favorito alterado.
        """
        self.contatos[indice].favorito = not self.contatos[indice].favorito

    def contatos_favoritos(self):
        """Mostra todos os contatos favoritos na agenda."""
        favoritos = [contato for contato in self.contatos if contato.favorito]
        if favoritos:
            for i, contato in enumerate(favoritos, 1):
                print(f"{i}. {contato.nome} - {contato.telefone} - {contato.email}")
        else:
            print("Nenhum contato favorito.")

    def apagar_contato(self, indice):
        """
        Remove um contato da agenda.

        Args:
            indice (int): Índice do contato a ser removido.
        """
        del self.contatos[indice]


def main():
    """
    Função principal que inicia a aplicação da agenda de contatos.

    Esta função cria uma instância da classe `Agenda` e apresenta um menu interativo
    para que o usuário possa realizar diversas operações em sua lista de contatos.

    Menu:
    1. Adicionar Contato
    2. Visualizar Contatos
    3. Editar Contato
    4. Marcar/Desmarcar como Favorito
    5. Ver Contatos Favoritos
    6. Apagar Contato
    0. Sair

    A função continua a solicitar opções até que o usuário escolha sair digitando '0'.

    Exemplos de Uso: main()

    Notas:
    - A função utiliza a classe `Agenda` para gerenciar a lista de contatos.
    - O usuário interage com a aplicação através de entradas no console.

    :return: Nenhum retorno direto, a execução continua até que o usuário escolha sair.
    """

    agenda = Agenda()

    while True:
        print("\n### Menu ###")
        print("1. Adicionar Contato")
        print("2. Visualizar Contatos")
        print("3. Editar Contato")
        print("4. Marcar/Desmarcar como Favorito")
        print("5. Ver Contatos Favoritos")
        print("6. Apagar Contato")
        print("0. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            favorito = input("Marcar como favorito? (S/N): ").upper() == "S"
            novo_contato = Contato(nome, telefone, email, favorito)
            agenda.adicionar_contato(novo_contato)

        elif escolha == "2":
            agenda.mostrar_contatos()

        elif escolha == "3":
            agenda.mostrar_contatos()
            indice = int(input("Digite o número do contato que deseja editar: ")) - 1
            novo_nome = input("Novo Nome: ")
            novo_telefone = input("Novo Telefone: ")
            novo_email = input("Novo Email: ")
            novo_contato = Contato(
                novo_nome, novo_telefone, novo_email, agenda.contatos[indice].favorito
            )
            agenda.editar_contato(indice, novo_contato)

        elif escolha == "4":
            agenda.mostrar_contatos()
            indice = (
                int(
                    input(
                        "Digite o número do contato que deseja marcar/desmarcar como favorito: "
                    )
                )
                - 1
            )
            agenda.marcar_favorito(indice)

        elif escolha == "5":
            agenda.contatos_favoritos()

        elif escolha == "6":
            agenda.mostrar_contatos()
            indice = int(input("Digite o número do contato que deseja apagar: ")) - 1
            agenda.apagar_contato(indice)

        elif escolha == "0":
            print("Saindo da aplicação. Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
