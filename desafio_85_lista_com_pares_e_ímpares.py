todos_numeros = [[], []]
for n in range(1, 8):
    numero = (int(input("Digite um valor: ")))
    if numero % 2 == 0:
        todos_numeros[0].append(numero)
    else:
        todos_numeros[1].append(numero)
print("-=" * 40)
print(f"Os números pares digitados foram {sorted(todos_numeros[0])}")
print(f"Os números ímpares digitados foram {sorted(todos_numeros[1])}")
