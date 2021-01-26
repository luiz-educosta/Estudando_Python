"""
87.Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""
from random import randint
from time import sleep
lista = list()
total = 1
jogos = list()
print('=' * 40)
print(f'{"JOGO NA MEGA SENA":^40}')
print('=' * 40)
sorteio = int(input('Quantos jogos você quer que eu sorteie?'))
print('=' * 6, f'SORTEANDO {sorteio} JOGOS', '=' * 6)

while total <= sorteio:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
for c in range(0, len(jogos)):
    print(f'Jogo {c+1}: {jogos[c]}')
    sleep(1)
print('Boa sorte!')
""" 
outro meio:
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
"""
