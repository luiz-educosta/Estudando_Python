"""
27. Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente.
"""
nome = str(input('Digite seu nome completo:')).strip().split()

print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {nome[0]}')
print(f'Seu ultimo nome é {nome[len(nome)-1]}')
"""
nome.reverse()
print(f'Seu último nome é {nome[0]}')

"""
