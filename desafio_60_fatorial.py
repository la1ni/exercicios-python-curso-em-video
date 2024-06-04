import math
numero = int(input("Digite um número inteiro para calcular sua fatorial: "))
fatorial = math.factorial(numero)
menos_um = numero
while (menos_um > 0):
    print(menos_um, end = " ")
    if menos_um > 1:
        print(" * ", end = " ")
    menos_um -= 1
print(f" =  {fatorial}")