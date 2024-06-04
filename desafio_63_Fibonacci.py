print("-----------------------------")
print("Sequência de Fibonacci")
print("-----------------------------")
termos = int(input("Quantos termos você quer ver? "))

a = 0
n1 = 0
n2 = 0
n = 0
while a != termos:
    n = n1 + n2
    print(n, end=" -> ")
    n1 = n2
    n2 = n
    a += 1
    if n == 0:
        n1 = 1
    if a == termos:
        print("FIM!")
