contador = 1
maiores = 0
homens = 0
mulher_jovem = 0
while True:
    idade = int(input(f"Insira a idade da {contador}ª pessoa: "))
    sexo = str(input(f"Insira o sexo da {contador}ª pessoa [M/F]: ")).upper().strip()
    continua = str(input("Deseja continuar? [S/N] ")).upper().strip()
    if idade >= 18:
        maiores += 1
    if sexo == "M":
        homens += 1
    if sexo == "F":
        if idade < 20:
            mulher_jovem += 1
    if continua == "N":
                break
    contador += 1
print(f"{maiores} são maiores de idade. {homens} são homens e {mulher_jovem} são mulheres de menos de 20 anos.")
