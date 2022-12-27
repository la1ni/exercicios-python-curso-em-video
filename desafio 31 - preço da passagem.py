p = int(input('Qual a distância da viagem? '))
a = p*0.50
b = p*0.45
if p <=200:
    print(f'Sua viagem ficará em R${a:.2f}')
else:
    print(f'Sua viagem então ficará em R${b:.2f}')