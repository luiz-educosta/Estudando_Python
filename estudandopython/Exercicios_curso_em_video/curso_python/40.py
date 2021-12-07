"""
40. Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO
"""
n1 = float(input('Digite a sua primeira nota:'))
n2 = float(input('Digite a sua segunda nota:'))
media = (n1 + n2) / 2

print(f'Quem tirou {n1:.2f} e {n2:.2f} tem a média {media:.2f}')

if media < 5:
    print('VocÊ foi REPROVADO!')
elif media >= 5 and media < 7:
    print('Você está de RECUPERAÇÃO!')
else:
    print('Você foi APROVADO!')
