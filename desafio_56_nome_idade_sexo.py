somaid = 0
mascid = 0
femnova = 0
n = 0
for d in range (1, 3):
    nome = str(input(f'Nome da {d}ª pessoa: ')).title().strip()
    idade = int(input(f'Idade da {d}ª pessoa: '))
    sexo = str(input(f'Sexo da {d}ª pessoa (M ou F): ')).upper().strip()
    sn = str(input('Você deseja adicionar mais uma pessoa? (S/N)')).upper()
    print('-----------------------------------------------------')
    somaid += idade
    if sexo in 'M':
        if idade > mascid:
            mascid = idade
    if mascid == idade:
        homemvelho = nome
    if sexo in 'F':
        if idade < 20:
            femnova += 1
    if d == 2:
        print(f'Você chegou ao limite, que é de {d} pessoas')
media = somaid/d
if femnova > 1:
    mulheres = ('es tem menos de 20 anos')
elif femnova == 1:
    mulheres = (' tem menos de 20 anos')
elif femnova < 1:
    mulheres = ('es tem menos de 20 anos')
if mascid == 0 :
    homemvelho = ('não tem nome, pois ele não existe')
    mulheres = ('es com menos de 20 anos')
print( f'A média das idades das pessoas é {media:.2f}. O homem mais velho do grupo se chama {homemvelho}, com seus {mascid} anos. Além disso, {femnova} mulher{mulheres}')

