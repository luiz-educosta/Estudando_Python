"""
95. Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
"""
gol = list()
time = list()
jogador = dict()

while True:
    jogador.clear()

    #  Nome
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))

    #  Gols
    for p in range(0, partidas):
        gol.append(int(input(f'    Quantos gols na partida {p+1}? ')))   
    jogador['gols'] = gol[:]
    jogador['saldo'] = sum(gol)
    

    #  Adicionando ao time
    time.append(jogador.copy())
    gol.clear()


    #  Sai do loop
    while True:
        continua = str(input('Quer continuar? [S/N]')).upper().split()[0]
        if continua  in 'SN': 
            break
        print('ERRO! Por favor, digite apenas S ou N.')
        
    if continua == 'N':
        break
print('-=' * 40)


#  Imprimindo tabela
print(f'{"cod":>3}',f'{"nome":<10}', f'{"gols":^15}', f'{"total":<10}')
print('-' * 40)
"""
poderia ter usado:
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
"""
for k, v in enumerate(time):
    #  Primeiro for é para o número:
    print(f'{k:>4} ', end='')
    #  Segundo for é para imprimir os valores
    for dados in v.values():
        print(f'{str(dados):<15}', end='') 
    print()

print('-' * 40)
#  Consulta dados
while True:
    
    consulta = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if consulta == 999:
        break
    
    if consulta >= len(time):
        print(f'ERRO! Não existe jogador com o código {consulta}!')
    
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[consulta]["nome"]}')

        for i, v in enumerate(time[consulta]["gols"]):
            print(f'No jogo {i + 1} fez {v} gols')
    print('-' * 40)
print("<< VOLTE SEMPRE >>")