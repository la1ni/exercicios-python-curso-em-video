from datetime import date
ano = date.today().year
nasc = int(input('Em qual ano o atleta nasceu? '))
idade = ano - nasc
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JÚNIOR')
elif idade <= 20:
    print('SÊNIOR')
else:
    print('MASTER')


