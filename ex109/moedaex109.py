def aumentar_porcento(num=0, taxa=0, form=True):
    valor = num + (taxa/100*num)
    if form:
        return moeda(valor)
    else:
        return valor


def reduzir_porcento(num, taxa, form=True):
    valor = num - ((taxa/100)*num)
    if form:
        return moeda(valor)
    else:
        return valor


def metade(num, form=True):
    valor = num/2
    if form:
        return moeda(valor)
    else:
        return valor


def dobro(num, form=True):
    valor = num * 2
    if form:
        return moeda(valor)
    else:
        return valor


def moeda(inserir=0.0, moeda = "R$"):
    return f'{moeda}{inserir:.2f}'.replace(".", ",")


