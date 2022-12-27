somaid = 0
mascid = 0
femnova = 0
sn = 'S'
contador = 1
while sn == 'S':
    nome = str(input(f'Nome da {contador}ª pessoa: ')).title().strip()
    idade = int(input(f'Idade da {contador}ª pessoa: '))
    sexo = str(input(f'Sexo da {contador}ª pessoa (M ou F): ')).upper().strip()
    sn = str(input('Você deseja adicionar mais uma pessoa? (S/N): ')).upper()
    print('-----------------------------------------------------')
    somaid += idade
    contador += 1
    if sexo in 'M':
        if idade > mascid:
            mascid = idade
    if mascid == idade:
        homemvelho = nome
    if sexo in 'F':
        if idade < 20:
            femnova += 1
media = somaid/contador
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

