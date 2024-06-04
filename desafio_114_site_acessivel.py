import urllib
import urllib.request
try:
    urllib.request.urlopen('http://pudim.com.br/')
except:
    print("Erro!")
else:
    print("Está acessivel!")

