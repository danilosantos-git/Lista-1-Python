# 7. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros
# quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6
# metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em
# galões de 3,6 litros, que custam R$ 25,00. Informe ao usuário as quantidades de tinta a serem
# compradas e os respectivos preços em 3 situações:
# a. comprar apenas latas de 18 litros;
# b. comprar apenas galões de 3,6 litros;
# c. misturar latas e galões, de forma que o preço seja o menor.

import math

# Solicita ao usuário o tamanho em metros quadrados da área a ser pintada
area_a_pintar = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

# Define as informações sobre a tinta
cobertura_litros_por_metro_quadrado = 1 / 6  # cobertura de 1 litro para 6 metros quadrados
litros_por_lata = 18
preco_lata = 80.00
litros_por_galao = 3.6
preco_galao = 25.00

# Calcula a quantidade de tinta necessária
quantidade_litros_necessarios = area_a_pintar * cobertura_litros_por_metro_quadrado

# Calcula as opções de compra
quantidade_latas = math.ceil(quantidade_litros_necessarios / litros_por_lata)
preco_total_latas = quantidade_latas * preco_lata

quantidade_galoes = math.ceil(quantidade_litros_necessarios / litros_por_galao)
preco_total_galoes = quantidade_galoes * preco_galao

# Misturar latas e galões de forma que o preço seja o menor
quantidade_latas_misturadas = int(quantidade_litros_necessarios / litros_por_lata)
resto_litros = quantidade_litros_necessarios % litros_por_lata
quantidade_galoes_misturados = math.ceil(resto_litros / litros_por_galao)

preco_total_misturado = (quantidade_latas_misturadas * preco_lata) + (quantidade_galoes_misturados * preco_galao)

# Exibe os resultados
print(f"a. Comprar apenas latas de 18 litros:")
print(f"   Quantidade de latas necessárias: {quantidade_latas}")
print(f"   Preço total: R${preco_total_latas:.2f}")

print("\nb. Comprar apenas galões de 3,6 litros:")
print(f"   Quantidade de galões necessários: {quantidade_galoes}")
print(f"   Preço total: R${preco_total_galoes:.2f}")

print("\nc. Misturar latas e galões, de forma que o preço seja o menor:")
print(f"   Quantidade de latas: {quantidade_latas_misturadas}")
print(f"   Quantidade de galões: {quantidade_galoes_misturados}")
print(f"   Preço total: R${preco_total_misturado:.2f}")
