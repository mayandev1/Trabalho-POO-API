# 🎓 API de Universidades — Sistema em Python

> Sistema interativo desenvolvido em Python para consumo e manipulação de dados da API pública de universidades.


## 📌 Sobre o Projeto

O projeto foi desenvolvido com foco em praticar:

- Consumo de APIs REST
- Manipulação de JSON
- Estruturas de repetição
- Listas e dicionários
- Programação modular
- Tratamento de exceções
- Organização de código em funções

A aplicação consome dados da API pública:

[API REST](https://universities.hipolabs.com/search?country=Brazil)


# 🚀 Funcionalidades

| Funcionalidade | Status |
|---|---|
| 📋 Listar universidades | ✅ Concluído |
| 🔍 Buscar universidade | ✅ Concluído |
| 🏛️ Mostrar detalhes | ✅ Concluído |
| 🎯 Filtrar dados | ✅ Concluído |
| 🔤 Ordenar dados | ✅ Concluído |
| ✅ Verificar item | ✅ Concluído |
| 📊 Estatísticas | ✅ Concluído |
| 🌐 Consumo de API | ✅ Concluído |
| ⚠️ Tratamento de erros | ✅ Concluído |


# 🛠️ Tecnologias Utilizadas

- Python
- Biblioteca `requests`
- API REST
- JSON


# 📂 Estrutura do Projeto

```bash
universidades-api/
│
├── Universidades.py
└── README.md
````


# ⚙️ Como Executar

## 1️⃣ Instale o Python

[Python Official Website](https://www.python.org?utm_source=chatgpt.com)


## 2️⃣ Instale a biblioteca requests

```bash
pip install requests
```


## 3️⃣ Execute o projeto

```bash
python main.py
```

ou

```bash
py main.py
```

# 🧠 Conceitos Trabalhados

O projeto utiliza diversos conceitos importantes da programação:

* Funções
* Loops
* Condicionais
* List Comprehension
* Dicionários
* Tratamento de Exceções
* Modularização
* Consumo de APIs


# 🌐 Dados Consumidos da API

A API retorna informações como:

* Nome da universidade
* País
* Código do país
* Domínios
* Websites
* Estado/Província

Exemplo de estrutura JSON:

```json
{
  "name": "Universidade Federal do Piauí",
  "country": "Brazil",
  "alpha_two_code": "BR",
  "domains": ["ufpi.br"],
  "web_pages": ["http://www.ufpi.br/"],
  "state-province": null
}
```


# 📸 Exemplo do Sistema

```text
===== MENU API DE UNIVERSIDADES =====

1. Listar Dados
2. Buscar um Item
3. Detalhes
4. Filtrar Dados
5. Ordenar Dados
6. Verificar Item
7. Sair
```


# 👨‍💻 Contributors

| GitHub                                                                  | Nome           |
| ----------------------------------------------------------------------- | -------------- |
| [@mayandev1](https://github.com/mayandev1?utm_source=chatgpt.com)       | Mayan Gabriel  |
| [@AllanaMrtins](https://github.com/AllanaMrtins?utm_source=chatgpt.com) | Allana Martins |


# 📚 Aprendizados

Durante o desenvolvimento do projeto foram praticados:

* Requisições HTTP
* Manipulação de dados externos
* Organização de sistemas em funções
* Tratamento de erros de conexão
* Estruturação de menus interativos


# 🔮 Melhorias Futuras

* Exportar dados para CSV
* Interface gráfica
* Paginação de resultados
* Busca avançada
* Cache local dos dados
* Integração com banco de dados


# 📄 Licença

Este projeto possui finalidade acadêmica e educacional.