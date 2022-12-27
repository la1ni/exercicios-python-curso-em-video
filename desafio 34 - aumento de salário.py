sal = float(input('Qual o seu salário? '))
a = sal + (sal*0.1)
b = sal + (sal*0.15)
if sal > 1250:
    print(f'Seu novo salário é de {a:.2f}')
else:
    print(f'Seu novo salário é de {b:.2f}')