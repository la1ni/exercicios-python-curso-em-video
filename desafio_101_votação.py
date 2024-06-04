from datetime import date


def voto(idade):
    if 16 <= idade < 18 or idade > 65:
        return "tem voto opcional"
    elif 65 > idade >= 18:
        return "tem voto obrigatório"
    else:
        return "não vota..."


anos = ((date.today().year - int(input("Em qual ano a pessoa nasceu? "))))
a = voto(anos)
print(f"Com {anos} anos a pessoa {a}")