# 3. Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius. C = (5 * (F-32) / 9).

# Solicita ao usuário a temperatura em graus Fahrenheit
temperatura_fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))

# Converte a temperatura para Celsius usando a fórmula
temperatura_celsius = (5 * (temperatura_fahrenheit - 32)) / 9

# Exibe o resultado
print(f"A temperatura em graus Celsius é: {temperatura_celsius:.2f}°C")
