import os

os.system('cls')

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

s = n1 + n2


if s < n3:
    print('A Soma dos números A e B é: {}'.format(s))
    print('A Soma é menor que o terceiro número.')
elif s == n3:
    print('A Soma dos números A e B é: {}'.format(s))
    print('A Soma é igual ao terceiro número.')
elif s >= n3:
    print('A Soma dos números A e B é: {}'.format(s))
    print('A Soma é maior que o terceiro número.')
else:
    print('Cálculo impossível/inválido.')
    exit()