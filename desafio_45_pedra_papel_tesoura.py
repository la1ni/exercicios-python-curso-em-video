import emoji
from random import randint
print('BEM VINDO AO PEDRA PAPEL TESOURA!')
escolha = int(input(emoji.emojize(':mountain: digite 1\n:page_facing_up:    digite 2\n:scissors: digite 3 ')))
pc = randint(1, 3)
if pc == 1:
    print(emoji.emojize('O PC escolheu :mountain:'))
elif pc == 2:
    print(emoji.emojize('O PC escolheu :page_facing_up:'))
else:
    print(emoji.emojize('O pc escolheu :scissors:'))
if escolha == pc:
    print('EMPATE!')
elif escolha == 1 and pc == 2 or escolha == 2 and pc == 3 or escolha == 3 and pc == 1:
    if pc == 1:
        print(emoji.emojize(':mountain: esmaga :scissors:'))
    elif pc == 2:
        print(emoji.emojize(':page_facing_up: sufoca :mountain:'))
    else:
        print(emoji.emojize(':scissors: corta :page_facing_up:'))
    print('O PC ganhou')
else:
    if escolha == 1:
        print(emoji.emojize(':mountain: esmaga :scissors:'))
    elif escolha == 2:
        print(emoji.emojize(':page_facing_up: sufoca :mountain:'))
    else:
        print(':scissors: corta :page_facing_up:')
    print('Você venceu!')



