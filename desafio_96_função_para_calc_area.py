def linha(mensagem):
    print("-" * 40)
    print(mensagem)
    print("-" * 40)


def area(compr, larg):
    a = compr * larg
    print(f"A área do terreno é {a:.2f}m2!")


linha('ÁREA DO TERRENO')

c = float(input("Digite o comprimento do terreno: "))
la = float(input("Digite a largura do terreno: "))
area(c, la)
