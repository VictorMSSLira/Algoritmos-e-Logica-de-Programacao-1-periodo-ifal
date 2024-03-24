# [#3] Efetuar o cálculo e apresentar o valor de uma prestação de um bem em atraso, utilizando a fórmula PRESTACAO <- VALOR +VALOR * (TAXA/100)*TEMPO_MES

import os

os.system('cls')

print('Digite o valor do bem: ', end="")
valor = float(input())
print('Digite a taxa de juros (%): ', end="")
taxa = float(input())
print('Digite o tempo de atraso em meses: ', end="")
tempo_mes = int(input())

prestacao = valor + valor * (taxa/100) * tempo_mes

os.system('cls')

print('='*80)
print(f"O valor da prestação em atraso é: \033[32mR${prestacao:0.2f}\033[0m")
print('='*80)