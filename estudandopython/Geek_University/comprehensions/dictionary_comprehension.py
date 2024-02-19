"""
Dictionary Comprehension

Pense no seguinte:

 - Se quisermos criar uma tupla:

    tupla = (1, 2, 3, 4) # 1, 2, 3, 4

- Se quisermos criar uma lista fazemos:

    lista = [1, 2, 3, 4]

- Se quisermos criar um set (conjunto):

    conjunto = {1, 2, 3, 4}

- Se quisermos criar um dicionário:

    dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Sintaxe

dicionário = {chave: valor for valor in iterável}
lista = [valor for valor in iterável]

# Exemplos

# 1
numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}

print(quadrado)

# 2
numeros = [1, 2, 3, 4, 5]

quadrados = {valor: valor ** 2 for valor in numeros}

print(quadrados)

# 3
chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}

print(mistura)

# 4 - Exemplos com lógica condicional

numeros = [1, 2, 3, 4, 5]

res = {num: ('par' if num % 2 == 0 else 'ímpar') for num in numeros}

print(res)

"""

