"""
64. Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
"""
cont = soma = num = 0
num = int(input('Digite um número [999 para parar]:'))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]:'))

print(f'Você digitou {cont} números e a soma entre eles foi {soma}.')
