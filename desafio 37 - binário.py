num = int(input('Digite um número qualquer: '))
base = int(input('Se quer converter para número binário, digite 1. Se quer converter para octal, digite 2. Caso queria um hexadecimal, digite 3: '))
if base == 1 :
    print(bin(num))
elif base == 2 :
    print(oct(num))
elif base == 3 :
    print(hex(num))
else:
    print('Digite uma opção válida, por favor')