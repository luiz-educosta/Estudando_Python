"""
105. Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
– Quantidade de notas 
    – A maior nota
        – A menor nota
            – A média da turma
                – A situação (opcional)
"""

def notas (*n, sit = False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    turma = {}
    maior = menor = media = tot = saldo = 0
    for valor in n:
        if tot == 0:
            maior = valor
            menor = valor
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor
        tot += 1
        saldo += valor
    media = saldo / tot

    turma['total'] = tot
    turma['maior'] = maior
    turma['menor'] = menor
    turma['media'] = media
    if sit == True:
        if media < 4:
            turma['situacao'] = 'RUIM'
        elif media > 4 and media < 7:
            turma['situacao'] = 'RAZOAVEL'
        else:
            turma['situação'] = 'BOA'
    
    return turma


#  Programa Principal
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
help(notas)