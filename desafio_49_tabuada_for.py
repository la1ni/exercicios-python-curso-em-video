n = int(input('Digite um número: '))
print(f'A tabuada de {n} é:')
for c in range (n, 10*n+1, n):
    print(c, end=" ")