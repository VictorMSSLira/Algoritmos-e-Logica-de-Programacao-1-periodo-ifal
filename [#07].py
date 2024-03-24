# [#7] Receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre  a idade dessa pessoa e quantos anos ela será em 2050.

import os
import datetime
os.system('cls')
ano_atual = datetime.datetime.now().year

ano_nascimento = int(input('Digite o ano de seu nascimento: '))

idade_atual = ano_atual - ano_nascimento
idade_2050 = 2050 - ano_nascimento

os.system('cls')
print('='*80)
print(f"Neste ano de {ano_atual}, você completa \033[32m{idade_atual}\033[0m anos de idade. Em 2050, você terá \033[32m{idade_2050}\033[0m anos de idade")
print('='*80)