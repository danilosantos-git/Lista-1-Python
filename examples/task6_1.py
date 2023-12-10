# 6. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o
# rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o
# estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma
# multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a
# variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de
# quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os
# dados do programa com as mensagens adequadas.

# Solicita ao usuário o peso de peixes
peso_peixes = float(input("Digite o peso dos peixes em quilos: "))

# Define o limite estabelecido pelo regulamento
limite_peso = 50.0

# Verifica se houve excesso de peso
if peso_peixes > limite_peso:
    # Calcula o excesso de peso e a multa
    excesso = peso_peixes - limite_peso
    valor_multa_por_quilo = 4.00
    multa = excesso * valor_multa_por_quilo

    # Exibe os resultados
    print(f"Peso de peixes: {peso_peixes} kg")
    print(f"Limite permitido: {limite_peso} kg")
    print(f"Excesso de peso: {excesso:.2f} kg")
    print(f"Multa a pagar: R${multa:.2f}")
else:
    print("Peso dentro do limite permitido. Sem multa.")
