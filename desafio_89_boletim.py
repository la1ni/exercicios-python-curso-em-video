lista_geral = list()
contador = 0
while True:
    lista_geral.append([])
    lista_geral[contador].append(str(input(f"Digite o nome {contador+1} do aluno: ").capitalize()))
    lista_geral[contador].append([])
    for c in range(0, 2):
        nota = (float(input(f"Digite a {c+1} nota: ")))
        lista_geral[contador][1].append(nota)
    contador += 1
    deseja_continuar = str(input("Deseja continuar [S/N]? ")).strip().upper()
    if deseja_continuar == "N":
        break
print("-" * 60)
print(f'{"Nº":<6} {"NOME":<15} {"MÉDIA"}')
print("-" * 60)
for i, aluno in enumerate(lista_geral):
    print(f"{i+1:<6} {lista_geral[i][0]:<15} {(lista_geral[i][1][0]+lista_geral[i][1][1])/2:.2f}")
while True:
    print("-" * 60)
    qual = int(input("Você quer ver as notas de qual aluno (use o Nº)? [999 interrompe o programa] "))
    if qual == 999:
        break
    else:
        print(f"Notas de {lista_geral[qual-1][0]} são {lista_geral[qual-1][1][0]} e {lista_geral[qual-1][1][1]}")
print("-" * 60)
