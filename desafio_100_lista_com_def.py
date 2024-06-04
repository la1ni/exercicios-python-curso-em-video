from random import randint
from time import sleep


def sorteio(lista):
    print("Sorteando 5 valores da lista:", end=" ")
    for c in range(0, 5):
        s = randint(0, 10)
        lista.append(s)
        print(s, end=" ")
        sleep(0.3)
    print()


def somapar(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    print(f"A soma dos pares na lista é {soma}")


numeros = list()
sorteio(numeros)
somapar(numeros)
