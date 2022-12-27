import AdivinheWhile
import AdivinheFor
jogo = int(input("Qual jogo você quer jogar?\n1 = adivinhação simples\n2 = adivinhação com pontos\n"))
if jogo == 1:
    AdivinheWhile.jogar()
if jogo == 2:
    AdivinheFor.jogar()