"""
Map

Com map, fazemos mapeamento de valores para função.


import math

def area(r):
    ""Calcula a área de um círculo com raio 'r'.""
    return math.pi * (r ** 2)

print(area(2))
print(area(5.13))

raios = [2, 5, 7.1, 0.3, 10, 44]

# Forma comum
areas = []
for r in raios:
    areas.append(area(r))

print(areas)

# Forma 2 - Map

# Map é uma função que recebe dois parâmetros: O primeiro a função, o segundo um iterável. Retorna um Map Object

areas = map(area, raios)

print(areas)
print(type(areas))
print(list(areas)) # Poderia ser list, tuple


# Forma 3 - Map com lambda

areas1 = map(lambda r: math.pi * (r ** 2), raios)

print(list(areas1))


# OBS.: Após utilizar a função map() depois da primeira utilização do resultado, ele zera
# Exemplo, esses dois de baixo não mostram
for n in areas1:
    print(n)

for n in areas1:
    print(n)   
"""

# Mais um exemplo

# transformando em Fahrenheit

cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 29), ('Los Angeles', 26), ('Tokio', 27), ('Nova York', 28), 
           ('Londres', 22)]

def convert_fahrenheit(dado):
    """Calcula a temperatura em fahrenheit"""
    return (dado[1] * 9/5) + 32

cidades_fahrenheit = map(lambda dado: (dado[0], (dado[1] * 9/5) + 32), cidades)

print(cidades)
print(list(cidades_fahrenheit))