# 4- Verificador de Ano Bissexto

# Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não. 
# Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não são divisíveis por 400.

year = int(input("INSIRA UM ANO: "))

is_leap_year = (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))

print(("É" if is_leap_year else "Não é") + " bissexto")