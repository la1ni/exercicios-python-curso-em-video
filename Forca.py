from random import choice
def jogar():
    def mensagemabertura():
        print("*******************************\nBem vindo ao jogo da forca!\n*******************************")

    def palavraDaForca():
        arquivo = open("palavras.txt", "r")
        pal = []
        for linha in arquivo:
            pal.append(linha.strip().upper())
        arquivo.close()
        palavra = choice(pal)
        return palavra

    def vemlista():
        tamanho = len(palavra)
        lista = ["_"] * tamanho
        return lista

    def solicitachance():
        chance = int(input("Quantas chances você quer para o jogador? "))
        while chance < 1:
            chance = int(input("Opa! inválido! Coloque um número  > 0: "))

    def chutecerto(acertos=0):
            index = 0
            for letra in palavra:
                if letra == chute and letra not in lista:
                    lista[index] = letra
                    print(f"{chute} está na palavra!")
                    acertos += 1
                index += 1

    mensagemabertura()
    palavra = palavraDaForca()
    lista = vemlista
    erro = 0
    acertos = 0
    erradas = ["..."]
    solicitachance()
    fim = False
    acertou = False
    while not fim and not acertou:
        print(f"Suas letras corretas são: {lista}")
        chute = str(input("Chute sua letra: ")).strip().upper()
        if chute in palavra:
            chutecerto()
        else:
            erro += 1
            if chute not in erradas:
                erradas.append(chute)
            else:
                erradas = erradas
            print(f"Você errou. Faltam {chance - erro} tentativas. O que você errou ate agora foi: {erradas}")

        fim = erro == chance or chance == 0
        acertou = acertos == tamanho
        if acertou:
            print(f"{lista}")
            print("Parabains! Você acertou!")
        if fim:
            erro = 0
            again = int(input("Enforcado!\nTentar de novo com a mesma palavra [1]\nTentar de novo com outra palavra [2]\nParar [3] "))
            if again == 1:
                erro = 0
                acertos = 0
                chance = int(input("Quantas chances você quer para o jogador? "))
                while chance < 1:
                    chance = int(input("Opa! inválido! Coloque um número  > 0: "))
                lista = ["_"] * tamanho
                tamanho = len(palavra)
                fim = False
                acertou = False
            elif again == 2:
                erro = 0
                acertos = 0
                palavra = palavraDaForca()
                tamanho = len(palavra)
                chance = int(input("Quantas chances você quer para o jogador? "))
                while chance < 1:
                    chance = int(input("Opa! inválido! Coloque um número  > 0: "))
                lista = ["_"] * tamanho
                erradas = ["..."]
                fim = False
                acertou = False
            else:
                print("Ok. Nos vemos depois!")


if __name__ == "__main__":
    jogar()
