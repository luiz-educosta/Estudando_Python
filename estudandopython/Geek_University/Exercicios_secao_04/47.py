"""
47. Leia um número inteiro de 4 dígitos (1000 a 9999) e imprima 1 dígito por linha.
"""
num = int(input('Digite um número de 1000 a 9999:'))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Unidade:{u}')
print(f'Dezena:{d}')
print(f'Centena:{c}')
print(f'Milhar:{m}')
