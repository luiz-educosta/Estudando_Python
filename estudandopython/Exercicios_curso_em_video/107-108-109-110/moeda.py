"""
Para esse exemplo, foi modificado de acordo que era acrescentado as funções ao longo dos exercícios presentes no nome da pasta.
Para ver a parte que se refere ao exercício especifico, recomendo ver os commits com os nomes dos exercícios.
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


def resumo(p = 0, a = 10, d = 5):
    print('-' * 40)
    print(f'{"RESUMO DO VALOR":^40}')  #  Poderia ter usado o .center(30)
    print('-' * 40)
    print(f'Preço analisado: \t{moeda(p)}')
    print(f'Dobro do preço: \t{moeda(dobro(p))}')
    print(f'Metade do preço: \t{moeda(metade(p))}')
    print(f'{a}% de aumento: \t{moeda(aumentar(p, a))}')
    print(f'{d}% de redução: \t{moeda(diminuir(p, d))}')
    print('-' * 40)