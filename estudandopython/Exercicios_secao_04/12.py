"""
12. Leia a distância em milhas e apresente-a convertida em quilômetros.
A foŕmula de conversão é: K = 1.61 * M, sendo K a distância em quilômetros
e M em milhas.
"""

milhas = float(input('Digite a distância em milhas que deseja converter:'))
k = 1.61 * milhas
print(f'A conversão da milha {milhas} em quilômetro é de {k}')
