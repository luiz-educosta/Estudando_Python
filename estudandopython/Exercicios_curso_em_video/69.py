"""
68. Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.
"""

contIdade = contMulher = contMasculino = 0
while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade:'))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    if idade >= 18:
        contIdade += 1
    if sexo == 'F' and idade < 20:
        contMulher += 1
    if sexo == 'M':
        contMasculino += 1
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continua == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {contIdade}')
print(f'Ao todo temos {contMasculino} homens cadastrados.')
print(f'E temos {contMulher} mulheres com menos de 20 anos')
