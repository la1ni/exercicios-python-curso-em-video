n1 = float(input('Qual foi sua nota na primera prova? '))
n2 = float(input('Nota na segunda prova: '))
a = float((n1+n2)/2)
if a < 5:
    print('Reprovado')
elif 5 <= a < 6.9:
    print('Recuperação')
else:
    print('Aprovado')