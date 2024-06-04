jogador = dict()
golos = list()
soma = 0
jogador['nome'] = str(input("Qual o nome do jogador? ")).capitalize()
jogador['partidas'] = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
for c in range(1, jogador['partidas'] + 1):
    por_partida = (int(input(f"Quantos gols {jogador['nome']} fez na {c}ª partida? ")))
    golos.append(por_partida)
    soma += por_partida
jogador['gols'] = golos
jogador['total'] = soma
print("-=" * 18)
for k, v in jogador.items():
    print(f"O campo {k} tem o valor {v}")
print("-=" * 18)
print(f"O jogador {jogador['nome']} fez {jogador['partidas']} partidas")
for i, partida in enumerate(golos):
    if partida == 0:
        print(f"Na {i+1}ª partida ele não fez gols")
    elif partida == 1:
        print(f"Na {i+1}ª partida ele fez {partida} gol")
    elif partida > 1:
        print(f"Na {i + 1}ª partida ele fez {partida} gols")
print(f"No total ele fez {jogador['total']} gols")
print(f"Uma média de {jogador['total']/jogador['partidas']:.2f} gols por partida")
if jogador['total']/jogador['partidas'] > 0.5:
    print("Ele é um craque!")
else:
    print("Provavelmente ele não deve ser atacante...")
print("-=" * 18)
