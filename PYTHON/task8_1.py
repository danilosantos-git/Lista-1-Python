# 8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas
# trabalhadas no mês. Calcule e mostre o total do seu salário no referido
# mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5%
# para o sindicato, faça um programa que nos dê:
# a. salário bruto.
# b. quanto pagou ao INSS.
# c. quanto pagou ao sindicato.
# d. o salário líquido.

# Solicita ao usuário o valor da hora e o número de horas trabalhadas
valor_por_hora = float(input("Digite o valor que você ganha por hora: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

# Calcula o salário bruto
salario_bruto = valor_por_hora * horas_trabalhadas

# Define as taxas de desconto
taxa_ir = 0.11  # 11% para o Imposto de Renda
taxa_inss = 0.08  # 8% para o INSS
taxa_sindicato = 0.05  # 5% para o sindicato

# Calcula os descontos
desconto_ir = salario_bruto * taxa_ir
desconto_inss = salario_bruto * taxa_inss
desconto_sindicato = salario_bruto * taxa_sindicato

# Calcula o salário líquido
salario_liquido = salario_bruto - (desconto_ir + desconto_inss + desconto_sindicato)

# Exibe os resultados
print(f"a. Salário bruto: R${salario_bruto:.2f}")
print(f"b. Valor descontado para o INSS: R${desconto_inss:.2f}")
print(f"c. Valor descontado para o sindicato: R${desconto_sindicato:.2f}")
print(f"d. Salário líquido: R${salario_liquido:.2f}")
