n = 1
par = 0
impar = 0
while n != 0:
    n = int(input('Digite um número: '))
    if n == 0:
        par += 0
    elif n % 2 == 0:
        par += 1
    else:
        impar += 1
print(f'Você digitou {par} números pares e {impar} ímpares antes de digitar 0.')