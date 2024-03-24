# [#4] Apresente o valor da conversão em dólar (U$) de um valor lido em real (R$). O algoritmo deve solicitar o valor da cotação do dólar e também a quantidade de reais disponível com o usuário.

import os

os.system('cls')

cotacao_dolar = float(input('Digite a cotação atualizada do dólar (U$): '))
valor_reais = float(input('Digite o valor, em reais (R$),  que você deseja converter: '))

valor_dolar = valor_reais / cotacao_dolar

os.system('cls')

print('='*80)
print(f"O valor de \033[36mR${valor_reais:0.2f}\033[0m equivale, aproximadamente, a \033[32mU${valor_dolar:0.2f}\033[0m")
print('='*80)