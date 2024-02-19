"""
Reduce

OBS: A partir do Python3+ a função reduce() não é mais uma função integrada (built-in). 
Agora temos que importar e utilizar essa função a partir do módulo 'functools'.

Guido van Rossum: Utilize a função reduce() se você realmente precisa dela. 
Em todo caso, 99% das vezes um loop for é mais legível.

Para entender o reduce()

# Imagine que vocẽ tem uma coleção de dados:

dados = [a1, a2, a3, ..., an]

def funcao(x, y):
return x * y

Assim como map() e filter, a funcao reduce() recebe dois parâmetros: a função e o iterável.

reduce(funcao, dados)

A função reduce(), funciona da seguinte forma:
    Passo 1: res1 = f(a1, a2)   # Aplica a função nos dois primeiros elementos da coleção e guarda o resultado.
    Passo 2: res2 = f(res1, a3) # Aplica a função passando o resultado do passo1 mais o terceiro elemento e guarda o res.

    Isso é repetido até o final.
    Passo 3: res3 = f(res2, a4)
    .
    .
    .
    Passo n: resn = f(resm, an)

Ou seja, em cada passo ela aplica a função passando como primeiro argumento o resultado da aplicação anterior.
No final, reduce() irá retornar o resultado final.

Alternativamente, poderiamos ver a função reduce() como:

funcao(funcao(funcao(a1, a2), a3), a4), ...), an)

# Dica, lembrar do fatorial
"""

# Como funciona na prática?

# Vamos utilizar a função reduce() para multiplicar todos os números de uma lista

from functools import reduce

dados = [1, 2, 3, 4]

res = reduce(lambda num1, num2: num1 * num2, dados)

print(res)

dados1 = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]

# Para utilizar o reduce() nós precisamos de uma função que receba dois parâmetros

multi = lambda x, y: x * y

res1 = reduce(multi, dados1)

print(res1)


# Utilizando um loop normal

res = 1
for n in dados1:
    res = res * n

print(res)