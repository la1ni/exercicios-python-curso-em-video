c = ('\033[m',  #  0 vazio
     '\033[0;30;42m',  #  1 pt f vd
     '\033[0;32;40m',  #  2 azul
     '\033[0;30;44m'  # 3
     )


def manual():
    def escreva(mensagem, cor=0):
        print(c[cor], end="")
        print("~" * len(mensagem))
        print(f"{mensagem}")
        print("~" * len(mensagem))
        print(c[0], end="")

    escreva("Bem vindo ao pyHelp!", 1)
    while True:
        a = str(input("Deseja conhecer qual função ou biblioteca? [FIM] para sair: "))
        if a == "FIM" or a == "fim":
            escreva("Atém mais!", 3)
            break
        else:
            escreva(f"Acessando o manual do comando '{a}'", 2)
            print(help(a))


manual()
