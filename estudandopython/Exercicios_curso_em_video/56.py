"""
56. Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
"""
somaIdade = 0
menorVinte = 0
maisVelho = 0
nome = ''
mediaIdade = 0
for c in range(1, 5):
    print('-' * 5, end='')
    print(f'{c}ª pessoa', end='')
    print('-' * 5)
    nome = str(input('Nome:')).strip()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]:')).strip()
    somaIdade += idade
    if sexo in 'Ff' and idade < 20:
        menorVinte += 1
    if c == 1 and sexo in 'Mm':
        maisVelho = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maisVelho:
        maisVelho = idade
        nomeVelho = nome
mediaIdade = somaIdade / 4
print(f'A media de idade do grupo é de {mediaIdade:.1f} anos')
print(f'O homem mais velho tem {maisVelho} anos e se chama {nomeVelho}')
print(f'Ao todo são {menorVinte} mulheres com menos de 20 anos.')
