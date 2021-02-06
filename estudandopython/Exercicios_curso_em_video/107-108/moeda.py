"""
107. Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
"""
def aumentar(n = 0, taxa = 0): 
    return n + (n * taxa/100)


def diminuir(n = 0, taxa = 0):
    return n - (n * taxa/100)


def metade(n = 0):
    met = n / 2
    return met


def dobro(n = 0):
    dob = n * 2
    return dob

def moeda(p = 0, moeda = 'R$'):
    return f'{moeda}{p:>.2f}'.replace('.', ',')