import os

os.system('cls')

n1 = int(input('Qual a nota do aluno?: '))
n2 = int(input('Qual a nota do segundo trimestre do aluno?: '))

m = (n1 + n2) / 2
print('A nota do aluno é {}.'.format(m))
if (m) >= 6:
    print('Passou de ano.')
else:
    print('Reprovado.')
