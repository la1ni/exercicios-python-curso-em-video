primeiro_termo = int(input("Qual será o primeiro termo da PA? "))
razao = int(input("Qual a razão da PA? "))
c = 0
b = 10
mais = 0
while c != b:
    print(primeiro_termo, end=" ")
    primeiro_termo += razao
    c += 1
    if c == b:
        print("-> PAUSA")
        mais = int(input("Você deseja ver mais quantos termos da PA? "))
        b += mais
        if mais == 0:
            print("FIM")
