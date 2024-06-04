nome = str(input('Digite seu nome completo: '))
upper = nome.upper()
split = upper.split()
a = 'SILVA' in split
if a >= True:
    print('Você tem Silva no nome hihihi')
else:
    print('Uau, diferentão sem Silva no nome...')