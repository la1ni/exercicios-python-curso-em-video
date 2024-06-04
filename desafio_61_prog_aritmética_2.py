primeiro_termo = int(input("Qual será o primeiro termo da PA? "))
razao = int(input("Qual a razão da PA? "))
c = 0
print("*****************************")
while c < 10:
    print(primeiro_termo, end=" ")
    primeiro_termo += razao
    c += 1
    if c == 10: print ("-> Fim")
print("\n*****************************")
