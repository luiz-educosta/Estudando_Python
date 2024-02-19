"""
Documentando funções com Docstrings

OBS: Podemos ter acesso á documentação de uma função em Python utilizando a propriedade especial __doc__

Podemos ainda fazer acesso á documentação com a função help()
"""

def diz_oi():
    """Uma função simples que retorna a string 'Oi!'"""
    return 'Oi!'

print(diz_oi())
help(diz_oi)

def exponencial(numero, potencia=2):
    """
    """