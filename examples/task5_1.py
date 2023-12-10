# 5. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# a. o produto do dobro do primeiro com metade do segundo.
# b. a soma do triplo do primeiro com o terceiro.
# c. o terceiro elevado ao cubo.

# Solicita ao usuário 2 números inteiros e 1 número real
numero_inteiro1 = int(input("Digite o primeiro número inteiro: "))
numero_inteiro2 = int(input("Digite o segundo número inteiro: "))
numero_real = float(input("Digite o número real: "))

# Calcula e exibe os resultados
resultado_a = (2 * numero_inteiro1) * (numero_inteiro2 / 2)
resultado_b = (3 * numero_inteiro1) + numero_real
resultado_c = numero_real ** 3

print(f"a. O produto do dobro do primeiro com metade do segundo é: {resultado_a}")
print(f"b. A soma do triplo do primeiro com o terceiro é: {resultado_b}")
print(f"c. O terceiro elevado ao cubo é: {resultado_c}")
