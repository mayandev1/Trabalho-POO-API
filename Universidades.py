import requests

url = "http://universities.hipolabs.com/search?country=Brazil"


# faz a requisição para a API
def requisicao_API():

    try:

        resposta = requests.get(url, timeout=10)

        if resposta.status_code == 200:
            return resposta.json()

        else:
            print(f"Erro ao acessar API. Status Code: {resposta.status_code}")
            return []

    except requests.exceptions.RequestException as erro:
        print(f"Erro de conexão: {erro}")
        return []


# lista universidades da API
def listar_dados(dados):

    if not dados:
        print("\nNenhum dado disponível.\n")
        return

    print("\n===== LISTA DE UNIVERSIDADES =====\n")

    for i, universidade in enumerate(dados[:20], start=1):

        print(f"{i}. {universidade['name']}")

    print()


# busca universidades pelo nome
def buscar_item(dados):

    if not dados:
        print("\nNenhum dado carregado da API.\n")
        return

    nome = input("\nDigite o nome da universidade: ").strip().lower()

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


# mostra detalhes completos da universidade
def mostrar_detalhes(dados):

    if not dados:
        print("\nNenhum dado carregado da API.\n")
        return

    nome = input("\nDigite o nome da universidade: ").strip().lower()

    for universidade in dados:

        if nome in universidade["name"].lower():

            print("\n===== DETALHES =====\n")

            print("Nome:", universidade.get("name"))
            print("País:", universidade.get("country"))
            print("Código:", universidade.get("alpha_two_code"))
            print("Domínio:", universidade.get("domains", ["Sem domínio"])[0])
            print("Site:", universidade.get("web_pages", ["Sem páginas web"])[0])
            print("Estado:", universidade.get("state-province", "Não informado"))

            return

    print("Universidade não encontrada.")


# filtra universidades por nome, país ou estado
def filtrar_dados(dados):

    if not dados:
        print("\nNenhum dado carregado da API.\n")
        return

    termo = input("\nDigite o nome, estado ou país: ").strip().lower()

    filtrados = [
        u for u in dados
        if termo in u.get("name", "").lower()
        or termo in u.get("country", "").lower()
        or termo in str(u.get("state-province", "")).lower()
    ]

    print("\n===== RESULTADO DO FILTRO =====\n")

    if filtrados:

        for u in filtrados:
            print(u["name"])

    else:
        print("Nenhuma universidade encontrada.")


# ordena universidades em ordem alfabética
def ordenar_dados(dados):

    if not dados:
        print("\nNenhum dado carregado da API.\n")
        return

    ordenados = sorted(dados, key=lambda u: u["name"].lower())

    print("\n===== UNIVERSIDADES ORDENADAS (A - Z) =====\n")

    for u in ordenados[:30]:
        print(u["name"])


# verifica se a universidade existe
def verificar_item(dados):

    if not dados:
        print("\nNenhum dado carregado da API.\n")
        return

    nome = input("\nDigite o nome da universidade: ").strip().lower()

    existe = any(
        nome in u.get("name", "").lower()
        or nome in u.get("country", "").lower()
        or nome in str(u.get("state-province", "")).lower()
        for u in dados
    )

    print("\n===== VERIFICAÇÃO =====\n")

    if existe:
        print("A universidade existe na base de dados.")

    else:
        print("Universidade não encontrada.")


# mostra estatísticas gerais da API
def estatisticas(dados):

    if not dados:
        print("\nNenhum dado carregado da API.\n")
        return

    print("\n===== ESTATÍSTICAS =====\n")

    # total de universidades
    total = len(dados)

    # universidades com estado definido
    com_estado = sum(
        1 for u in dados
        if u.get("state-province")
    )

    # universidades sem estado definido
    sem_estado = total - com_estado

    # universidades com domínio .br
    dominios_br = sum(
        1 for u in dados
        if ".br" in u.get("domains", [""])[0]
    )

    print(f"Total de universidades: {total}")
    print(f"Com estado definido: {com_estado}")
    print(f"Sem estado definido: {sem_estado}")
    print(f"Domínios '.br': {dominios_br}")


# menu principal do sistema
def menu():

    dados = requisicao_API()

    while True:

        print("\n===== MENU API DE UNIVERSIDADES =====")
        print("1. Listar Dados")
        print("2. Buscar um Item")
        print("3. Detalhes")
        print("4. Filtrar Dados")
        print("5. Ordenar Dados")
        print("6. Verificar Item")
        print("7. Estatísticas")
        print("8. Sair")

        try:

            opcao = int(input("Sua opção: "))

            match opcao:

                case 1:
                    listar_dados(dados)

                case 2:
                    buscar_item(dados)

                case 3:
                    mostrar_detalhes(dados)

                case 4:
                    filtrar_dados(dados)

                case 5:
                    ordenar_dados(dados)

                case 6:
                    verificar_item(dados)

                case 7:
                    estatisticas(dados)

                case 8:
                    print("Encerrando sistema...")
                    break

                case _:
                    print("Opção inválida.")

        except ValueError:
            print("Digite apenas números.")


menu()