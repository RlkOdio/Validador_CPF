# Validador de CPF em Python

Este é um script simples em Python que utiliza a biblioteca `validate-docbr` para validar números de CPF.

---

## Como utilizar

### 1. Pré-requisitos
Certifique-se de ter o Python instalado em sua máquina.

### 2. Instalação
Abra o seu terminal ou prompt de comando e instale a biblioteca necessária:

```bash
pip install validate-docbr
```

### 3. Execução
Execute o script e digite o número do CPF quando solicitado:

```bash
python nome_do_arquivo.py
```

---

## Exemplo de uso

```text
Digite o CPF para validação: 12345678909
CPF inválido!
```

---

## Funcionalidade

O código instancia o objeto `CPF` da biblioteca `validate_docbr` e utiliza o método `.validate()` para verificar se o documento inserido respeita o algoritmo de validação de CPF brasileiro.
