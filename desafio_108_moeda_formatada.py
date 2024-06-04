from ex107 import moeda
from random import randint
n = float(input("Digite um valor: R$"))
print(f"A metade de {n} é {moeda.moeda(moeda.metade(n))}")
print(f"O dobro de {n} é {moeda.moeda(moeda.dobro(n))}")
taxared = randint(0, 100)
taxaaum = randint(0, 100)
print(f"Reduzindo {taxared}% de {moeda.moeda(n)}, o valor que resta é {moeda.moeda(moeda.reduzir_porcento(n, taxared))}")
print(f"Aumentando {taxaaum}% em {moeda.moeda(n)}, o valor é {moeda.moeda(moeda.aumentar_porcento(n, taxaaum))}")
