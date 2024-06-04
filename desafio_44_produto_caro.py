pr = float(input('Qual o preço do produto? '))
print('Condições de pagamento:\nDinheiro/Cheque --- Digite 1\nÀ vista no cartão --- Digite 2\nDuas vezes no cartão --- Digite 3\nTrês ou mais vezes no cartão --- Digite 4')
cond = int(input('Qual será a condição de pagamento? '))
a = pr - 0.1*pr
b = pr - 0.05*pr
c = pr/2
d = 0.2*pr
e = pr + d
if cond == 1:
      print(f'O produto terá 10% de desconto, sendo o novo valor que você pagará igual a R${a:.2f}')
elif cond == 2:
      print(f'O produto terá 5% de desconto, sendo o valor que você vai pagar igual a R${b:.2f}')
elif cond == 3:
      print(f'Você pagará o valor normal, RS{pr:.2f}. A parcela será de R${c:.2f}')
else:
      print(f'Você acabará pagando 20% a mais de juros no valor do produto, o que corresponde a R${d:.2f} totalizando R${e:.2f}')