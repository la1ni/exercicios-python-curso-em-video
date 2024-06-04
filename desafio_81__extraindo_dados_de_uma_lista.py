valores_digitados = []
contador = 0
while True:
    numero_inserido = int(input("Insira um número: "))
    contador += 1
    valores_digitados.append(numero_inserido)
    deseja_continuar = str(input("Deseja continuar? [S/N]: ")).upper().strip()
    if deseja_continuar == "N":
        break
    while deseja_continuar != "S" and "N":
        print("Por favor, responda...")
        deseja_continuar = str(input("Deseja continuar? [S/N]: ")).upper().strip()
lista_reversa = sorted(valores_digitados)[::-1]
print(f"Você digitou {contador} números.")
print(f"Em ordem decrescente, os valores são: {lista_reversa} ")
if 5 in valores_digitados:
    print(f"\nO valor 5 aparece {valores_digitados.count(5)} vezes")
else:
    print("\nO valor 5 não aparece")
