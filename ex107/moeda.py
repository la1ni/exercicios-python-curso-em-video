
def aumentar_porcento(num, taxa):
    valor = num + (taxa/100*num)
    return valor


def reduzir_porcento(num, taxa):
    valor = num - ((taxa/100)*num)
    return valor


def metade(num):
    valor = num/2
    return valor


def dobro(num):
    valor = num * 2
    return valor


def moeda(inserir = 0, moeda = "R$"):
    return f'{moeda}{inserir:.2f}'.replace(".", ",")


