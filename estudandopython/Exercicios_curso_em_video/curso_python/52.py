"""
52. Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
"""
num = int(input('Digite um número: '))
cont = 0
contP = 0
for c in range(1, num+1):
    if num % c == 0:
        print(f'\033[33m{c}', end=' ')
        contP += 1
    else:
        print(f'\033[31m{c}', end=' ')
print(f'\033[m \nO número {num} foi divisível {contP} vezes')
if cont == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
