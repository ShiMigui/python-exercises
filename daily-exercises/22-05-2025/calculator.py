operations = {
    '-': lambda a, b: a - b,
    '+': lambda a, b: a + b,
    '/': lambda a, b: a / b,
    '*': lambda a, b: a * b,
}

while True:
    try:
        num1=float(input("INSIRA UM NÚMERO: "))
        num2=float(input("INSIRA UM NÚMERO: "))
        op=input("INSITA A OPERAÇÃO: (+, -, *, /)")
        if op not in operations:
            raise ValueError('Operação inválida!')
        
        result = operations[op](num1, num2)
        break
    except ValueError as e:
        print(f"Erro: {e}")
    except ZeroDivisionError:
        print("Erro: divisão por zero!")

print(f'{num1} {op} {num2} = {result}')