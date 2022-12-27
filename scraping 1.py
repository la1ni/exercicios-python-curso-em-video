import re
#re.função (padrão, string, flag)
#print (var.group()) -> retorna o termo buscado ao invés da posição
#. retorna qualquer caractere exceto enter. Usando re.DOTALL na flag, pega também o enter
#^ busca caracteres no inicio da string apenas e $, no fim
#\ é o escape, ou seja, em re.função (\., string, flag), o ponto é realmente um ponto
# [] procura sequência ex: [1-9]#
texto = ("existE um grandE clube na cidade e ele mora dentro do meu coração")
#a = re.compile("e", re.IGNORECASE)
b = re.findall("e", texto, re.IGNORECASE)
print (b)

