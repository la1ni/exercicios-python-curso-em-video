from time import sleep
from random import randint
contador = 0
jogos = []
print("-=" * 16, "BEM VINDO AO JOGO DA MEGA SENA", "-=" * 17)
quantos_jogos = int(input("Quantos jogos você quer que eu sorteie? "))
print("-=" * 20, f"Sorteando {quantos_jogos} jogos", "-=" * 20)
for d in range(0, quantos_jogos):
    jogos.append([])
    for c in range(0, 6):
        numero_jogo = (randint(1, 60))
        if numero_jogo not in (jogos[d]):
            (jogos[d]).append(numero_jogo)
        else:
            numero_jogo = (randint(1, 60))
            (jogos[d]).append(numero_jogo)
for sequencia in jogos:
    contador += 1
    sequencia.sort()
    print(f"{contador}º jogo: {sequencia}")
    sleep(0.5)
