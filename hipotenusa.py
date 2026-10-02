import math
import os

os.system('cls')
co = input('Digite o cateto oposto: ')
print('-' * 20)
ca = input('Digite o cateto adjacente: ')
print('-' * 20)

co = float(co)
ca = float(ca)

coq = math.pow(co, 2)
caq = math.pow(ca, 2)

qh = coq + caq
h = math.pow(qh, 0.5)

print(f'O cateto oposto é {co} e o adjacente é {ca}')
print('-' * 20)
print(f'O quadrado do cateto oposto é {coq} e o quadrado do cateto adjacente é {caq}')       
print('-' * 20)
print(f'A soma dos dois é {qh}, cujo mesmo é o quadrado da hipotenusa')
print('-' * 20)
print(f'A hipotenusa é {h:.5f}')
print('-' * 20)