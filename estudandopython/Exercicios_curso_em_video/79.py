"""
79. Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""
duvida = ' '
v = 0
num = []
while True:

    n = int(input('Digite um valor: '))
    if n not in num:
        num.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar...')
    duvida = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if duvida == 'N':
        break
print('=-' * 40)
num.sort()
print(f'Você digitou os valores {num}')
