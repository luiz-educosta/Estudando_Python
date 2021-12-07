"""
92. Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""
from datetime import date
dicionario = dict()
dicionario['nome'] = str(input('Nome:'))
ano = int(input('Ano de nascimento:'))
dicionario['idade'] = date.today().year - ano
dicionario['ctps'] = int(input('Carteira de trabalho (0 não tem):'))
print('-=' * 30)
#  poderia ter posto o for por ultimo
if dicionario['ctps'] == 0:
    for k, v in dicionario.items():
        print(f' - {k} tem o valor {v}')
else:
    dicionario['contratação'] = int(input('Ano de contratação:'))
    dicionario['salario'] = float(input('Sálario: R$'))
    dicionario['aposentadoria'] = dicionario['idade'] + ((dicionario['contratação'] + 35) - date.today().year)
    for k, v in dicionario.items():
        print(f' - {k} tem o valor {v}')