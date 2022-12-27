#def comandos():
from random import choice
arquivo = open("palavras.txt", "r")
pal = []
for linha in arquivo:
    pal.append(linha.strip().upper())
arquivo.close()
palavra = choice(pal)
tamanho = len(palavra)
erro = 0
acertos = 0
chance = int(input("Quantas chances você quer para o jogador? "))
while chance < 1:
    chance = int(input("Opa! inválido! Coloque um número  > 0: "))
lista = ["_"] * tamanho
erradas = ["..."]
fim = False
acertou = False

  #  if __name__ == "__main__":
        #comandos()