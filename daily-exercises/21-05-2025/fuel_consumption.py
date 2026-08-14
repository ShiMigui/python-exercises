# 4- Calculadora de Consumo de Combustível
# Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

#   Distância percorrida: 300 km
#   Combustível gasto: 25 litros
# O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.
distance = 300
fuel = 25

print(f"DISTÂNCIA: {distance} km")
print(f"COMBUSTÍVEL: {fuel} litros")
print(f"CONSUMO MÉDIO: {distance / fuel:.2f} km/l")