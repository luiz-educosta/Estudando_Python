"""
74. Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
"""
from random import randint

sorteados = []
for c in range(0, 5):
    sorteados.append(randint(0, 10))
    if c == 0:
        maior = sorteados[c]
        menor = sorteados[c]
    if sorteados[c] > maior:
        maior = sorteados[c]
    if sorteados[c] < menor:
        menor = sorteados[c]

print(f'Os valores sorteados foram: {sorteados}')
print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')

#  Solução do prof
numeros = (randint(1, 10), randint(1, 10), randint(1, 10),
           randint(1, 10), randint(1, 10))

print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')
