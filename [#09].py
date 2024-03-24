# [#9] Receba o valor dos catetos de um triângulo, calcule e mostre o valor da hipotenusa.

import os
os.system('cls')

cateto1 = float(input('Digite o valor do cateto 1: '))
cateto2 = float(input('Digite o valor do cateto 2: '))

hipotenusa = (cateto1 ** 2 + cateto2 ** 2) ** 0.5

os.system('cls')
print('='*80)
print(f"O valor da hipotenusa é \033[32m{hipotenusa:0.2f}\033[0m.")
print('='*80)