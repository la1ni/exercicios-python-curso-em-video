dados_geral = list()
temporario = dict()
somaidades = 0
mulheres = list()
while True:
    temporario['nome'] = str(input("Digite o nome: ")).strip().capitalize()
    temporario['idade'] = int(input("Digite a idade: "))
    while True:
        temporario['sexo'] = str(input("Digite o sexo [M/F]: ")).upper().strip()
        if temporario['sexo'] in "MF":
            break
        print("ERRO! Apenas M ou F")
    somaidades += temporario['idade']
    if temporario['sexo'] == "F":
        mulheres.append(temporario['nome'])
    dados_geral.append(temporario.copy())
    temporario.clear()
    while True:
        deseja_continuar = str(input("Deseja continuar [S/N]? ")).upper().strip()
        if deseja_continuar in "SN":
            break
        print("ERRO! Apenas S ou N")
    if deseja_continuar == "N":
        break
print(dados_geral)
print("-=" * 30)
print(f"- O número de pessoas no grupo é {len(dados_geral)}")
print(f"- A média das idades é {somaidades/len(dados_geral):.2f}")
print(f"- As mulheres cadastradas são {mulheres}")
print(f"- Lista de pessoas acimea da média de idade do grupo: ", end= " ")
for dados in dados_geral:
    if dados['idade'] > (somaidades/len(dados_geral)):
        print(f"{dados['nome']}, com {dados['idade']} anos",end= " | ")




