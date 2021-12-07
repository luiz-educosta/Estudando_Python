"""
70. Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.
"""
print('-' * 40)
print(f'LOJA SUPER BARATÃO')
print('-' * 40)
preco = cont = total = menor = cont1 = 0
nomeBarato = nome = ''
while True:

    nome = str(input('Nome do Produto:'))
    preco = float(input('Preço: R$'))
    continua = ' '
    cont1 += 1
    total += preco
    if cont1 == 1 or preco < menor:
        menor = preco
        nomeBarato = nome
    if preco > 1000:
        cont += 1

    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continua == 'N':
        print('FIM DO PROGRAMA')
        break

print(f'O total da compra foi R${total:.2f}.')
print(f'Temos {cont} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomeBarato} que custa R${menor:.2f}')
