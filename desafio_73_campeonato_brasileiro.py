colocados = ("Palmeiras", "Internacional", "Fluminense", "Corinthians", "Flamengo", "Athletico-PR", "Atlético-MG", "Fortaleza", "São Paulo", "América-MG", "Botafogo", "Santos", "Goiás", "Bragantino", "Coritiba", "Cuiabá", "Ceará", "Atlético-GO", "Avaí", "Juventude")
a = colocados.index("Bragantino") + 1
print(f"Os 5 primeiros times foram {colocados[0: 5]}")
print(f"Os rebaixados foram {colocados[-4:]}")
print(f"Os times em ordem alfabética são {sorted(colocados)}")
print(f"O Bragantino está na {a}ª posição")

