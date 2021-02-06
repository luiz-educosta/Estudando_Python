"""
107. Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
"""
def aumentar(n, taxa): 
    return n + (n * taxa/100)


def diminuir(n, taxa):
    return n - (n * taxa/100)


def metade(n):
    met = n / 2
    return met


def dobro(n):
    dob = n * 2
    return dob

 