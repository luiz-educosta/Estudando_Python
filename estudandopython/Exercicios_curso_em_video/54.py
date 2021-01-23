"""
54. Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""
from datetime import date
contM = 0
contm = 0
for c in range(1, 8):
    ano = int(input(f'Em que ano a {c}ª pessoa nasceu?'))
    if (date.today().year) - ano >= 18:
        contM += 1
    else:
        contm += 1
print(f'Ao todo tivemos {contM} pessoas maiores de idade.')
print(f'E também tivemos 4 pessoas menores de idade.')
