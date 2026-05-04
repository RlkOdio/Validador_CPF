# Encontrei essa biblioteca chamada "validate-docbr" que pode ser usada para validar CPF. Você pode instalá-la usando pip:
# Comando que utilizei para importar a biblioteca externa: "pip install validate-docbr"

from validate_docbr import CPF

validador = CPF()

documento = input("Digite o CPF para validação: ")

if validador.validate(documento):
    print("CPF válido!")
else:
    print("CPF inválido!")
