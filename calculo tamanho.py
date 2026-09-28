import os

os.system('cls')

n = input('Qual o tamanho em metros que você quer converter para milímetros e centimetros?: ')
if '.' in n:
    n = float(n)
else:
    n = int(n)

c = n * 100
m = n * 1000

print ('Tamanho original: {} \n Tamanho em centímetros: {} \n Tamanho em milímetros: {}'.format(n, c, m))