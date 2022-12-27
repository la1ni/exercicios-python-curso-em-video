n1 = int(input('Primeiro termo da PA: '))
r = int(input('Qual é a razão da P.A? '))
for c in range (n1, (n1+10*r), r):
    print (c, end= ", ")