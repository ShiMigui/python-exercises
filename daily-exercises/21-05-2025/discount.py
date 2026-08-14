# 2- Calculadora de Desconto
# Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

#   Nome do produto: "Camiseta"
#   Preço original: R$ 50.00
#   Porcentagem de desconto: 20%
# O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.

product_name = "Camiseta"
original_price = 50.0
discount_percentage = .2

discount_price = original_price * discount_percentage
discounted_price = original_price - discount_price

print(f"PRODUTO: {product_name}")
print(f"ORIGINAL: R${original_price:.2f}")
print(f"DESCONTO: {discount_percentage * 100:.0f}% -> R${discount_price:.2f}")
print(f"TOTAL: R${discounted_price:.2f}")