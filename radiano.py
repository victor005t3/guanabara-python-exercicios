import os
import math

os.system('cls')
angulo = int(input('Digite o ângulo: '))

sen = round(math.sin(math.radians(angulo)), 2)
cos = round(math.cos(math.radians(angulo)), 2)
tan = round(math.tan(math.radians(angulo)), 2)

print(f'O Seno do seu ângulo é {sen}')
print(f'O Cosseno do seu ângulo é {cos}')
print(f'A Tangente do seu ângulo é {tan}')