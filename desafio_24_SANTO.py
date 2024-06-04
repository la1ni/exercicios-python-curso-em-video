c = str(input('Digite o nome de uma cidade: '))
s = c.split()
a = (s[0])
b = a.upper()
if b >= 'SANTO':
    print('Parece que estamos falando de uma cidade com nome de santo...')
else:
    print('Uma cidade sem nome de santo...')