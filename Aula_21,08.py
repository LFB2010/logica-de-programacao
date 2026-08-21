dados_brutos = [
    " JOAO.SILVA@ESCOLA.COM ",
    " 000.111.222-33 ",
    " Rua das Flores, No 123 ",
    " MARIA.SOUZA@EMAIL.COM ",
    " 123.456.789-00 ",
    " Avenida Brasil, No 456 "
]

dados_limpos = []

for item in dados_brutos:
    # 1. Remover espaços do início e do fim
    item = item.strip()

    # 2. Padronizar e-mails para letras minúsculas
    if "@" in item:
        item = item.lower()

    # 3. Substituir "No" por "Número"
    if "No" in item:
        item = item.replace("No", "Número")

    # 4. Limpar CPF formatado
    if "." in item and "-" in item:
        item = item.replace(".", "").replace("-", "")

    # 5. Adicionar o item limpo à nova lista
    dados_limpos.append(item)

print("Dados limpos:")
for dado in dados_limpos:
    print(dado)
