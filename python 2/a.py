import os

os.system('cls')

vc = float(input('Qual o valor da casa? '))
salário = float(input('Qual o seu salário? '))
tempo = int(input('Em quantos anos você vai pagar? '))

meses = tempo * 12
presmensal = vc / meses

if presmensal <= salário * (30/100):
    print('Prestação Mensal permitida.')
elif presmensal > salário * (30/100):
    print('Prestação Mensal negada.')