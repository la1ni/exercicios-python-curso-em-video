from random import randint
tentativas = 1
r = randint(0, 5)
num = int(input('Adivinhe um número de 0 a 5: '))
while num != r:
    num = int(input('Que pena! Tente novamente: '))
    tentativas += 1
print(f'Parabéns! Você acertou! Só precisou de {tentativas} tentativas.')
