valor = float(input("Entre com o valor: R$"))
pc = float(input("Entre com a porcentagem: "))
def gorjeta(vl, pc):
    return vl * pc
print(f"Gorjeta: R${gorjeta(valor, pc)}")
