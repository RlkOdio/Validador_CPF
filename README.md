# Validador de CPF em Python

Este projeto contém um script simples, eficiente e sem o uso de bibliotecas externas para validar números de Cadastro de Pessoas Físicas (CPF) no Brasil. Ele utiliza o algoritmo oficial de validação baseado nos dígitos verificadores.

# 🚀 Funcionalidades
Validação de formato: Verifica se a entrada possui 11 dígitos e é composta apenas por números.

Filtro de CPFs inválidos: Identifica sequências numéricas inválidas (como 111.111.111-11, mesmo que passem no cálculo dos dígitos).

Cálculo dos dígitos verificadores: Executa o algoritmo matemático da Receita Federal para garantir que os dois últimos dígitos estão corretos.

# 🧠 Como funciona a validação?
O algoritmo de validação do CPF funciona em duas etapas principais para calcular os dígitos verificadores (os dois últimos números do CPF):

Primeiro Dígito Verificador: Multiplica-se os 9 primeiros dígitos por uma sequência decrescente de 10 a 2, soma-se os resultados e aplica-se o módulo 11.

Segundo Dígito Verificador: Inclui-se o primeiro dígito verificador calculado e multiplica-se os 10 dígitos por uma sequência de 11 a 2, aplicando o mesmo cálculo de módulo.
