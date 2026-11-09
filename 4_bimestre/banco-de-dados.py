#Atividade 1: Cadastro de alunos
cadastros = [
    {"nome": "Luis Fernando",
     "idade": "16",
     "curso": "TI"
    },

    {"nome": "jhony",
     "idade": "15",
     "curso": "TI"
    },
]

novo_aluno = [
    {"nome": "Kevin",
     "idade": " 17",
     "curso": "TI"
    }
]

cadastros.append(novo_aluno)

print("=== LISTA DE ALUNOS ===")

for aluno in cadastros:
    print("----------------------")
    print("Nome:", aluno["nome"])
    print("Idade:", aluno["idade"])
    print("Curso:", aluno["curso"])

#Atividade 2: Cadastro de produtos

catalogo = [
    {"produto": "Notebook", 
    "preco": 3500.00, 
    "em_estoque": True},
    
    {"produto": "Mouse", 
    "preco": 50.00, 
    "em_estoque": True}
]

print("=== CATÁLOGO DE PRODUTOS ===")

for item in catalogo:
    print("----------------------")
    print("Produto:", item["produto"])
    print(f"Preço: R$ {item['preco']:.2f}")