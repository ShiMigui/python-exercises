# 1 - Conversor de Moeda
# Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

#   Valor em reais: R$ 100.00
#   Taxa do dólar: R$ 5.20
#   Taxa do euro: R$ 6.15
# O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.

DOLLAR = 5.2
EURO = 6.15

value = 100

print(f"US$ {value / DOLLAR:.2f}")
print(f"€ {value / EURO:.2f}")