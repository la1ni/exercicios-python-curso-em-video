def notas(* n, sit=True):
    """
    -> Analisa as notas digitadas
    :param n: notas inseridas
    :param sit: (opcional) - se verdadeiro, mostra a situação da turma com base na média
    :return: retorna dicionário com a maior, menor, quantidade de notas e média
    """
    contador = 0
    maior = 0
    menor = 0
    diario = dict()
    soma = 0
    for nota in n:
        contador += 1
        soma += nota
        if nota >= maior:
            maior = nota
        if contador == 1:
            menor = nota
        elif nota < menor:
            menor = nota
    diario['quantidade'] = contador
    diario['maior_nota'] = maior
    diario['menor_nota'] = menor
    diario['media'] = (soma/contador)
    if sit:
        if diario['media'] < 5:
            diario['situacao'] = "Ruim"
        elif 7 > diario['media'] >= 5:
            diario['situacao'] = "Regular"
        else:
            diario['situacao'] = "Boa"
    return diario


resposta = notas(9, 5.6, 3, 5, 10, 10)
print(resposta)


