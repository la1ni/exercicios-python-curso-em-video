from datetime import date
ano = date.today().year
menores = 0
maiores = 0
for c in range (0, 7):
    nasc = int(input('Qual o ano em que você nasceu? '))
    if (ano - nasc) < 18:
        menores += 1
    else:
        maiores += 1
print(f'Existem {menores} menores de idade e {maiores} maiores de idade no grupo.')
