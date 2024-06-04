s = 0
cont = 0
for c in range (0,3):
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        #s = s + n (forma alternativa de escrever)
        #cont = cont + 1 (forma alternativa de escrever)
        s += n
        cont += 1
        # em s, está dizendo que se o número n em questão for par, ele será somado ao valor da variável s (antes, 0). Em cont, se diz que se o numero for par, ele será adicionado à contagem de números pares (antes, 0)
print(f'A soma dos números pares é {s} e a quantidade de pares informados é {cont}')
