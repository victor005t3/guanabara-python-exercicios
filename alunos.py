import os
import random

os.system('cls')

aluno1 = str(input('Escolha o primeiro aluno para ser sorteado: '))
aluno2 = str(input('Escolha o segundo aluno para ser sorteado: '))
aluno3 = str(input('Escolha o terceiro aluno para ser sorteado: '))
aluno4 = str(input('Escolha o quarto aluno para ser sorteado: '))


sorteio = random.choice([aluno1, aluno2, aluno3, aluno4])

print(f'O aluno escolhido foi: {sorteio}')