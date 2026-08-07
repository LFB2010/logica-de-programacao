# Exercício 1: Caixa de Supermercado
quantidade = int(input("Quantidade de itens: "))
total = 0

for i in range(1, quantidade + 1):
    preco = float(input(f"Preço do item {i}: R$ "))
    total += preco

media = total / quantidade

print(f"\nTotal da compra: R$ {total:.2f}")
print(f"Média por item: R$ {media:.2f}")


# Exercício 2: Tabela de Parcelamento
valor_total = 1200.00

print("\n====================================")
print(f"TABELA DE PARCELAMENTO - COMPRA R$ {valor_total:.2f}")
print("====================================")

for parcelas in range(1, 11):
    valor_parcela = valor_total / parcelas
    print(f"{parcelas}x de R$ {valor_parcela:.2f}")

print("====================================")


# Exercício 3: Monitor de Consumo de Energia
consumo_total = 0
dias_acima_20 = 0

for dia in range(1, 8):
    consumo = float(input(f"Consumo do dia {dia} (kWh): "))
    consumo_total += consumo
    if consumo > 20:
        dias_acima_20 += 1

print(f"\nConsumo total da semana: {consumo_total:.2f} kWh")
print(f"Dias com consumo acima de 20 kWh: {dias_acima_20}")


# Exercício 4: Contagem Regressiva
for segundos in range(15, -1, -1):
    print(segundos)

print("Servidor desligado com segurança.")
