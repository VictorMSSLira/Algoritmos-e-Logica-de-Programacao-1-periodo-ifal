# [#10] Receba a medida de dois ângulos de um triângulo, calcule e mostre a medida do terceiro ângulo.

import os
os.system('cls')

angulo1 = float(input('Digite o valor do ângulo 1: '))
angulo2 = float(input('Digite o valor do ângulo 2: '))

angulo3 = 180 - angulo1 - angulo2

os.system('cls')
print('='*80)
print(f"o valor do terceiro ângulo interno do triângulo é de \033[32m{angulo3:0.2f}º\033[0m.")
print('='*80)