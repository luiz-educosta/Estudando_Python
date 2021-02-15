"""
40. Uma empresa contrata um encanador a R$30,00 por dia. Faça um programa que solicite
o número de dias trabalhados pelo encanador e imprima a quantia líquida que deverá ser
paga, sabendo-se que são descontados 8% para imposto de renda
"""
diasTrabalhados = int(input('Digite o número de dias trabalhados:'))
total = (diasTrabalhados * 30) * 0.92
print(f'O encanador vai receber uma quantia de R${total}.')
