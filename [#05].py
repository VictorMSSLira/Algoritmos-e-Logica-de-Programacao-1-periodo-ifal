# [#5] Converter uma temperatura dada em Celsius para Farenheit e Kelvin.

import os

os.system('cls')

print('Digite a temperatura em Celsius (°C): ', end="")
temperatura_celsius = float(input())

temperatura_fahrenheit = (temperatura_celsius * 9 / 5) + 32
temperatura_kelvin = temperatura_celsius + 273.15

os.system('cls')

print('='*80)
print(f"Sua temperatura em Fahrenheit é: \033[32m{temperatura_fahrenheit:0.2f} °F\033[0m")
print('='*80)
print(f"Sua temperatura em Kelvin é:  \033[32m{temperatura_kelvin:0.2f} K\033[0m")
print('='*80)