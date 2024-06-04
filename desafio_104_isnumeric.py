def leia_int(numero):
    ok = False
    valor = 0
    while True:
        num = str(input(numero))
        if num.isnumeric():
            valor = int(num)
            ok = True
        else:
            print("Digite um NÚMERO INTEIRO...")
        if ok:
            break
    return valor


numero = leia_int("Digite um número: ")
print(f"Você digitou o número {numero}!")
