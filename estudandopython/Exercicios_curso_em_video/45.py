"""
45.Crie um programa que faça o computador jogar Jokenpô com você.
"""
from time import sleep
import random
print('Suas opções:')
print("""
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA""")
jogada = int(input('Qual a sua jogada?'))
if jogada == 0:
    jogador = 'PEDRA'
elif jogada == 1:
    jogador = 'PAPEL'
elif jogada == 2:
    jogador = 'TESOURA'
else:
    print('Você não digitou nenhuma das opções! Jogue novamente!')

jogo = ['PEDRA', 'PAPEL', 'TESOURA']  # LISTA ALEATÓRIA CRIADA
computador = random.choice(jogo)  # GERANDO ELEMENTO ALEATÓRIO
"""
poderia ter colocado:
jogo = ['PEDRA', 'PAPEL', 'TESOURA']
computador = randint(0,2)
print(f'O computador escolheu {jogo[computador]}')
print(f'Jogador jogou {jogo[jogador]})

"""

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)

print('=-' * 11)
print(f'Computador jogou {computador}')
print(f'Jogador jogou {jogador}')
print('-=' * 11)

if jogador == 'PEDRA' and computador == 'PEDRA':
    print('EMPATE!!!')
elif jogador == 'PAPEL' and computador == 'PAPEL':
    print('EMPATE!!!')
elif jogador == 'TESOURA' and computador == 'TESOURA':
    print('EMPATE!!!')
elif jogador == 'PEDRA' and computador == 'TESOURA':
    print('JOGADOR VENCE!')
elif jogador == 'PAPEL' and computador == 'PEDRA':
    print('JOGADOR VENCE!')
elif jogador == 'TESOURA' and computador == 'PAPEL':
    print('JOGADOR VENCE!')
elif jogador == 'PEDRA' and computador == 'PAPEL':
    print('COMPUTADOR VENCE!')
elif jogador == 'PAPEL' and computador == 'TESOURA':
    print('COMPUTADOR VENCE!')
elif jogador == 'TESOURA' and computador == 'PEDRA':
    print('COMPUTADOR VENCE!')
