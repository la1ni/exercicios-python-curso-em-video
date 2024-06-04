
def leia_dinheiro(frase):
    valor = input(frase)
    cont_carac = 0
    erro = False
    while True:
        valor = str(valor)
        valor = valor.replace(",", ".")
        if valor.strip() == '':
            erro = True
        for carac in valor.strip():
            if carac.isnumeric() == False and carac != ".":
                erro = True
            if carac == ".":
                cont_carac += 1
            if cont_carac >= 2:
                erro = True
                cont_carac = 0
        if erro:
            print(f"\033[0;31mERRO! '{valor.strip()}' é inválido!\033[0m")
            valor = input(frase)
            erro = False
        else:
            break
    return float(valor)
