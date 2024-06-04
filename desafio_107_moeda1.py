from ex107 import moeda
from random import randint
n = float(input("Digite um valor: R$"))
print(f"A metade de {n} é R${moeda.metade(n):.2f}")
print(f"O dobro de {n} é R${moeda.dobro(n):.2f}")
taxared = randint(0, 100)
taxaaum = randint(0, 100)
print(f"Reduzindo {taxared}% de {n}, o valor que resta é R${moeda.reduzir_porcento(n, taxared):.2f}")
print(f"Aumentando {taxaaum}% em {n}, o valor é R${moeda.aumentar_porcento(n, taxaaum):.2f}")
