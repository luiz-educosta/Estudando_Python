"""
60. Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

5! = 5 x 4 x 3 x 2 x 1 = 120
"""
from math import factorial
fatorial = 1
numero = int(input('Digite um número para \ncalcular seu fatorial:'))
print(f'Calculando {numero}! = ', end='')
while numero > 0:
    fatorial = fatorial * numero  # ou ainda fatorial *= numero
    print(f'{numero}', end='')
    print(' x ' if numero > 1 else ' = ', end='')
    numero -= 1

print(f'{fatorial}')

#  Ou ainda
n = int(input('Digite um número para calcular seu fatorial:'))
f = factorial(n)
print(f'O fatorial de {n} é {f}.')
