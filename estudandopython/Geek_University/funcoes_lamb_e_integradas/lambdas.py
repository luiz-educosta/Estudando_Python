"""
Utilizando Lambdas

São funções sem nome, ou seja, funções anônimas.

lambda entrada: retorno da expressão

# Funções em Python

def funcao(x):
    return 3 * x + 1

print(funcao(4))

# Expressão Lambda
lambda x: 3 * x + 1

# Como utilizar a expressão lambda?
calc = lambda x: 3 * x +1

print(calc(7))


# Podemos ter expressões lambdas com múltiplas entradas

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo(' luiz ', ' eDUARDO'))



# Em funções python, podemos ter nenhuma ou várias entradas. Em lambda também.

amar = lambda: 'Como não amar Python?'

uma = lambda x: 3 * x + 1

duas = lambda x, y: (x * y) ** 0.5

tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)

# n = lambda x1, x2, ..., xn <expressão>

print(amar())
print(uma(6))
print(duas(5, 7))
print(tres(3, 6, 9))


# Outro exemplo

autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clake', 'Frank Herbert', 'Orson Scott Card', 
           'Douglas Adams', 'H. G. Wells', 'Leigh Brackett']

# key é a chave para ordenação, a forma como vai ordenar
autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(autores)


"""


# Função Quadrática
# f(x) = ax² + bx + c

# Definindo a função

def geradora_funcao_quadratica(a, b, c):
    """Retorna a função f(x) = ax² + 2bx + c"""
    return lambda x: a * x ** 2 + b * x + c


quadratica = geradora_funcao_quadratica(2, 3, -5)

print(quadratica(0))
print(quadratica(1))
print(quadratica(2))

# outra forma de utilizar
print(geradora_funcao_quadratica(3, 0, 1)(2))

# Aplicações:
# Filtragem e ordenação de dados