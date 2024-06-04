
import valida_numero_e_texto


def insere_no_arquivo():
    try:
        open("pessoas.txt", "a")
    except FileNotFoundError:
        print("Criando arquivo...")
        arquivo = open("pessoas.txt", "w")
        nome = (str(input("Digite o nome da pessoa: ")))
        idade = valida_numero_e_texto.leia_int("Digite a idade: ")
        arquivo.writelines(f"{nome}\n")
        arquivo.writelines(f"{idade}\n")
        arquivo.close()
    else:
        arquivo = open("pessoas.txt", "a")
        nome = (str(input("Digite o nome da pessoa: ")))
        idade = valida_numero_e_texto.leia_int("Digite a idade: ")
        arquivo.writelines(f"{nome}\n")
        arquivo.writelines(f"{idade}\n")
        arquivo.close()


def texto_central(texto):
    print("-" * 50)
    print(f'{texto:^50}')
    print("-" * 50)


def menu():
    lista = []
    mostra_menu = True
    escolha = 0
    while mostra_menu:
        texto_central('MENU INICIAL')
        print('1- Ver pessoas cadastradas\n2- Cadastrar nova pessoa\n3- Sair do Programa')
        print("-" * 50)
        try:
            escolha = int(input('Sua opção: '))
        except (ValueError, TypeError, KeyboardInterrupt):
            print(f"\033[0;31mERRO! Digite uma opção válida!\033[0m")
        else:
            if escolha == 1:
                try:
                    arquivo = open("pessoas.txt", "r")
                except FileNotFoundError:
                    print("Ainda não temos ninguém cadastrado!")
                    break
                else:
                    for linha in arquivo:
                        lista.append(linha.replace("\n", ""))
                    texto_central('LISTA DE PESSOAS')
                    for pos in range(0, len(lista)):
                        if pos % 2 == 0:
                            print(f'{lista[pos]:<15}', end=" ")
                        else:
                            print(f'\t{lista[pos]:>25} anos')
                    lista.clear()
                    arquivo.close()
            if escolha == 2:
                insere_no_arquivo()
            if escolha == 3:
                print('Até logo!')
                break
            if escolha not in range(1, 4):
                print("Digite uma opção válida ")
    print("-" * 50)


menu()
