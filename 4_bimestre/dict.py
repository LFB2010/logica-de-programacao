produto = {
    "codigo": 101,
    "nome": "Teclado Mecânico Gayter",
    "preco": 250.0,
    "estoque": 14
}

print("=== PRODUTO CADASTRADO ===")
print(produto)

print("Nome do produto:", produto["nome"])
print("Preço do produto: R$", produto["preco"]) 
print("-"*20)

produto["preco"] = 220.0
produto["estoque"] = produto["estoque"] + 6
produto["categoria"] = "Periféricos"

print("=== PRODUTO ATUALIZADO ===")
print(produto)
print(f"Novo Estoque Total {produto['estoque']} Unidades")
print("-"*20)

usuario = {
    "nome": "Carlos Eduardo",
    "nivel": "Administrador",
    "ativo": True
}
print("=== USUÁRIO ===")
print("\nChaves do usuário:")
print(usuario.keys())
print("\nValores do usuário:")
print(usuario.values())
print("-"*20)