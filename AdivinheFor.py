from random import randint
def jogar():
    chute = 0
    numero = 0
    tentativas = 0
    qual = 1
    pontos = 10
    numero = randint(1, 11)
    nivel = int(input(f"Vamos jogar! Você começa com {pontos}pts Escolha um nível de dificuldade de 1 a 3! "))
    for c in range (1, nivel+1):
        print(f"**********************\n{qual}ª tentativa\nAdivinhe um número de 0 a 10\n**********************")
        chute = int(input(("Digite o número: ")).strip())
        qual += 1
        if chute < 0 or chute >= 11:
            print(f"Núemro não está no intervalo... Você perdeu essa tentativa e ainda perdeu os pontos...")
        if chute != numero:
            pontos = pontos - abs(numero - chute)
            if qual != nivel + 1:
                print(f'Tente de novo!')
            elif qual == nivel + 1:
                print(f"Não foi dessa vez... O núemro era {numero} e você fez {pontos} pontos")
        if chute == numero:
                    print(f"Você acertou, o número realmente é {numero} e você fez {pontos} pontos")
                    break
if __name__ == "__main__":
    jogar()
#isso impede que ao importar o arquivo dentro de outro programa ele seja automaticamente executado. Já quando chamado diretamente no prompt, ele irá sim executar



