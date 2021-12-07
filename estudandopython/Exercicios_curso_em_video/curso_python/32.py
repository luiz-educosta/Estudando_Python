"""
32. Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
"""
from datetime import date

ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))

if ano == 0:
    #   Verificando ano atual
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO.')
else:
    print(f'O ano {ano} NÃO É BISSEXTO.')
