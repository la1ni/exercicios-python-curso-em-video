print("-" * 50)
print("BEM VINDO AO CAIXA 24h!")
print("Disponíveis cédulas de 50, 20, 10 e 1")
print("-" * 50)
valor_do_saque = int(input("Qual o valor que você quer sacar? "))
while valor_do_saque < 1:
    print("Inteiros e positivos...")
    valor_do_saque = int(input("Qual o valor que você quer sacar?"))
notas50 = valor_do_saque // 50
notas20 = ((valor_do_saque - (notas50 * 50)) // 20)
notas10 = ((valor_do_saque - (notas50 * 50) - (notas20 * 20)) // 10)
notas1 = ((valor_do_saque - (notas50 * 50) - (notas20 * 20) - (notas10 * 10)) // 1)
print("-------------------- TOTAIS --------------------")
if notas50 >= 1:
    print(f"{notas50} cédulas de 50")
if notas20 >= 1:
    print(f"{notas20} cédulas de 20")
if notas10 >= 1:
    print(f"{notas10} cédulas de 10")
if notas1 >= 1:
    print(f"{notas1} cédulas de 1")
