# [#6] Receba o salário de um funcionário e o percentual de aumento, calcule e mostre o valor do aumento e o novo salário.

import os
os.system('cls')

salario_antigo = float(input("Digite o valor do seu salário atual\n"))
aumento_percentual = float(input("Digite o aumento percentual do seu salário (%)\n"))

valor_aumento = salario_antigo * (aumento_percentual / 100)
valor_total = salario_antigo + valor_aumento

os.system('cls')

print('='*80)
print(f"Seu salário teve um aumento de \033[32mR${valor_aumento:0.2f}\033[0m. Agora, você recebe um salário de \033[32mR${valor_total:0.2f}\033[0m")
print('='*80)