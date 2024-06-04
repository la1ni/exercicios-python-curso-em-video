total = 0
barato = 0
contador = 1
mais_de_mil = 0
mais_barato = ""
print("Vamos às compras!")
while True:
    nome_do_produto = str(input(f"Qual o nome do {contador}º produto? ")).upper().strip()
    preco = float(input(f"Qual o valor do {contador}º produto? "))
    total += preco
    if contador == 1:
        barato = preco
    if barato >= preco:
        barato = preco
        mais_barato = nome_do_produto
    if preco > 1000:
        mais_de_mil += 1
    continua = str(input("Deseja continuar? [S/N] ")).upper().strip()
    contador += 1
    if continua == "N":
        break
print(f"O valor total da sua compra é {total:.2f}. {mais_de_mil} produtos custam mais de R$1000 e o item mais barato "
      f"de todos é {mais_barato}, que custa R${barato:.2f}")
