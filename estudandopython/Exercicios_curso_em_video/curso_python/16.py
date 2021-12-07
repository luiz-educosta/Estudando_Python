"""
16. Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
"""
from math import trunc
real = float(input('Digite um valor:'))
inteiro = int(real)
# print(f'O valor digitado foi {real} e a sua porção inteira é {inteiro}.')
print(f'O valor digitado foi {real} e a sua porção inteira é {trunc(real)}.')
