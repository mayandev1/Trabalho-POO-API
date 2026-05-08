import requests

def requisicao_API(dados):
    # requisicao para a API
    url = "https://universities.hipolabs.com/search?country=Brazil"
    resposta = requests.get(url)
    print("Status: ", resposta.status_code)

    # converte para dicionario
    dados = resposta.json()
    return dados

def menu():
    print("===== MENU API DE UNIVERSIDADES =====")
    print("1. Listar Dados")
    print("2. Buscar um Item")
    print("3. Detalhes")
    print("4. Filtrar Dados")
    print("5. Ordenar Dados")
    print("6. Verificar Item")