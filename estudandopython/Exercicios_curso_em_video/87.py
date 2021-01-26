"""
87. Aprimore o desafio anterior, mostrando no final:  
A) A soma de todos os valores pares digitados.      
B) A soma dos valores da terceira coluna.     
C) O maior valor da segunda linha. 
"""
somapar = somaterceira = maior = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linhas in range(0, 3):
    for colunas in range(0, 3):
        matriz[linhas][colunas] = int(
            input(f'Digite um valor para [{linhas}, {colunas}]: '))
print('=-' * 30)
for linhas in range(0, 3):
    for colunas in range(0, 3):
        print(f'[{matriz[linhas][colunas]:^5}]', end='')
        #  Verificando se é par
        if matriz[linhas][colunas] % 2 == 0:
            somapar += matriz[linhas][colunas]

        #  valor maior da segunda linha
        if len(matriz) == 0:
            maior = matriz[1][colunas]
        if matriz[1][colunas] > maior:
            maior = matriz[1][colunas]

    #  Somando  valores da terceira coluna
    somaterceira += matriz[linhas][2]
    print()
print('=-' * 30)
print(f'A soma dos valores pares é {somapar}.')
print(f'A soma dos valores da terceira coluna é {somaterceira}')
print(f'O maior valor da segunda linha é {maior}')
