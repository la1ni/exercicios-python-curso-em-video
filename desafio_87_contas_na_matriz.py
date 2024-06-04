matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapares = somaterceira = 0
for l in range(0, 3):
    for c in range (0, 3):
        matriz[l][c] = int(input(f"Digite o valor de {l,c}: "))
        if matriz[l][c] % 2 == 0:
            somapares += matriz[l][c]
        if matriz[l][2]:
            somaterceira += matriz[l][2]
print("-=" * 40)
for l in range(0, 3):
    for c in range(0, 3):
        print(f"{matriz[l][c]:^6}", end= " ")
    print()
maxseglinha = max(matriz[1])
print("-=" * 40)
print(f"A soma dos valores pares é {somapares}")
print(f"A soma dos valores da terceira coluna é {somaterceira}")
print(f"O maior número da segunda linha é {maxseglinha}")