lista_geral = []
lista_pares = []
lista_impares = []
while True:
    valor_digitado = int(input("Digite um valor: "))
    lista_geral.append(valor_digitado)
    continua = str(input("Deseja continuar? [S/N] ")).strip()
    while continua not in "Nn" and continua not in "Ss":
        continua = str(input("Por favor responda [S/N]: ")).strip()
    if continua in "Nn":
        break
for item in lista_geral:
    if item % 2 == 0:
        lista_pares.append(item)
    else:
        lista_impares.append(item)
print(f"Os números digitados foram {lista_geral}")
print(f"Os números pares foram {lista_pares}")
print(f"Os números ímpares foram {lista_impares}")