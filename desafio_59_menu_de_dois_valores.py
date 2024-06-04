soma = 0
multiplica = 1
opção = 0
a = 0
b = 0
c = 0
d = 0
while opção == 0:
    c += 1
    d += 1
    print(f'--------- {d}º valor ---------')
    n1 = int(input('Digite um número: '))
    soma += n1
    multiplica = multiplica * n1
    if c == 1:
        a = n1
    if c == 2:
        b = n1
    if c == 2:
        opção = int(input('--- MENU ---\n1 -> soma os números\n2 -> multiplica os números\n3 -> descobre o maior para você\n4 -> quero mudar meus números\n5 ou qualquer outro número -> tchau!\nDigite aqui: '))
    if opção == 1:
        print(f'A soma dos números inseridos é {soma}')
    elif opção == 2:
        print(f'O produto dos números inseridos é {multiplica}')
    elif opção == 3:
        if a > b:
            print('O primeiro número é maior que o segundo')
        elif a == b:
            print('Os números são iguais.')
        else:
            print('O segundo número é maior que o primeiro.')
    elif opção == 4:
        opção = 0
        d = 0
        c = 0
        soma = 0
        multiplica = 1
    elif opção > 4:
        print('Tchau!')




