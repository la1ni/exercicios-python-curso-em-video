n1 = int (input('digite um número '))
n2 = int (input('digite outro número agora... '))
s = n1+n2
# print ('considerando que você digitou', n1, 'e', n2, 'posso dizer que a soma deles é', s)
#print ('Considerando que você digitou {} e {}, A soma entre eles é {}'.format(n1, n2, s))
print (f'Considerando que você digitou {n1} e {n2}, A soma entre eles é {s}')

n1 =int(input('Oi! Vamos digitar um número, por favor? '))
n2 =int(input('Agradeço! \nAgora, por gentileza, digite outro número... '))
s = n1 + n2
sub = n1 - n2
m = n1 * n2
d = n1 / n2
p = n1 ** n2
di = n1 // n2
print (f'Hmmm, interessante. A parir desses valores, é possível concluir que a soma deles é {s}, a subtração é {sub}, a multilicação é {m} e a divisão simples é {d:.2f}')
print (f'Já a divisão inteira entre eles é {di} e a potenciação é {p}. Ufa, cansei aqui.')

n1 = float(input('Digite sua nota na primeira prova: '))
n2 = float(input('Digite sua nota na segunda prova agora: '))
m = (n1+n2)/2
print (f'Vish... Quer dizer... Sua média entre as duas provas é {m}')

d = float(input('Quanta grana você tem na carteira? Até os centavos... '))
dol = d/3.27
print (f'Nossa, quanto dinheiro...! Com isso você consegue comprar {dol:.2f} dólares.')

alt = float(input('Qual a altura da parede a ser pintada? '))
larg = float(input('Tá bom, mas e a largura? '))
a = alt * larg
t = a/2
print(f'Ok. A área dessa parede é de mais ou menos {a:.2f}m. Isso quer dizer que você vai precisar de aproximadamente {t:.2f}l de tinta para pintá-la.')

p = float(input('Qual o preço do produto? '))
d = p-(p*0.05)
print(f'O novo preço do produto após aplicados 5% de desconto é de R${d:.2f}.')

s = float(input('Quanto você ganha? '))
a = s + s * 0.15
print(f'Depois do reajuste anual, seu novo salário será de R${a:.2f}!')

