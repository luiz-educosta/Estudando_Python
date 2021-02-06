"""
107. Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
"""
def aumentar(n = 0, taxa = 0, converte = False):
    res = n + (n * taxa/100)
    return res if converte is False else moeda(res)


def diminuir(n = 0, taxa = 0, converte = False):
    res =  n - (n * taxa/100)
    return res if converte is False else moeda(res)


def metade(n = 0, converte = False):
    res = n / 2
    return res if not converte else moeda(res)  #  Outro jeito de escrever


def dobro(n = 0, converte = False):
    res = n * 2
    return res if not converte else moeda(res)  #  Outro jeito de escrever


def moeda(p = 0, moeda = 'R$'):
    return f'{moeda}{p:>.2f}'.replace('.', ',')

