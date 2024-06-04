#n = int(input('Digite um número inteiro: '))
#if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0 or n <= 0 :
 #   print(f'O número {n} não é primo')
#else:
#    print(f'O número {n} é primo')
n = int(input('Digite um número inteiro: '))
total = 0
for c in range (1, n+1):
    if n % c == 0:
        print('\033[33m', end= ' ')
        total += 1
    else:
        print('\033[31m', end= ' ')
    print(f'{c}', end= ' ')
if total > 2:
    print(f'\n\033[mO número {n} não é primo, porque foi dividido \033[31m{total} \033[mvezes. Números primos são divididos apenas \033[33m2 \033[mvezes.')
else:
    print(f'\n\033[mO número {n} é primo, porque foi dividido apenas \033[31m{total} \033[mvezes')
