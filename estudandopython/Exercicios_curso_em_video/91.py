"""
91. Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
"""
from random import randint
from time import sleep
from operator import itemgetter

sorteado = {}
ranking = ()

print('Valores sorteados:')
#  sorteando os valores
for c in range(1,5):
    sorteado[f'jogador{c}'] = randint(1,6)    
#  imprimindo
for k, v in sorteado.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)

print('-=' * 30)
print(f'{"== RANKING DOS JOGADORES =="}')

#  precisou criar outra lista para poder colocar os numeros sortidos
#  coloca os itens a serem sorteados, a parte do dicionario que vai pegar
#  e inverte para poder colocar em ordem do maior pro maior
ranking = sorted(sorteado.items(), key=itemgetter(1), reverse=True)


for i, v in enumerate(ranking):
    print(f'{i+1}º lugar : {v[0]} com {v[1]}')
    sleep(1)
    