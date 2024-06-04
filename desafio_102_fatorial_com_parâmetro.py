def fatorial(num, show=False):
    """
    -> Calcula a fatorial de um número
    :param num: número que será alvo de fatorial
    :param show: se verdadeiro, o processo de multiplicação será exibido. se falso, não
    :return: resultado da fatorial
    """
    for c in range(num-1, 0, -1):
        if show:
            print(f"{c}", end=" ")
            if c != 1 :
                print("x ", end="")
            elif c == 1:
                print("= ", end="")
        num *= c
    return num


resultado = fatorial(6)
print(resultado)
print(help(fatorial))
