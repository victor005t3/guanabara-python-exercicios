import os

os.system('cls')
i = input('Digite Qualquer Coisa: ')

print('O tipo primitivo do seu imput é:', type(i))
print('Só tem espaços?:', i.isspace())
print('É um número?:', i.isnumeric())
print('É alfabético?:', i.isalpha())
print('É número e letra? (alfanumérico):', i.isalnum())
print('Está em maiúsculo?:', i.isupper())
print('Está em minúsculo?:', i.islower())
print('Está capitalizado?:', i.istitle())