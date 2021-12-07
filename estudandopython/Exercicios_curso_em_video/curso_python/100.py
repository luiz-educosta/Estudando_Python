"""
100. Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
"""
from random import randint
from time import sleep
lista = list()
num = list()

def sorteia(lista):
    print(f'Sorteando 5 valores da lista:', end='')
    for c in range(1, 6):
        lista.append(randint(0, 10))
    #  Poderia ter armazenado o valor aleatório em uma variavel para economizar em usar um só for
    for c, v in enumerate(lista):
        print(f'{v} ', end='', flush=True)
        sleep(0.5)
    print('PRONTO!')

def somaPar(lista):
    soma = 0
    for c, v in enumerate(lista):
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores pares de {lista}, temos {soma}')


# Programa principal
sorteia(num)
somaPar(num)