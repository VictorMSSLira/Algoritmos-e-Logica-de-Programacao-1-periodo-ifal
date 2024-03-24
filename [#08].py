# [#8] Receba o peso de uma pessoa, calcule e mostre dois novos pesos, se a pessoa engordar 15% e se emagrecer 20% sobre o peso digitado.

import os
os.system('cls')

peso = float(input('Digite seu peso em quilograma (Kg): '))

ganha_15 = peso * 1.15
perde_20 = peso * 0.8

os.system('cls')
print('='*80)
print(f"Se você \033[32mganhasse 15%\033[0m do seu peso atual, você teria \033[32m{ganha_15:0.2f}Kg\033[0m. \nSe você \033[31mperdesse 20%\033[0m do seu peso atual, você teria \033[31m{perde_20:0.2f}Kg\033[0m.")
print('='*80)