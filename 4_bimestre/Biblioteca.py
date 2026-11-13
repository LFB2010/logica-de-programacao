
# ==========================================
# SISTEMA DE GESTÃO DE BIBLIOTECA
# ==========================================

# PARTE 1 - Modelagem e carga inicial

acervo = [
    {
        "codigo": 101,
        "titulo": "Dom Casmurro",
        "autor": "Machado de Assis",
        "paginas": 256,
        "disponivel": True
    },
    {
        "codigo": 102,
        "titulo": "O Pequeno Príncipe",
        "autor": "Antoine de Saint-Exupéry",
        "paginas": 96,
        "disponivel": True
    },
    {
        "codigo": 103,
        "titulo": "Harry Potter",
        "autor": "J.K. Rowling",
        "paginas": 350,
        "disponivel": False
    },
    {
        "codigo": 104,
        "titulo": "A Culpa é das Estrelas",
        "autor": "John Green",
        "paginas": 288,
        "disponivel": True
    }
]

# PARTE 2 - Cadastro dinâmico

novo_livro = {
    "codigo": 105,
    "titulo": "O Hobbit",
    "autor": "J.R.R. Tolkien",
    "paginas": 310,
    "disponivel": True
}

acervo.append(novo_livro)

# PARTE 3 - Filtragem de livros

print("\n--- LIVROS DISPONÍVEIS COM MAIS DE 250 PÁGINAS ---")

for livro in acervo:
    if livro["disponivel"] == True and livro["paginas"] > 250:
        print("Título:", livro["titulo"])
        print("Autor:", livro["autor"])
        print("----------------------")

# PARTE 4 - Busca pelo código 104

encontrado = False

for livro in acervo:
    if livro["codigo"] == 104:
        encontrado = True

        print("\n--- LIVRO LOCALIZADO ---")
        print("Título:", livro["titulo"])

        if livro["disponivel"] == True:
            print("Situação: Disponível")
        else:
            print("Situação: Emprestado")

        break

if encontrado == False:
    print("Código 104 não localizado no acervo.")

# DESAFIO EXTRA - Empréstimo de livro

codigo_busca = int(input("\nDigite o código do livro para empréstimo: "))

encontrado = False

for livro in acervo:
    if livro["codigo"] == codigo_busca:
        encontrado = True

        if livro["disponivel"] == True:
            livro["disponivel"] = False
            print("Empréstimo realizado com sucesso!")
            print("Livro:", livro["titulo"])
        else:
            print("Este livro está indisponível para empréstimo.")

        break

if encontrado == False:
    print("Livro não encontrado no acervo.")
