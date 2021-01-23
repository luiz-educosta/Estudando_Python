"""
50. Implemente um programa que calcule o ano de nascimento de uma pessoa a partir de sua idade e do ano atual.
"""
ano = int(input('Digite o ano de nascimento que você nasceu: '))
anoAtual = int(input('Digite o ano atual: '))
idade = anoAtual - ano
print(f'A idade que você tem é {idade} anos')
