"""
37. Faça um programa que leia o valor de um produto e imprima o valor com desconto,
tendo em vista que o desconto foi de 12%.
"""
valorInicial = float(input('Digite o valor de um produto: R$'))
desconto = valorInicial * 0.88
print(f'O Produto que custa R${valorInicial:.2f} com 12% de desconto sai a R${desconto:.2f}.')
