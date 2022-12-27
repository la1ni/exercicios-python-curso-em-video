a = int(input('Digite o tamanho de uma reta: '))
b = int(input('Digite o tamanho de outra reta: '))
c = int(input('Digite o tamanho de mais uma reta: '))
if ((a + b) > c) & ((b + c) > a) & ((c + b) > a) :
    print('Essas três retas são capazes de formar um trângulo!')
else:
    print('Essas três retas não conseguem formar um triângulo...')