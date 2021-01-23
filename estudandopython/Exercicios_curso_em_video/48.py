"""
48. Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
"""
cont = 0
soma = 0
for c in range(1, 500):  # ou então coloca range (1, 500, 2)
    if not c % 2 == 0 and c % 3 == 0:
        soma = soma + c  # ou soma += c
        cont = cont + 1  # ou cont+= 1

print(f'A soma de todos os {cont} valores solicitados é {soma}.')
