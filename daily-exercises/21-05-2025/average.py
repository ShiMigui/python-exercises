# 3- Calculadora de Média Escolar
# Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:

#   Nota 1: 7.5
#   Nota 2: 8.0
#   Nota 3: 6.5
# O programa deve calcular a média e exibir todas as notas e o resultado final, arredondando para duas casas decimais.

nt1 = 7.5
nt2 = 8.0
nt3 = 6.5

average = (nt1 + nt2 + nt3) / 3

status = "PASSOU"
if average < 6.0:
    status = "NÃO PASSOU"

print("NOTAS:")
print(f"\t{nt1:.2f}")
print(f"\t{nt2:.2f}")
print(f"\t{nt3:.2f}")
print(f"MÉDIA: {average:.2f}")
print(f"STATUS: {status}")