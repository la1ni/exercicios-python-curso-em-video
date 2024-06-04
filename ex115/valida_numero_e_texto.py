def leia_int(msg):
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
