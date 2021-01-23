"""
37.Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
"""
import math
num = int(input('Digite um número inteiro:'))
print('Escolha uma das base para conversão:')
print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
opcao = int(input('Sua opção:'))
if opcao == 1:
    resultado = bin(num)
    print(f'O número {num} tem o seu número binário {resultado[2:]}')
elif opcao == 2:
    resultado = oct(num)
    print(f'O número {num} tem o seu número octal {resultado[2:]}')
elif opcao == 3:
    resultado = hex(num)
    print(f'O número {num} tem o seu número hexadecimal {resultado[2:]}')
else:
    print('VocÊ não escolheu nenhuma das opções, tente novamente.')
