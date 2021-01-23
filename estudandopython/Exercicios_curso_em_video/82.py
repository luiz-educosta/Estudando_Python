"""
82. Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
"""
lista = []
listaPar = []
listaImpar = []
continua = ' '
while True:
    n = int(input('Digite um número:'))
    lista.append(n)
    if n % 2 == 0:
        listaPar.append(n)
    else:
        listaImpar.append(n)
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N]')).upper().strip()[0]
