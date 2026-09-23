import os

os.system('cls')

n1 = input('Digite um número: ')
if n1.isnumeric():
    print('-' * 20)
    n2 = input('Digite outro número: ')
    if n2.isnumeric():
        print('-' * 20)
        soma = int(n1) + int(n2)
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
else:
    print('Digite um número válido')
