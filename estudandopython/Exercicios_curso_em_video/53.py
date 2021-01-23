"""
53. Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
"""
frase = str(input('Digite uma frase:')).strip().upper().split()
junto = (''.join(frase))
invertida = ''
for letra in range(len(junto) - 1, -1, -1):
    invertida += junto[letra]
print(f'O inverso de {junto} é {invertida}')
if frase == invertida:
    print('A frase digitada É UM PALÍNDROMO!')
else:
    print('A frase digitada NÃO É UM PALÍNDROMO!')
