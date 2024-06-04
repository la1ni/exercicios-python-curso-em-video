n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
n3 = int(input("Digite um número: "))
n4 = int(input("Digite um número: "))
numeros = (n1, n2, n3, n4)
if 9 in numeros:
    print(f"O valor 9 apareceu {numeros.count(9)} vezes")
else:
    print("O número 9 não apareceu")
if 3 in numeros:
    print(f"O valor 3 apareceu primeiro na posição {numeros.index(3) + 1}")
else:
    print("O número 3 não apareceu")
print("Os números pares digitados foram:", end= " ")
for c in numeros:
    if c % 2 == 0:
        print(c, end= " ")

