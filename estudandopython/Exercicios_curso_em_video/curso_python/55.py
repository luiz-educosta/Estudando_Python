"""
55. Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
"""
menor = 0
maior = 0
for c in range(1, 6):
    peso = float(input(f'Digite o peso da {c}ª pessoa:'))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso < menor:
            menor = peso
        if peso > maior:
            maior = peso
print(f'O maior peso lido foi de {maior:.1f}kg')
print(f'O menor peso lido foi de {menor:.1f}kg')
