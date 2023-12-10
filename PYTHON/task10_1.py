# 10. Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os
# valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é:
# equilátero, isósceles ou escaleno.

# Solicita ao usuário os três lados do triângulo
lado1 = float(input("Digite o comprimento do primeiro lado do triângulo: "))
lado2 = float(input("Digite o comprimento do segundo lado do triângulo: "))
lado3 = float(input("Digite o comprimento do terceiro lado do triângulo: "))

# Verifica se os lados formam um triângulo
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    # Verifica o tipo de triângulo
    if lado1 == lado2 == lado3:
        tipo = "Equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        tipo = "Isósceles"
    else:
        tipo = "Escaleno"

    # Exibe o resultado
    print(f"Os lados formam um triângulo {tipo}.")
else:
    print("Os lados informados não formam um triângulo válido.")
