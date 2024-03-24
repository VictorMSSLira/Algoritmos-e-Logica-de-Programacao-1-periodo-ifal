# [#1] Leia três valores numéricos inteiros (representados pelas variáveis A, B e C) e apresente como resultado final o valor da soma dos quadrados dos três valores lidos.

import os

os.system('cls')

print("Digite três números")
print('A: ', end="")
a = float(input())
print('B: ', end="")
b = float(input())
print('C: ', end="")
c = float(input())

valor = (a**2) + (b**2) + (c**2)

os.system('cls')

print('='*80)
print(f"A soma do quadrados dos números é: \033[31m{valor:0.2f}\033[0m")
print('='*80)