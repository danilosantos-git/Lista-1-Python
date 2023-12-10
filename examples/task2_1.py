# 2. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

# Solicita ao usuário o valor da hora e o número de horas trabalhadas
valor_por_hora = float(input("Digite o valor que você ganha por hora: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

# Calcula o salário total
salario_total = valor_por_hora * horas_trabalhadas

# Exibe o resultado
print(f"Seu salário total no mês é: R${salario_total:.2f}")
