"""
Interrompendo repetições While.
utilizando o comando break
"""
n = s = 0
while True:  # Loop infinito
    n = int(input('Digite um número: '))
    if n == 999:
        break  # Sai do loop
    s += n
print(f'A soma vale {s}')

# Curiosidade
nome = 'José'
idade = 33
print(f'O {nome:^20} tem { idade} anos')  # :^20 centralizar e colocar no meio
#  (:->) alinha a direita, (:-<) alinha a esquerda
