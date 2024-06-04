lista_de_palavras = ("rosa", "queijo", "marido", "sorridente", "latinha", "carro", "banana", "filiado", "curadoria")
print("-" * 40)
print("Mostrador de vogais")
print("-" * 40, end= " ")
for palavra in lista_de_palavras:
    palavra = palavra.upper()
    print(f"\n A palavra {palavra} tem as vogais", end= " ")
    for letra in palavra:
        if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
            print(f"{letra}", end= " ")


