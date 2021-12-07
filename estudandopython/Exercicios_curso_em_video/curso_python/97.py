"""
97. Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.                                  Ex:                                                                                                                                                                        escreva(‘Olá, Mundo!’) Saída:                                                                                                                          ~~~~~~~~~                                                                                                                                                            Olá, Mundo!                                                                                                                                                          ~~~~~~~~~                                                                          
"""

def escreva(msg):
    pos = 0
    while pos < len(msg):
        print('~', end='')
        pos += 1
    print()
    print(msg)
    pos = 0
    while pos < len(msg):
        print('~', end='')
        pos += 1
    print()
    print()


"""
Poderia fazer assim:

def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)

"""
#  Programa principal
escreva('Luiz Eduardo')
escreva('Curso de Python')
escreva('Python')
