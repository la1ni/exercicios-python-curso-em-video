def leia_int(msg):
    global letra
    while True:
        try:
            valor = int(input(msg))
        except (KeyboardInterrupt):
            print("\nO usuário preferiu não digitar esse número")
            valor = 0
            break
        except (ValueError, TypeError):
             print(f"\033[0;31mERRO! Digite um número inteiro válido!\033[0m")
        else:
            break
    return valor

def leia_float(msg):
    while True:
        try:
            valor = float(input(msg))
        except (KeyboardInterrupt):
            print("\nO usuário preferiu não digitar esse número")
        except (ValueError, TypeError):
            print(f"\033[0;31mERRO! Digite um número real válido!\033[0m")
        else:
            break
    return valor



n1 = leia_int('Digite um número inteiro: ')
n2 = leia_float('Digite um número real: ')
print(f'Número real: {n2}; Número inteiro: {n1}')
