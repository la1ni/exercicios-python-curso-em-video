def ficha(nome="", gols=0):
    if nome == "":
        nome = "<sem_nome>"
    if gols == "":
        gols = 0
    print(f"O jovgador {nome} fez {gols} gols no campeonato")


nome_input = str(input("Qual o nome do jogador?")).strip().capitalize()
gols_input = (input("Quantos gols o jogador fez? "))
if gols_input.isnumeric():
    gols_input = int
else:
    gols_input = 0
ficha(nome_input, gols_input)
