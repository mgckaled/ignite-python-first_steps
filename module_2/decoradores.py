def meu_decorator(func):
    """
    Um decorator simples que imprime uma mensagem antes e depois
    da execução da função decorada.

    Parameters:
    func (callable): A função a ser decorada.

    Returns:
    callable: Função decorada.
    """

    def wrapper():
        """
        Função de envoltório que adiciona mensagens de log antes e depois
        da execução da função decorada.
        """
        print("Antes da função ser chamada")
        func()
        print("Depois da função ser chamada")

    return wrapper


@meu_decorator
def minha_funcao():
    """
    Função de exemplo para demonstrar o uso do decorator.
    """
    print("Minha função foi chamada")


minha_funcao()


class MeuDecoradorDeClasse:
    """
    Um decorador de classe que imprime mensagens antes e depois da
    execução da função decorada.

    Attributes:
    func (callable): A função a ser decorada.
    """

    def __init__(self, func) -> None:
        self.func = func

    def __call__(self) -> any:  # type: ignore
        """
        Método chamado quando a instância da classe é chamada como uma função.
        Adiciona mensagens de log antes e depois da execução da função decorada.
        """
        print("Antes da função ser chamada (decorador de classe)")
        self.func()
        print("Depois da função ser chamada (decorador de classe)")


@MeuDecoradorDeClasse
def segunda_funcao():
    """
    Função de exemplo para demonstrar o uso do decorador de classe.
    """
    print("Segunda função foi chamada")


segunda_funcao()
