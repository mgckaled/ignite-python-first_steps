<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD014 -->

# Ignite Trilha Python - Primeiros Passos

<div align="center">
   <img alt="logo trilha" src=".github/assets/trilha-rs.png" width="35%"/>
</div>

<br>

<div align="center">
  <img alt="Made by mgckaled" src="https://img.shields.io/badge/made%20by-mgckaled-darkblue">
  <img alt="GitHub Repo Size" src="https://img.shields.io/github/repo-size/mgckaled/ignite-python-first_steps">
  <img alt="pylint badge" src="https://img.shields.io/badge/linting-pylint-yellowgreen">
  <img alt="License" src="https://img.shields.io/static/v1?label=license&message=MIT&color=49AA26&labelColor=000000">
</div>

## Sumário

- [Ignite Trilha Python - Primeiros Passos](#ignite-trilha-python---primeiros-passos)
  - [Sumário](#sumário)
  - [Sobre o Projeto](#sobre-o-projeto)
    - [Módulo 1 - Introdução ao Python](#módulo-1---introdução-ao-python)
    - [Módulo 2 - Programação Orientada a Objetos](#módulo-2---programação-orientada-a-objetos)
    - [Desafio](#desafio)
      - [Regras da aplicação](#regras-da-aplicação)
  - [Tecnologias](#tecnologias)
    - [Linguagem de Programação](#linguagem-de-programação)
    - [Gerenciadores de Ambiente Virtual](#gerenciadores-de-ambiente-virtual)
    - [Bibliotecas Instaladas (Packages)](#bibliotecas-instaladas-packages)
  - [Como clonar o projeto?](#como-clonar-o-projeto)
  - [Licença](#licença)

## Sobre o Projeto

Repositório dos dois primeiros módulos da trilha Python 2024, desenvolvido pela Rocketseat Education.

> Perguntas e Respostas dos [**quizzes**](./.github/docs/quizzes.md).

### Módulo 1 - Introdução ao Python

Este módulo introdutório é um mergulho profundo nos fundamentos da programação em Python, além de preparar o cenário para um projeto prático e desafiador de gerenciamento de tarefas. Inicialmente, oferecemos uma introdução abrangente ao Python, contemplando desde a instalação em diferentes sistemas até a criação do primeiro programa e uma exploração detalhada da sintaxe Python.

> Acessar [**anotações**](./.github/docs/notes_m1.md) do módulo

### Módulo 2 - Programação Orientada a Objetos

Módulo imersivo em Programação Orientada a Objetos (POO) em Python. Aprenda fundamentos como herança, polimorfismo, encapsulamento e decoradores. Cada aula aprofunda conceitos, proporcionando base sólida. Projeto prático: jogo de combate em turnos aplicando conhecimento adquirido. Ao final, domine POO em Python para aplicação eficaz em projetos futuros.

> Acessar [**anotações**](./.github/docs/notes_m2.md) do módulo

### Desafio

Nesse desafio desenvolveremos uma agenda para salvar, editar, deletar e marcar um contato como favorito. O resultado da aplicação deve ser apresentado no terminal, assim como foi visto no módulo “Introdução ao Python”.

Link com instruções: [desafio](https://efficient-sloth-d85.notion.site/Desafio-01-622bb29769034c9ba659f2dc33019055)

#### Regras da aplicação

- A aplicação deve iniciar mostrando uma lista de opções do que é possível fazer com o app e permitir que o usuário digite uma escolha para iniciar a aplicação.
- Deve ser possível adicionar um contato
  - O contato pode ter os dados:
  - Nome
  - Telefone
  - Email
  - Favorito (está opção é para poder marcar um contato como favorito)
- Deve ser possível visualizar a lista de contatos cadastrados
- Deve ser possível editar um contato
- Deve ser possível marcar/desmarcar um contato como favorito
- Deve ser possível ver uma lista de contatos favoritos
- Deve ser possível apagar um contato

## Tecnologias

### Linguagem de Programação

- [`python`](https://www.python.org/) (v3.11.5)

### Gerenciadores de Ambiente Virtual

- [`pyenv`](https://github.com/pyenv/pyenv)
- [`pipenv`](https://pipenv.pypa.io/en/latest/)

### Bibliotecas Instaladas (Packages)

- [`pylint`](https://pylint.pycqa.org/en/latest/index.html)
- [`requests`](https://requests.readthedocs.io/en/latest/)

## Como clonar o projeto?

1. Certifique-se de que está usando o `pyenv` e o `pipenv` para gerenciar as dependências do projeto. Veja como instalar e configurar clicando nos respectivos links do tópico [Gerenciadores de Ambiente Virtual](#gerenciadores-de-ambiente-virtual).

2. Faça o clone pelo Github:

    ```shell
    $ git clone https://github.com/mgckaled/ignite-devia-supervised_algorithms.git
    ```

3. Acesse o diretório:

    ```shell
    $ cd ignite-devia-supervised_algorithms
    ```

4. Instale as dependências e ative o ambiente virtual

    ```shell
    $ pipenv install -r requirements.txt
    $ pipenv shell
    ```

## Licença

Distribuído sob a licença *MIT*. Veja [LICENSE](LICENSE) para mais informações.

---

<h5 align="center">
  2024 - <a href="https://github.com/mgckaled/">Marcel Kaled</a>
</h5>
