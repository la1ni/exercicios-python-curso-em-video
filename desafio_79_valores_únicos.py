valores = []
while True:
    v = int(input("Digite um valor: "))
    if v in valores:
        print("Valor duplicado! Não vou adicionar!")
    else:
        print("Adicionado com sucesso")
        valores.append(v)
    continua = str(input("Deseja continuar [S/N]: ")).upper().strip()
    while continua != "N" and continua != "S":
        continua = str(input("Digite [S ou N]: ")).upper().strip()
    if continua == "N":
        break
print(f"Os valores digitados foram {sorted(valores)}!")
