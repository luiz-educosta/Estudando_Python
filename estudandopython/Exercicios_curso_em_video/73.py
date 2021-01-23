"""
73. Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time do Corinthians.
"""
times = ('São Paulo', 'Internacional', 'Atlético Mineiro', 'Flamengo', 'Palmeiras', 'Grêmio', 'Fluminense', 'Santos', 'Corinthians', 'Athletico-PR',
         'Ceará', 'Bragantino', 'Atlético Goianiensse', 'Sport Recife', 'Vasco da Gama', 'Fortaleza', 'Bahia', 'Goiás', 'Coritiba', 'Botafogo')

print('-=' * 20)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 20)
print(f'Os cinco primeiros são: {times[0:5]}')
print('-=' * 20)
print(f'Os quatro últimos são: {times[16:]}')  # ou times[-4:]
print('-=' * 20)
print(f'Times em ordem alfabética:{sorted(times)} ')
print('-=' * 20)
print(f'O Corinthians está na {times.index("Corinthians")+1}ª posição')
