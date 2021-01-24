"""
84. Faça um programa que leia nome e peso de várias pessoas,        guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas. 
B) Uma listagem com as pessoas mais pesadas.  
C) Uma listagem com as pessoas mais leves.
"""
dados = []
pessoas = []
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]

    pessoas.append(dados[:])
    dados.clear()
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N]')).upper().split()[0]
    if continua == 'N':
        break

print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior:.1f}Kg. Peso de ', end='')
for peso in pessoas:
    if peso[1] == maior:
        print(f'{peso[0]}', end=' ')
print(f'\nO menor peso foi de {menor:.1f}kg.Pedo de ', end='')
for peso in pessoas:
    if peso[1] == menor:
        print(f'{peso[0]}', end=' ')
