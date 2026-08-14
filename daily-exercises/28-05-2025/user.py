import requests

url = "https://randomuser.me/api/"
def fetch():
    try:
        response = requests.get(url)
        dados = response.json()['results'][0]
        
        name = f"{dados['name']['first']} {dados['name']['last']}"
        mail = dados['email']
        country = dados['location']['country']

        return f"Nome: {name}\nEmail: {mail}\nPaís: {country}"
    except requests.RequestException as e:
        return f"Erro: {e}"

print(fetch())