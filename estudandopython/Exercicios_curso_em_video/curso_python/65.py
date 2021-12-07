"""
65. Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""
cont = soma = media = maior = menor = 0
continua = 'S'

while continua in 'Ss':
    num = int(input('Digite um número: '))
    cont += 1
    soma += num
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    continua = str(input('Quer continuar? [S/N]')).strip().upper()[0]

media = soma / cont
print(f'Você digitou {cont} números e a média foi {media:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
