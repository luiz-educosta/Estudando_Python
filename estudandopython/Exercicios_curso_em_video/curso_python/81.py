"""
81.  Crie um programa que vai ler vários números e colocar em uma lista.Depois disso, mostre:
A) Quantos números foram digitados.   
B) A lista de valores, ordenada de forma decrescente.  
C) Se o valor 5 foi digitado e está ou não na lista.

"""
lista = []
cont = 0
while True:
    lista.append(int(input('Digite um valor:')))
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if continua == 'N':
        break
print('=-' * 30)
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')
