"""
63. Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:

0 – 1 – 1 – 2 – 3 – 5 – 8
"""
print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)
termos = int(input('Quantos termos você quer mostrar: '))
c = 3
t1 = 0
t2 = 1
print(f'{t1} -> {t2}', end='')
while c <= termos:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    c += 1
print(' -> FIM')
