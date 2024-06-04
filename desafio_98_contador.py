from time import sleep


def contador(inicio, fim, passo):
    if passo == 0:
        print("0 não vai a lugar algum. Vamos usar 1...")
        passo = 1
    if inicio > fim:
        if passo > 0:
            passo = - passo
        while True:
            sleep(1)
            if fim > inicio:
                print("FIM")
                break
            else:
                print(inicio, end=" -> ")
                inicio += passo
    elif fim > inicio:
        if passo < 0:
            passo = -passo
            print("Vamos trocar o sinal do passo ;)")
        while True:
            sleep(1)
            if inicio > fim:
                print("FIM")
                break
            else:
                print(inicio, end=" -> ")
                inicio += passo


def linhaa():
    print("-" * 50)


linhaa()
i = 1
f = 10
p = 1
print(f"Contagem de {i} até {f} com passo {p}")
contador(i, f, p)
linhaa()
i = 10
f = 0
p = 2
print(f"Contagem de {i} até {f} com passo {p}")
contador(i, f, p)
linhaa()
print("Agora é sua vez!")
i = int(input("Defina o início: "))
f = int(input("Defina o fim: "))
p = int(input("Defina o passo: "))
print(f"Contagem de {i} até {f} com passo {p}")
contador(i, f, p)
linhaa()
