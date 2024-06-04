def printados():
    print("-" * 100)
    print("*-+%/" * 20)
    print("-" * 100)
    print(f'{"Bem vindo ao analisador de expressão matemática":^90}')
    print("-" * 100)
    print("*-+%/" * 20)
    print("-" * 100)


parenteses = []
paberto = pfechado = 0
fechado_sem_abrir = 0
printados()
expressao_digitada = str(input("Digite uma expresão matemática que use parênteses: "))
for letra in expressao_digitada:
    if letra == ("("):
        paberto += 1
        parenteses.append(letra)
    elif letra == (")"):
        pfechado += 1
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            fechado_sem_abrir =+ 1
if len(parenteses) == 0 and fechado_sem_abrir == 0:
    print("Expressão válida!")
else:
    print("Expressão inválida!")
    if paberto > pfechado:
        print(f"Você esqueceu de fechar {paberto - pfechado} parênteses")
    elif pfechado > paberto:
        print(f"Você esqueceu de abrir {pfechado - paberto} parênteses")
    elif pfechado == paberto:
        print("Parênteses na ordem errada")

