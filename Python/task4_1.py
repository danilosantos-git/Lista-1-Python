# 4. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.

# Solicita ao usuário a temperatura em graus Celsius
temperatura_celsius = float(input("Digite a temperatura em graus Celsius: "))

# Converte a temperatura para Fahrenheit usando a fórmula
temperatura_fahrenheit = (9 * temperatura_celsius / 5) + 32

# Exibe o resultado
print(f"A temperatura em graus Fahrenheit é: {temperatura_fahrenheit:.2f}°F")
