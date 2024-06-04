numero = 0
while True:
    print("********************************************************")
    numero = int(input("Digite um número positivo para ver sua tabuada: "))
    if numero == 0:
        print("0 não tem tabuada!")
    if numero <= 0:
        break
    print("********************************************************")
    for c in range (1, 11):
        print(numero, "x", c, " = ", numero * c)
