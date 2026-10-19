valores = [12, 45, 7, 89, 23]

# Inicialização
menor = valores[0]
maior = valores[0]
indice_menor = 0
indice_maior = 0

# Percurso baseado em índice
for i in range(len(valores)):
    if valores[i] < menor:
        menor = valores[i]
        indice_menor = i

    if valores[i] > maior:
        maior = valores[i]
        indice_maior = i

# Relatório posicional
print("=== RELATÓRIO POSICIONAL ===")

for i in range(len(valores)):
    print(f"Índice: {i} | Posição: {i + 1} | Valor: {valores[i]}")

print("\n=== RESULTADOS ===")
print(f"Menor valor: {menor} (índice {indice_menor}, posição {indice_menor + 1})")
print(f"Maior valor: {maior} (índice {indice_maior}, posição {indice_maior + 1})")