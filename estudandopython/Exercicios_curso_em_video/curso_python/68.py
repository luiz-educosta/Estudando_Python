"""
68. Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""
from random import randint
cont = 0
print('=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 20)

while True:
    soma = 0
    valor = int(input('Digite um valor:'))
    computador = randint(0, 10)
    soma = valor + computador
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
    print('-' * 40)
    print(
        f'Você jogou {valor} e o computador {computador}. Total de {soma}', end=' ')
    print('DEU PAR' if soma % 2 == 0 else 'DEU ÍMPAR')
    """    
    if soma % 2 == 0:
        print('DEU PAR')
    else:
        print('DEU ÍMPAR')
    print('-' * 40)
    """
    if escolha == 'P' and soma % 2 == 0:
        print('Você VENCEU!')
        print('Vamos jogar novamente..')
        print('=-' * 20)
        cont += 1
    elif escolha == 'I' and soma % 2 != 0:
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print('=-' * 20)
        cont += 1
    else:
        print('Você PERDEU!')
        print('=-' * 20)
        break

print(f'GAME OVER! Você venceu {cont} vezes.')
