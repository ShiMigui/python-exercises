from requests import get

cep = input("CEP: ")

resp = get(f"https://viacep.com.br/ws/{cep}/json/")

obj = resp.json()

print(f"{obj['bairro']}, {obj['localidade']} - {obj['uf']}\nRua: {obj['logradouro']}")