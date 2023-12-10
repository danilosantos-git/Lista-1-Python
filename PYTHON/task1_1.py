# 1. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math

# Solicita ao usuário o raio do círculo
raio = float(input("Digite o raio do círculo: "))

# Calcula a área do círculo
area = math.pi * raio**2

# Exibe o resultado
print(f"A área do círculo com raio {raio} é: {area}")
