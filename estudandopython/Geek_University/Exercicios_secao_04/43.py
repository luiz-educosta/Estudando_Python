"""
43. Escreva um programa de ajuda para vendedores. A partir de um valor lido, mostre:
*O total a pagar com desconto de 10%;
*O valor de cada parcela, no parcelamento  de 3x sem juros;
*A comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto)
*A comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total)
"""
valor = float(input('Digite o valor da compra R$'))
desconto = valor * 0.9
parcela = valor / 3
comissaoVista = desconto * 0.05
comissaoParcelada = valor * 0.05
print(f'* O valor a pagar com desconto de 10% é R${desconto:.2f};')
print(f'* O valor de cada parcela, no parcelamento de 3x sem juros é de R${parcela:.2f};')
print(f'* A comissão do vendedor se a venda for a vista é de R${comissaoVista:.2f};')
print(f'* A comissão do vendedor se a venda for parcelada é de R${comissaoParcelada:.2f}')
