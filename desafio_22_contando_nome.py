nome = str(input('Qual o seu nome completo? '))
upper = nome.upper()
lower = nome.lower()
count = len(nome) - nome.count(' ')
split = len(nome.split()[1])

print(f'Seu nome maiúsculo é {upper}\nJá minúsculo, fica {lower}\nA contagem de todas as letras do seu nome é {count}\nE só as do primeiro nome são {split}')
