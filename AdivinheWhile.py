from random import randint
def jogar():
    chute = 0
    numero = 0
    while numero != chute or numero == 0:
        numero = randint(1, 5)
        print("Adivinhe um número de 0 a 10)\n**********************")
        chute = int(input(("Digite o número: ")).strip())
        if chute == numero:
            print(f"Você acertou, o número realmente é {numero}")
        else:
            print(f'Tente de novo! O núemro dessa vez era {numero}')
if __name__ == "__main__":
    jogar()
#isso impede que ao importar o arquivo dentro de outro programa ele seja automaticamente executado. Já quando chamado diretamente no prompt, ele irá sim executar
