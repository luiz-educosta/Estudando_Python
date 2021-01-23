"""
71. Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""
print('=' * 40)
print('BRANCO CEV')
print('=' * 40)

valor = int(input('Qual valor você quer sacar? R$'))
total = valor
ced = 50
totalced = 0
while True:

    #  Verificando quantas vezes consegue tirar 50
    if total >= ced:
        total -= ced  # tirando a cédula até acabar
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} células de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0  # pois mudou o valor da nota
        if total == 0:
            break

print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
