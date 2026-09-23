import os

os.system('cls')

nome = input('Qual o seu nome?: ')

if nome == 'José' or nome == 'João' or nome == 'Antônio' or nome == 'Francisco' or nome == 'Pedro':
    print('Bem vindo, {}, seu nome é bem popular no Brasil.'.format(nome))
elif nome == 'Maria' or nome == 'Ana' or nome == 'Francisca' or nome == 'Júlia' or nome == 'Antônia':
    print('Bem vinda, {}, seu nome é bem popular no Brasil.'.format(nome))
else:
    print('Bem vindo/a, {}.'.format(nome))
print ('É um prazer te conhecer')