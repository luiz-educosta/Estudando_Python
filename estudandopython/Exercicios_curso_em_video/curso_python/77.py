"""
77. Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""
lista = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
         'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for c in lista:
    print(f'\nNa palavra {c.upper()} temos ', end='')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
