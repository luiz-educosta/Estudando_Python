"""
28. Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""
from random import randint
from time import sleep

print('-*-' * 20)
print('Vou pensar em um número entre 0 e 5. Teste adivinhar...')
print('-*-' * 20)
num = int(input('Em qual número eu pensei?'))
print('PROCESSANDO...')
print('-*-' * 20)
sleep(3)
aleatorio = randint(0, 5)  # Gera números inteiros aleatórios de 0 a 5

if aleatorio == num:
    print(f'Parabéns! Você conseguiu me vencer!')
    print('-*-' * 20)
else:
    print(f'Eu pensei no número {aleatorio} e não no {num}!')
    print('-*-' * 20)
