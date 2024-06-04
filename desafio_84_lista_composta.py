dado_temporario = list()
todos_cadastrados = list()
mais_pesados = list()
mais_leves = list()
contador = maximopeso = minimospeso = 0
while True:
    dado_temporario.append(str(input("Nome: ")).capitalize())
    dado_temporario.append(int(input("Peso: ")))
    todos_cadastrados.append(dado_temporario[:])
    contador += 1
    if dado_temporario[1] >= maximopeso:
        maximopeso = dado_temporario[1]
    if contador == 1:
        minimospeso = dado_temporario[1]
    else:
        if dado_temporario[1] <= minimospeso:
            minimospeso = dado_temporario[1]
    dado_temporario.clear()
    deseja_continuar = str(input("Deseja continuar [S/N]? ")).strip().upper()
    while deseja_continuar != "N" and deseja_continuar != "S":
        deseja_continuar = str(input("Digite uma opção válida [S/N]? ")).strip().upper()
    if deseja_continuar == "N":
        break
for c in todos_cadastrados:
    if c[1] == maximopeso:
        mais_pesados.append(c[0])
    if c[1] == minimospeso:
        mais_leves.append(c[0])
print(f"Você digitou os dados de {contador} pessoas.\nO mais pesado tem {maximopeso}Kg e é/são {mais_pesados}\nO mais leve tem {minimospeso}Kg e é/são {mais_leves}")
