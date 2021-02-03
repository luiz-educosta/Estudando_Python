"""
99. Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""
from time import sleep
def maior(*num):
    cont = maior = 0
    print('-=' * 40)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.5)
        if cont == 0:
            maior = valor
        if valor > maior:
            maior = valor
        cont += 1
    sleep(0.5)
    print(f'Foram informados {len(num)} valores ao todo.')
    sleep(0.5)
    print(f'O maior valor informado foi {maior}.')
    sleep(0.5)
#Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

