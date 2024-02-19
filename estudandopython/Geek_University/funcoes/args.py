"""
Entendendo o *args

- O *args é um parâmetro, como outro qualquer. Isso significa que você poderá 
chamar de qualquer coisa, desde que comece com asterisco.

Exemplo:

*xis

Mas por convenção, utilizamos *args para definí-lo

Mas o que é o *args?

O parâmetro *args utilizado em uma função, coloca os valores extras informados 
como entrada em uma tupla. Então desde já lembre-se que tuplas são imutáveis.


# Exemplo

def soma_todos_numeros(num1, num2, num3):
    return num1 + num2 + num3

print(soma_todos_numeros(4, 6, 9))


# Entendendo o *args

def soma_todos_numeros(*args):
    return sum(args)

print(soma_todos_numeros())
print(soma_todos_numeros(1))
print(soma_todos_numeros(2, 3))

def soma_todos_numeros(nome, email, *args):
    return sum(args)

print(soma_todos_numeros('Luiz', 'Eduardo'))
print(soma_todos_numeros('Luiz', 'Eduardo', 1))
print(soma_todos_numeros('Luiz', 'Eduardo', 2, 3))


def soma_todos_numeros(nome, email, *args):
    return sum(args)

print(soma_todos_numeros('Luiz', 'Eduardo'))
print(soma_todos_numeros('Luiz', 'Eduardo', 1))
print(soma_todos_numeros('Luiz', 'Eduardo', 2, 3))


"""

# Entendendo o *args

def soma_todos_numeros(*args):
    return sum(args)

numeros = [1, 2, 3, 4, 5, 6, 7]

# Desempacotador

# print(soma_todos_numeros(numeros)) # errado

print(soma_todos_numeros(*numeros)) # utilizando o desempacotador

# Obs.: O asterisco serve para que informemos ao Python que estamos 
# passando como argumento uma coleção de dados.
# Dessa forma, ele saberá que precisará antes desempacotar estes dados.