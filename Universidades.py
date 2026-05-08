import requests
#requisicao para a API
url = "http://universities.hipolabs.com/search?country=Brazil"
resposta = requests.get(url)
print("Status: ", resposta.status_code)

#converte para dicionario
dados = resposta.json()


