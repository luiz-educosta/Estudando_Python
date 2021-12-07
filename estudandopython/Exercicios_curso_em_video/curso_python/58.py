"""
58. Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
"""
from random import randint
print("""Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?""")
computador = randint(0, 10)
palpite = int(input('Qual é o seu palpite?'))
tentativa = 0
while palpite != computador:
    if palpite > computador:
        print('Menos... Tente mais uma vez.')
    if palpite < computador:
        print('Mais.. Tente mais uma vez.')
    palpite = int(input('Qual é o seu palpite?'))
    tentativa += 1
print(f'Acertou em {tentativa} tentativas. Parabéns!')
