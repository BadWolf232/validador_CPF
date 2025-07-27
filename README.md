
# Validador de CPF em Python

Este projeto é um **exercício em Python** que implementa um validador de CPF (Cadastro de Pessoa Física), com verificação da quantidade de dígitos e dos dígitos verificadores, conforme as regras da Receita Federal do Brasil.

## Funcionalidades

- Remove automaticamente qualquer caractere não numérico do CPF.
- Verifica se o CPF possui 11 dígitos.
- Calcula e valida os dois dígitos verificadores.
- Retorna se o CPF é válido ou inválido com mensagens explicativas.

## Estrutura

- `validador_cpf.py`: Contém a classe `validacpf`, responsável pela validação do CPF.
- `main.py`: Arquivo principal para execução de testes. Utiliza a biblioteca [`cpf-generator`](https://github.com/matAlmeida/cpf-generator) para gerar CPFs de teste automaticamente.

## Requisitos

- Python 3.6+
- Biblioteca `cpf-generator`

Instale a biblioteca com:

```bash
pip install cpf-generator
```

## Como executar

Execute o arquivo `main.py`:

```bash
python main.py
```

A saída mostrará um CPF gerado automaticamente e o resultado da validação.

---

Este projeto é de caráter educacional e foi desenvolvido como prática de programação com classes, métodos e expressões regulares em Python.
