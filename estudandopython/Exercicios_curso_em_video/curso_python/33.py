"""
33. Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
if n1 < n2 and n1 < n3:
    menor = n1
if n1 > n2 and n1 > n3:
    maior = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n2 > n1 and n2 > n3:
    maior = n2
if n3 < n1 and n3 < n2:
    menor = n3
if n3 > n1 and n3 > n2:
    maior = n3
print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digiado foi {maior}')