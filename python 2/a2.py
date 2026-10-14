import os

os.system('cls')

print('-=' * 20)
n = int(input('Digite um número inteiro: '))
print('-=' * 20)

binario = format(n, 'b')
octal = format(n, 'o')
hexa = hex(n)

print('Qual conversor deseja?')
print('-=' * 20)
print('1 - Binário')
print('-=' * 20)
print('2 - Octal')
print('-=' * 20)
print('3 - Hexadecimal')
print('-=' * 20)
opção = int(input(''))

if opção == 1:
    print(f'Seu código {n} em binário é {binario}')
elif opção == 2:
    print(f'Seu código {n} em octal é {octal}')
elif opção == 3:
    print(f'Seu código {n} em hexadecimal é {hexa}')
else:
    print('Número impossível ou não-numeral.')
    exit()