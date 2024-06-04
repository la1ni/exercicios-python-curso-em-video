valores = []
pmax = []
pmin = []
for c in range(1, 6):
    valor_digitado = int(input(f"Digite um {c}º valor: "))
    valores.append(valor_digitado)
for pos, v in enumerate (valores):
    if max(valores) == v:
        pmax.append(pos)
    if min(valores) == v:
        pmin.append(pos)
print(f"Você digitou os valores {valores}")
print(f"O maior valor digitado foi {max(valores)}, nas posições {pmax}")
print(f"O menor valor digitado foi {min(valores)}, nas posições {pmin}")
