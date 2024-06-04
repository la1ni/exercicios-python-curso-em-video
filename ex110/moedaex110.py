def moeda(inserir=0.0, moeda="R$"):
    return f'{moeda:>4}{inserir:>8.2f}'


def resumo(valor=0, taxa_aumentar=0, taxa_reduzir=0):
    print("-" * 50)
    print(f'{"RESUMO DOS VALORES":^40}')
    print("-" * 50)
    dobro = valor * 2
    metade = valor/2
    aumentar = valor + valor*(taxa_aumentar/100)
    reduzir = valor - valor*(taxa_reduzir/100)
    print(f"Valor analisado: \t{moeda(valor)}")
    print(f"Dobro do valor: \t{moeda(dobro)}")
    print(f"Metade do valor: \t{moeda(metade)}")
    print(f"{taxa_aumentar}% de aumento: \t{moeda(aumentar)}")
    print(f"{taxa_reduzir}% de redução: \t{moeda(reduzir)}")
    print("-" * 50)



