"""
59. Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
"""
from time import sleep
soma = 0
mult = 0
n1 = int(input('Primeiro valor:'))
n2 = int(input('Segundo valor:'))
print("""[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] sair do programa""")
opcao = int(input('Qual é a sua opção?'))
while opcao != 5:

    #  print('Você digitou um número errado, por favor digite novamente')
    if opcao == 1:
        soma = n1 + n2
        print(f' A soma entre {n1} + {n2} é {soma}')

    elif opcao == 2:
        mult = n1 * n2
        print(f'A multiplicação ente {n1} X {n2} é {mult}')

    elif opcao == 3:
        if n1 > n2:
            print(f'O número {n1} é maior.')
        else:
            print(f'O número {n2} é maior.')

    elif opcao == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor:'))
        n2 = int(input('Segundo valor:'))
    else:
        print('Opção inválida. Tente novamente!')

    print('=-=' * 9, end='')
    sleep(2)
    print("""
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] sair do programa""")
    print('=-=' * 9)
    opcao = int(input('Qual é a sua opção?'))
print('Finalizando...')
sleep(3)
print('=-=' * 9)
