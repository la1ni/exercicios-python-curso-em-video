vel = int(input('Digite a velocidade do carro na estrada: '))
b = 7*(vel-80)
if vel <= 80 :
    print('Andando na velocidade correta... não fez mais que a obrigação')
else:
    print(f'Pelo visto, você terá que pagar um valor de R${b},00 de multa por ultrapassar a velocidade permitida.')