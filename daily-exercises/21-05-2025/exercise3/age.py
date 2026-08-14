# 1- Classificador de Idade

# Crie um programa que solicite a idade do usuário e classifique-o 
# em uma das seguintes categorias: 

#   Criança (0-12 anos), 
#   Adolescente (13-17 anos), 
#   Adulto (18-59 anos) ou 
#   Idoso (60 anos ou mais).

age = int(input("INSIRA SUA IDADE: "))

if age < 0:
    info = "Você simplesmente não existe"
elif age < 13:
    info = "Criança"
elif age < 18:
    info = "Adolescente"
elif age < 60:
    info = "Adulto"
else:
    info = "Idoso"

print(f"Classificação: {info}")