from datetime import datetime

ano_nascimento = int(input("Digite seu ano de nascimento: "))
def calc(nascimento):
    return datetime.now().year - nascimento

idade = calc(ano_nascimento)

print(f"Sua idade é: {idade} anos")
