"""
Set Comprehension

lista = [1, 2, 3, 4, 5]
set = {1, 2, 3, 4, 5}

"""

# Exemplos

numeros = {num for num in range(1, 7)}

print(numeros)

numeros = {x ** 2 for x in range(10)}

print(numeros)

# DESAFIO: Faça uma alteração na estrutura acima para gerar um dicionário ao invés de set
numeros = {x: x ** 2 for x in range(10)}
print(numeros)

letras = {letra for letra in 'Geek University'}
print(letras)
