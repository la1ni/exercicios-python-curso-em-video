from random import randint
print("********************************************************")
print("Bem vindos ao jogo de par ou ímpar com números de 0 a 10!")
print("********************************************************")
numero_do_pc = randint(1, 11)
soma = 0
venceu = False
perdeu = False
contador = 0
while True:
    numero = int(input("Digite seu número: "))
    while numero < 0 or numero > 10:
        print("Inválido. Jogue nas regras, não seja o Rigby.")
        numero = int(input("Digite seu número: "))
    par_ou_impar = str(input("Par ou Ímpar? [P/I] ")).upper().strip()
    while par_ou_impar != "P" and par_ou_impar != "I":
        print("Inválido!")
        par_ou_impar = str(input("Par ou Ímpar? [P/I] ")).upper().strip()
    soma = numero_do_pc + numero
    print("-------------------------------------------------------------------------------")
    print(f"Você jogou {numero} e o pc jogou {numero_do_pc}. A soma foi igual a {soma}")
    if soma % 2 == 0:
        if par_ou_impar == "P":
            print("Resultado par! Você venceu!")
            venceu = True
        elif par_ou_impar == "I":
            print("Resultado par! Você perdeu!")
            perdeu = True
    else:
        if par_ou_impar == "I":
            print("Resultado ímpar! Você venceu!")
            venceu = True
        elif par_ou_impar == "P":
            print("Resultado ímpar! Você perdeu!")
            perdeu = True
    contador += 1
    print("-------------------------------------------------------------------------------")
    if perdeu == True:
        break
    if venceu == True:
        print("Vamos jogar de novo?")
print(f"Você obteve {contador} vitórias!")
