""""
93. Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""
jogador = {}
tot = 0
golsnapartida = []
jogador['nome'] = str(input('Nome do jogador:'))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))
for c in range(0,partidas):
    saldo = int(input(f'Quantos gols na partida {c}?'))
    golsnapartida.append(saldo)
    tot += saldo
jogador['gols'] = golsnapartida[:]
jogador['total'] = tot  #  poderia ter usado a função sum(golsnapartida) ai não precisava de colocar o tot
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')  #  se n usou o tot, ai era só colocar o o len(jogador['gols'])
for c, v in enumerate(golsnapartida):
    print(f' => Na partida {c}, fez {v} gols. ')
print(f'Foi um total de {jogador["total"]} gols.')