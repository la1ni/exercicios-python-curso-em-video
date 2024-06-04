nomes_de_numeros = ("ZERO", "UM", "DOIS", "TRÊS", "QUATRO", "CINCO", "SEIS", "SETE", "OITO", "NOVE", "DEZ", "ONZE", "DOZE", "TREZE", "CATORZE", "QUINZE", "DESESSEIS", "DEZESSETE", "DEZOITO", "DEZENOVE", "VINTE")
n = -1
while True:
    n = int(input("Digite um número entre 0 e 20... "))
    if 0 <= n <= 20:
        print(f"Você digitou o número {nomes_de_numeros[n]}")
        continua = str(input("Deseja continuar [S/N] ")).upper().strip()
        if continua == "N":
            break
    else:
        print("Tente novamente...", end=" ")
