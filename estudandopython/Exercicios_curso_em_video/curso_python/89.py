"""
89. Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
"""
from time import sleep
lista = []
dados = []
cont = 0
while True:
    #  Poderia ter pegado e criado n1, n2, media e feito um
    #  ficha.append([nome], [n1]...)
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))

    lista.append(dados[:])
    dados.clear()

    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N]')).upper().split()[0]
    if continua == 'N':
        break
print('-=' * 40)
#  Poderia usar for i, a in enumerate(lista)
print(f'{"No.":<4}', f'{"NOME":<15}', f'{"MEDIA":^5}')
print('-' * 30)
for aluno in lista:
    print(f'{cont:<4}', f'{aluno[0]:<15}', f'{(aluno[1] + aluno[2])/2:^5.1f}')
    cont += 1
print('-' * 30)
while True:
    print('*' * 30)
    aluno = int(input('Mostrar notas de qual aluno? (999 interrompe):'))
    if aluno == 999:
        break
    print(
        f'Notas de {lista[aluno][0]} são [{lista[aluno][1]}, {lista[aluno][2]}]')
print('FINALIZANDO...')
sleep(1)
print('<' * 3, 'VOLTE SEMPRE', '<' * 3)
