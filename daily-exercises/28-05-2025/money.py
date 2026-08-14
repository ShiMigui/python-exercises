import requests
from datetime import datetime

def fetch(origin):
    try:
        url = f"https://economia.awesomeapi.com.br/last/{origin}-BRL"
        r = requests.get(url).json()
        c = r[f"{origin}BRL"]
        return (
            f"{origin} para BRL\nValor: R$ {float(c['bid']):.2f}\nMáxima: R$ {float(c['high']):.2f}\nMínima: R$ {float(c['low']):.2f}\nData/Hora: {datetime.fromtimestamp(int(c['timestamp']))}"
        )
    except:
        return "Erro ao obter cotação ou moeda inválida."

origin = input("Código da moeda (ex: USD, EUR): ").upper()
print(fetch(origin))