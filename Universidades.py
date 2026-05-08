import requests

url = "https://universities.hipolabs.com/search?country=Brazil"
    
def requisicao_API():
    # requisicao para a API
    try:

        resposta = requests.get(url)

        if resposta.status_code == 200:
            return resposta.json()

        else:
            print("Erro ao acessar API.")
            return []

    except requests.exceptions.RequestException:
        print("Erro de conexão.")
        return []

def listar_dados(dados):
    
    print("\n===== LISTA DE UNIVERSIDADES =====\n")

    # loop para listar as universidades presentes na API
    for i, universidade in enumerate(dados[:20], start=1):

        print(f"{i}. {universidade['name']}")

    print()
    

# função de busca
def buscar_item(dados):
    
    nome = input("\nDigite o nome da universidade: ").lower()

    encontrados = [
        universidade for universidade in dados
        if nome in universidade["name"].lower()
    ]

    if encontrados:

        print("\n===== RESULTADOS =====\n")

        for universidade in encontrados:

            print(universidade["name"])

    else:
        print("Universidade não encontrada.")

# função que lista todos os detalhes da universidade solicitada
def mostrar_detalhes(dados):
    
    nome = input("\nDigite o nome da universidade: ").lower()

    for universidade in dados:

        if nome in universidade["name"].lower():

            print("\n===== DETALHES =====\n")

            print("Nome:", universidade.get("name"))
            print("País:", universidade.get("country"))
            print("Código:", universidade.get("alpha_two_code"))
            print("Domínio:", universidade.get("domains", ["Sem domínio"])[0])
            print("Site:", universidade.get("web_pages", ["Sem páginas web"])[0])
            print("Estado:", universidade.get("state-province"))

            return

    print("Universidade não encontrada.")

# def filtrar_dados(dados):
# def ordenar_dados(): - Allana pode terminar 
# def verificar_item():

def menu():
    # menu 
    
    dados = requisicao_API() # recebe tudo da API
    while True:
        print("===== MENU API DE UNIVERSIDADES =====")
        print("1. Listar Dados")
        print("2. Buscar um Item")
        print("3. Detalhes")
        print("4. Filtrar Dados")
        print("5. Ordenar Dados")
        print("6. Verificar Item")
        print("7. Sair")
        
        try:
            opcao = int(input("Sua opção: "))
        
            match opcao:

                case 1:
                    listar_dados(dados)

                case 2:
                    buscar_item(dados)

                case 3:
                    mostrar_detalhes(dados)

                case 7:
                    print("Encerrando sistema...")
                    break

                case _:
                    print("Opção inválida.")
                    
        except ValueError:
            print("Digite apenas números.")
            

menu()