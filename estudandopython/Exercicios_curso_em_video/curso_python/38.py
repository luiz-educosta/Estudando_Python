"""
38. Escreva um programa que leia dois números inteiros e compare-os. 
Mostrando na tela uma mensagem:

– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais

"""
n1 = float(input('Digite o PRIMEIRO número: '))
n2 = float(input('Digite o SEGUNDO número:'))

if n1 > n2:
    print('O PRIMEIRO número é maior!')
elif n2 > n1:
    print('O SEGUNDO número é maior!')
else:
    print('Os dois números são iguais!')
