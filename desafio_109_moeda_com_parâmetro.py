from ex109 import moedaex109
from random import randint
n = float(input("Digite um valor: R$"))
print(f"A metade de {n} é {moedaex109.metade(n, True)}")
print(f"O dobro de {n} é {moedaex109.dobro(n, True)}")
taxared = randint(0, 100)
taxaaum = randint(0, 100)
print(f"Reduzindo {taxared}% de {moedaex109.moeda(n)}, o valor que resta é {(moedaex109.reduzir_porcento(n, taxared, True))}")
print(f"Aumentando {taxaaum}% em {moedaex109.moeda(n)}, o valor é {(moedaex109.aumentar_porcento(n, taxaaum, True))}")
