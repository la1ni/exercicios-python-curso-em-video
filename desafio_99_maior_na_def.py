from time import sleep


def numeros(* num):
    tam = len(num)
    print(f"Foram passados {tam} valores ao todo:", end=" | ")
    if tam == 0:
        print("De nenhum, o maior é nenhum.")
    else:
        for n in num:
            print(n, end=" | ")
            sleep(0.5)
        print()
        print(f"O maior valor informado foi {max(num)}")


def linhaa():
    print("-" * 50)


linhaa()
numeros(5, 4, 7, 78)
linhaa()
