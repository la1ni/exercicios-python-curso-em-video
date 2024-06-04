grad = 0
b = 's'
soma = 0
gradd = grad + 1
while b != 'N':
    a = int(input(f'Digite a {gradd}ª nota do aluno: '))
    b = input('Deseja digitar mais uma? (s/n) ').upper()
    soma += a
    grad += 1
    gradd += 1
media = soma/grad
print(f'A média das notas do aluno é {media}')


