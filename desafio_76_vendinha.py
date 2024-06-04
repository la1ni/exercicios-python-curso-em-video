listagem = ("Cadeira", 800.50, "Telefone", 1250.99, "Monitor", 1000, "Cama", 500.75, "Mesa", 300, "Rack", 200.89 )
print("-" * 50)
print(f'{"VENDINHA":^40}')
print("-" * 50)
for pos in range (0, len(listagem)):
    if pos % 2 == 0:
        print(f"{listagem[pos]:.<30}", end= " ")
    else:
        print(f"R${listagem[pos]:>9.2f}")