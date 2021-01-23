"""
62. Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
"""
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo:'))
razao = int(input('Razão da PA: '))
termo = 10
c = 1
status = True
while status:
    while c <= termo:
        print(primeiro, end=' -> ')
        primeiro += razao
        c += 1
    print('PAUSA')

    termo = int(input('Quantos termos você quer demonstrar a mais?'))
    c1 = 0
    if termo == 0:
        status = False
    else:
        while c1 < termo:
            print(primeiro, end=' -> ')
            primeiro += razao
            c1 += 1
            c += 1
print(f'Progressão finalizada com {c - 1} termos mostrados')
# outra resolução
"""
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo:'))
razao = int(input('Razão da PA: '))
termo = primeiro
c = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        print({termo}, end='')
        termo += razao
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais?'))
print('Progressão finalizada com {total} termos mostrados.')
"""
