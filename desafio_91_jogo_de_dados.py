from random import randint
from time import sleep
from operator import itemgetter
resultados = dict()
ranking = list()
for c in range(1, 5):
    resultados[f'Jogador {c}'] = randint(1, 6)
for k, v in resultados.items():
    print(f"O {k} tirou {v}")
    sleep(0.5)
ranking = sorted(resultados.items(), key=itemgetter(1), reverse=True)
print("*" * 12, "RANKING DOS JOGADORES", "*" * 12)
for i, k in enumerate(ranking):
    print(f"{i+1}º lugar: {k[0]} com {k[1]} no dado")
    sleep(0.5)



