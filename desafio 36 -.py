a = float(input('Qual o valor da casa?'))
b = float(input('Qul o seu salário?'))
c = float(input('Em quantos anos você vai pagar a cas?'))
d = a/(c*12)
print (f'A prestação ficará em {d}')
if (d) >= 0.3*b :
    print('Seu empréstimo vai ser negado...')
else:
    print('Você vai conseguir o empréstimo')