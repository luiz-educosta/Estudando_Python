"""
39. Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""
from datetime import date

anoNascimento = int(input('Ano de nascimento:'))
anoAtual = date.today().year
idade = anoAtual - anoNascimento
print(f'Quem nasceu em {anoNascimento} tem {idade} anos em {anoAtual}.')

anoAlistamento = anoNascimento + 18
diferenca = anoAtual - anoAlistamento
diferenca2 = anoAlistamento - anoAtual

if idade < 18:
    diferenca = anoAlistamento - anoAtual
    print(f'Ainda faltam {diferenca} anos para o alistamento')
    print(f'Seu alistamento será em {anoAlistamento}')
elif idade > 18:
    diferenca = anoAtual - anoAlistamento
    print(f'Você já deveria ter alistado há {diferenca} anos')
    print(f'Seu alistamento foi em {anoAlistamento}')
else:
    print('VocÊ tem que se alistar IMEDIATAMENTE!')
