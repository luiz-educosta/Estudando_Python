"""
Any e all

all() "TODOS" Tipo função "E"  -> Retorna True se todos os elementos do iterável são verdadeiros ou ainda se o iterável está vazio.
any() "ALGUM" Tipo função "OU" -> Retorna True se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio, retorna False.

# Exemplo all()

print(all([0, 1, 2, 3, 4, 5])) # Todos os números são verdadeiros? False

print(all([1, 2, 3, 4, 5])) # Todos os números são verdadeiros? True

print(all([])) # Todos os números são verdadeiros? True

print(all((1, 2, 3, 4, 5))) # Todos os números são verdadeiros? True

print(all({1, 2, 3, 4, 5})) # Todos os números são verdadeiros? True

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina'] # Se acrescentar 'Daniel', daria false

print(all([nome[0] == 'C' for nome in nomes]))

# OBS: um iterável vazio convertido em boolean é False, mas o all() entende como True

print(all([letra for letra in 'kkkk' if letra in 'aeiou']))

"""

# Exemplo any()



nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Zorilda'] # Se acrescentar 'Daniel', daria true

print(any([nome[0] == 'C' for nome in nomes]))

print(any([num for num in [1, 3, 5, 9] if num % 2 == 1]))