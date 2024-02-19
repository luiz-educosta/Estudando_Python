tupla = (1, 2, 3)

print(tupla[1])

# Named Tuple -> São tupla diferenciadas, onde, especificamos um nome para a mesma e também parâmetros.

from collections import namedtuple

# Precisa definir nome e parâmetros.

# Forma 1 - Declaração Named Tuple

cachorro1 = namedtuple('cachorro1', 'idade raca nome')

# Forma 2 - Declaração Named Tuple

cachorro2 = namedtuple('cachorro2', 'idade, raca, nome')

# Forma 3 - Declaração Named Tuple

cachorro3 = namedtuple('cachorro2', ['idade', 'raca', 'nome'])

# Usando

ray = cachorro3(idade=2, raca='Chow-Chow', nome='Ray')

# Acessando os dados
print(ray)
print(ray.idade) # ou ray[0]

print(ray.index('Chow-Chow'))
print(ray.count('Chow-Chow'))