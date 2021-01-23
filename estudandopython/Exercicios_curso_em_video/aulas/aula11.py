"""
ANSI escape sequence
\033[style:text:back m
ex: \033[0:33:44m

style:
0 = None
1 = Negrito(bold)
4 = Sublinhar (underline)
7 = Negative

text:
30 = Branco
31 = Vermelho
32 = Verde
33 = Amarelo
34 = Azul
35 = Magenta
36 = Ciano
37 = Cinza

Background:
40 = Branco
41 = Vermelho
42 = Verde
43 = Amarelo
44 = Azul
45 = Magenta
46 = Ciano
47 = Cinza

fundo vermelho e letra branca = \033[0:30:41m
fundo azul, letra sublinhada e letra amarelo = \033[4:33:44m
fundo amarelo, letra negrito e letra roxa = \033[1:35:43m
fundo verde letra branca = \033[30:42m
fundo preto e letra cinza = \033[m volta pro padrão do terminal
letra preta e fundo branco = \033[7:30m
"""
print('\033[7;33;44mOlá, Mundo!\033[m')
a = 3
b = 5
print(f'Os valores são \033[32m{a}\033[m e \033[31m{b}\033[m!!!')

nome = 'Luiz Eduardo'
cores = {'Limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
#  print(f"Olá! Muito prazer em te conhecer, {cores['amarelo'] nome }!!!")  # Faltou colocar as cores em python 3.8

x = 'curso de python no curso em video'
print(x[:5])
s = 'prova de python'
print(len(s))
