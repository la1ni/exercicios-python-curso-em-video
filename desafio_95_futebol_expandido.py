time = list()
jogador = dict()
golos = list()
soma = 0
while True:
    jogador['nome'] = str(input("Digite o nome do jogador: ")).capitalize()
    jogador['partidas'] = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    for c in range(1, (jogador['partidas']+1)):
        por_partida = (int(input(f"Quantos gols {jogador['nome']} fez na {c}ª partida? ")))
        golos.append(por_partida)
        soma += por_partida
    jogador['gols'] = golos.copy()
    jogador['total'] = soma
    soma = 0
    golos.clear()
    time.append(jogador.copy())
    jogador.clear()
    while True:
        deseja_continuar = str(input("Deseja continuar [S/N]? ")).upper().strip()
        if deseja_continuar in "SN":
            break
        print("ERRO! Apenas S ou N")
    if deseja_continuar == "N":
        break
print("-=" * 30)
print(f'{"CÓDIGO":<8} {"NOME":<20} {"GOLS":<25} {"TOTAL":<5}')
print("-" * 60)
for cont, j in enumerate(time):
    gols_visual = str(j['gols'].copy())
    print(f"{cont + 1:<8} {j['nome']:<20} {gols_visual:<25} {j['total']:<5}")
print("-" * 60)
while True:
    qual = int(input("Mostrar o levantamento de qual jogador? (999) para parar: "))
    if qual == 999:
        break
    if qual > len(time):
        print("INVÁLIDO! ESCOLHA UM CODIGO DE JOGADOR QUE EXISTE")
    else:
        print(f"Estatística do jogador {time[qual-1]['nome']}")
        for n, partida in enumerate(time[qual-1]['gols']):
            print(f"Na {n+1} ele fez {partida} gols")
        print(f"Uma média de {time[qual-1]['total']/len(time[qual-1]['gols']):.2f} por partida")
print("=========== VOLTE SEMPRE ============")
