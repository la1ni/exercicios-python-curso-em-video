frase = str(input('Digite uma frase: ')).strip().upper()
corte = frase.split()
semesp = ''.join(corte)
contrario = ''
for letra in range (len(semesp) -1, -1, -1):
    contrario += semesp[letra]
print(f'Você digitou a frase {frase}, que ao contrário fica {contrario}')
if semesp == contrario:
    print('A frase é um palíndromo!')
else:
    print('Sem palíndromos por aqui...')