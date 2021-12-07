"""
80. Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
"""
lista = []

for c in range(0, 5):
    n = int(input('Digite um valor:'))
    # se o valor for igual ou maior do que o ultimo elemento da lista
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Valor adicionado na posição {pos}')
                break
            pos += 1

print(f'Os valores digitados em ordem foram {lista}')
