s = str(input('Digite seu sexo (M/F): ')).upper().strip()
while s != 'M' and s != 'F':
    print('Digite novamente...')
    s = str(input('Digite seu sexo (M/F): ')).upper()
if s == 'F':
    s = 'feminino'
else:
    s = 'masculino'
print(f'Então seu sexo é {s}')
print('FIM')
