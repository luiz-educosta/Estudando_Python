"""
83. Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
"""
pilha = []
expr = str(input('Digite a expressão:'))
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')


if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
