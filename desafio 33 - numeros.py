

n1 = int(input('\33[0;30;107mDigite um número: \33[m'))
n2 = int(input('Digite outro número: '))
n3 = int(input('Mais um número, por favor: '))

if (n1 > n2) & (n1 > n3) :
    print(f'O maior número é \33[30m{n1}\33[m')
elif (n2 > n1) & (n2 > n3) :
    print(f'O maior número é {n2}')
elif (n3 > n1) & (n3 > n2) :
    print(f'O maior número é {n3}')
if (n1 < n2) & (n1 < n3) :
    print(f'O menor número é {n1}')
elif (n2 < n1) & (n2 < n3) :
    print(f'O menor número é {n2}')
elif (n3 < n1) & (n3 < n2) :
    print(f'O menor número é {n3}')

