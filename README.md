# TS: sistema gerenciamento de produtos

## Descrição

Desafio: API para gerenciamento de produtos com teste unitário e verificação de cobertura de testes.

Construído sobre uma plataforma DRF

## Instruções instalação e execução com docker-compose

- Configure as opções de: migrations, user_admin, pytest (com ou sem relatório) e runserver, em:

> scripts/run.sh

- No terminal execute:

```sh
docker-compose up
```

## Instruções de instalação local

- Instale o Python:

```sh
pyenv local 3.9.5
```

- Configure o ambiente virtual:

```sh
poetry install
```

- Acesse o ambiente virtual:

```sh
poetry shell
```

- Execute o flake8:

```sh
flake8 .
```

## Autor(es)

- Danilo
