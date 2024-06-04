def aumentar_porcento(num=0.0, taxa=0, form=True):
    valor = num + (taxa / 100 * num)
    if form:
        return moeda(valor)
    else:
        return valor


def reduzir_porcento(num=0.0, taxa=0, form=True):
    valor = num - ((taxa / 100) * num)
    if form:
        return moeda(valor)
    else:
        return valor


def metade(num=0.0, form=True):
    valor = num / 2
    if form:
        return moeda(valor)
    else:
        return valor


def dobro(num=0.0, form=True):
    valor = num * 2
    if form:
        return moeda(valor)
    else:
        return valor


def moeda(inserir=0.0, moeda="R$"):
    return f'{moeda}{inserir:.2f}'.replace(".", ",")


def resumo(valor=0.0, taxa_aumentar=0, taxa_reduzir=0):
    print("-" * 50)
    print(f'{"RESUMO DOS VALORES":^40}')
    print("-" * 50)
    print(f"Valor analisado: \t{(moeda(valor))}")
    print(f"Dobro do valor: \t{dobro(valor)}")
    print(f"Metade do valor: \t{metade(valor)}")
    print(f"{taxa_reduzir}% de redução: \t{reduzir_porcento(valor, taxa_reduzir)}")
    print(f"{taxa_aumentar}% de aumento: \t{aumentar_porcento(valor, taxa_aumentar)}")
    print("-" * 50)