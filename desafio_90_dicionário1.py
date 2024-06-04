boletim = {}
boletim['Nome'] = str(input("Qual o nome do aluno? "))
boletim['Média'] = float(input("Qual a média das notas dele? "))
if boletim['Média'] < 7:
    boletim['Situação'] = "reprovado"
else:
    boletim['Situação'] = "aprovado"
for k, v in boletim.items():
    print(f"{k} é {v}")