# 9. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e
# lhe contrataram para desenvolver o programa que calculará os reajustes. Faça um programa
# que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no
# salário atual:
# - salários até R$ 280,00 (incluindo) : aumento de 20%
# - salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# - salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# - salários de R$ 1500,00 em diante: aumento de 5%
# Após o aumento ser realizado, informe na tela:
# a. o salário antes do reajuste;
# b. o percentual de aumento aplicado;
# c. o valor do aumento;
# d. o novo salário, após o aumento.

# Solicita ao usuário o salário atual do colaborador
salario_atual = float(input("Digite o salário atual do colaborador: "))

# Define as faixas de reajuste e seus respectivos percentuais
faixas_reajuste = [
    (0, 280, 0.2),      # até R$ 280,00 (20% de aumento)
    (280, 700, 0.15),    # R$ 280,00 a R$ 700,00 (15% de aumento)
    (700, 1500, 0.1),    # R$ 700,00 a R$ 1500,00 (10% de aumento)
    (1500, float('inf'), 0.05)  # R$ 1500,00 em diante (5% de aumento)
]

# Encontra a faixa de reajuste correspondente ao salário atual
for faixa in faixas_reajuste:
    inicio, fim, percentual = faixa
    if inicio <= salario_atual < fim:
        # Calcula o valor do aumento e o novo salário
        aumento = salario_atual * percentual
        novo_salario = salario_atual + aumento

        # Exibe os resultados
        print(f"a. Salário antes do reajuste: R${salario_atual:.2f}")
        print(f"b. Percentual de aumento aplicado: {percentual * 100}%")
        print(f"c. Valor do aumento: R${aumento:.2f}")
        print(f"d. Novo salário, após o aumento: R${novo_salario:.2f}")
        break
else:
    print("Erro: Salário fora das faixas de reajuste previstas.")
