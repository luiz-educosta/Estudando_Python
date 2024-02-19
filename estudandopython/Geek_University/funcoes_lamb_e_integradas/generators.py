""""
Generators

Em aulas anteriores nós estudamos:
 - List Comprehension;
 - dictionary Comprehension;
 - Set Comprehension;

Não vimos:
 - Tuple Comprehension... porque elas se chama Generators

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Zorilda']

# List Comprehension
res = [nome[0] == 'C' for nome in nomes]
print(type(res))

# Generators
# Ocupa menos recurso em memória, mais performático
res = (nome[0] == 'C' for nome in nomes)
print(type(res))


# Qual a utilidade de getsizeof()? -> Retorna a quantidade de bytes em memória do elemento passado como parâmetro 
# from sys import getsizeof

# Mostra quantos bytes a string 'Geek' está ocupando em memória. Quanto maior a string, mais espaço ocupa.
print(getsizeof('Geek'))

print(getsizeof('University'))

print(getsizeof(9))

print(getsizeof(91))

print(getsizeof(92345668823))

print(getsizeof(True))
"""
from sys import getsizeof

# Gerando uma lista de números com List Comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista de números com set Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de números com Dictonary Comprehension
dict_comp = getsizeof({x : x * 10 for x in range(1000)})

# Gerando um lista de números com Generator
gen = getsizeof((x * 10 for x in range(1000)))

print('Para fazer a mesma tarefa gastamos em memória: ')
print(f'List Comprehension: {list_comp} bytes')
print(f'Set Comprehension: {set_comp} bytes')
print(f'Dictionary Comprehension: {dict_comp} bytes')
print(f'Generator Expression: {gen} bytes')
