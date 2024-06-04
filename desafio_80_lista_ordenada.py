valores = []
for c in range(1, 8):
    numero = int(input("Digite um valor: "))
    if c == 1:
        valores.append(numero)
        print("Valor adicionado com sucesso!")
    else:
        if numero >= max(valores):
            valores.append(numero)
            print("Valor adicionado na última posição da lista")
        elif numero <= min(valores):
            valores.insert(0, numero)
            print("Valor adicionado na primeira posição da lista")
        if min(valores) < numero < max(valores):
            for pos, valor in enumerate(valores):
                if numero < valor:
                    valores.insert(pos, numero)
                    print(f"Valor adicionado na posição {pos} da lista!")
                    break
        print(valores)
print(f"A lista em ordem é {valores}")
