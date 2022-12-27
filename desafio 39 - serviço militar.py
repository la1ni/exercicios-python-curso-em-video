import datetime
a = datetime.datetime.now()
b = a.date()
ano = b.strftime("%Y")
anoo = int(ano)
nasc = int(input('Em que ano você nasceu? '))
c = anoo - nasc
d = 18 - c
e = c - 18
if c < 18:
    print(f'Ainda não é hora de você se alistar. Faltam {d} anos.')
elif c > 18:
    print(f'Já passou da hpra de você se alistar... Deveria ter se alistado há {e} anos.')
else:
    print('Já está na hora de você se alistar!')
