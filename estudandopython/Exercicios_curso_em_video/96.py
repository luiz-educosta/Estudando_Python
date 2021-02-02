"""
96. Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
Aula Anterior
"""
def area(l, c):
    area = l * c
    print(f'A área de um terreno {l} X {c} é de {area}m²')


#  Programa principal
print('Controle de Terrenos')
print('-' * 30)
largura = float(input('LARGURA (m):'))
comprimento = float(input('COMPRIMENTO (m):'))
area(largura, comprimento)