def quadrado_de_7():
    return 7 * 7

ret = quadrado_de_7()

print(f'Retorno {ret}')

# Podemos, em uma função, retornar qualquer tipo de dado e até mesmo múltiplos valores

def outra_funcao():
    return 2, 3, 4, 5

num1, num2, num3, num4 = outra_funcao()

print(num1, num2, num3, num4)
print(outra_funcao())

# função para jogar a moeda

from random import random

def joga_moeda():
    # Gera um número pseudo-randômico entre 0 e 1
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'

print(joga_moeda())