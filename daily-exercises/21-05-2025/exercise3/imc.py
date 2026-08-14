# 2- Calculadora de IMC

# Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa. 
# O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário, 
# calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

#   < 18.5: classificacao = "Abaixo do peso"
#   < 25: classificacao = "Peso normal"
#   < 30: classificacao = "Sobrepeso"
# Para os demais cenários: classificacao = "Obeso"

weight = float(input("INSIRA O PESO (kg): "))
height = float(input("INSIRA A ALTURA (m): "))

IMC = weight / height**2

if IMC < 0: info = "Pior que mentir para um programa de computador é mentir para si mesmo!"
elif IMC < 18.5: info = "Abaixo do peso"
elif IMC < 25: info = "Peso normal"
elif IMC < 30: info = "Sobrepeso"
else: info = "Obeso"

print(f"IMC: {IMC:.2f}")
print(f"STATUS: {info}")