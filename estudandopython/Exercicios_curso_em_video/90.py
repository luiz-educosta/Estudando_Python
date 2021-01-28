"""
90. Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
"""
aluno = dict()
aluno['nome'] = str(input('Nome:'))
aluno['media'] = int(input(f'Média de {aluno["nome"]}:'))
if aluno['media'] < 3:
    aluno['situacao'] = 'Reprovado'
elif aluno['media'] <=5:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Aprovado'
print('-=' * 30)

for k, v in aluno.items():
    print(f' - {k} é igual a {v}')