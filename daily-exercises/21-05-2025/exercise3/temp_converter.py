# 3- Conversor de Temperatura

# Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 
# O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.

temperature = float(input("INSIRA A TEMPERATURA: "))
origin = input("INSIRA A MEDIDA DE ORIGEM (C/F/K): ").strip().upper()
target = input("INSIRA A MEDIDA DESEJADA (C/F/K): ").strip().upper()

tup = {
    "C": {
        "K": lambda valor: valor + 273.15,
        "F": lambda valor: (valor * 9/5) + 32
    },
    "K": {
        "C": lambda valor: valor - 273.15,
        "F": lambda valor: (valor - 273.15) * 9/5 + 32
    },
    "F": {
        "C": lambda valor: (valor - 32) * 5/9,
        "K": lambda valor: (valor - 32) * 5/9 + 273.15
    }
}

converted_temperature = temperature if origin == target else tup[origin][target](temperature)
print(f"{temperature}º{origin} = {converted_temperature}º{target}")