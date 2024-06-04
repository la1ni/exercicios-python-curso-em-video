numero = 0
soma = 0
contador = 0
while True:
    numero = int(input("Digite um número [999 para parar]: "))
    if numero == 999:
        break
    soma += numero
    contador += 1
print(f"A soma dos {contador} números exceto o 999 é {soma}")