# 4 - Calculadora de Preço Total
price = float(input("Price: R$"))
quantity = int(input("Qauntity: "))

print("Total: R${:.2f}".format(price*quantity))