"""
61.  Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
"""

#  Essa resolução é mais facíl
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Digite o primeiro termo:'))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(termo, end=' -> ')
    termo += razao
    cont += 1
"""
c = 0
num = 0
print('Gerador de PA')
print('-=' * 10)
termo = int(input('Digite o primeiro termo:'))
razao = int(input('Razão da PA: '))
decimo = termo + ((10 - 1) * razao)

while termo <= decimo:
    print(termo, end=' -> ')
    termo = termo + razao
print('Fim')

"""
