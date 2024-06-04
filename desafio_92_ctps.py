from datetime import date
ano = date.today().year
pessoa = dict()
pessoa['nome'] = str(input("Digite seu nome: ")).capitalize()
pessoa['idade'] = (ano - int(input("Digite o ano do seu nascimento: ")))
pessoa['CTPS'] = int(input("Digite sua carteira de trabalho [0 para não possui]: "))
if pessoa['CTPS'] != 0:
    pessoa['salario'] = float(input("Digite seu salário: "))
    print("-=" * 8, "TEORICAMENTE O TEMPO DE CONTRIBUIÇÃO É 35 ANOS", "-=" * 8)
    pessoa['aposentadoria'] = (pessoa["idade"] + 35 - (ano - (int(input("Digite seu ano de contratação: ")))))
for k, v in pessoa.items():
    print(f"{k} recebe o valor de {v}")
