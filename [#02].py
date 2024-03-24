# [#2] Obter e atribuir um valor randômico a uma variável inteira...utiliza-se a função randômica da ferramenta de pseudocódigo (u.sorteia(valor_inicial, valor_final) no Studio).

import os
import random

os.system('cls')

num_aleatorio = random.choice(range(1, 101))

print('='*80)
print(f"O número sorteado foi: \033[31m{num_aleatorio}\033[0m")
print('='*80)