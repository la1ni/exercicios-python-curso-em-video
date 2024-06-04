escolha = str("S").upper()
contador = 0
soma = 0
anterior = 0
maior = 0
menor = 0
n = 0
while escolha == "S":
    anterior = n
    n = int(input("Digite um número inteiro positivo: "))
    while n <= 0:
        print("Observe as regras! Inteiro e positivo...")
        n = int(input("Digite um número inteiro positivo: "))
    escolha = str(input("Deseja continuar? [S/N] ")).upper().strip()
    contador += 1
    soma += n
    if n >= maior:
        maior = n
    if contador == 1:
        menor = n
    if menor >= n:
        menor = n
print(f"Você digitou {contador} números e a média deles é {soma/contador:.2f}, sendo sua soma {soma}\nO maior deles é {maior}, e o menor, {menor}")
