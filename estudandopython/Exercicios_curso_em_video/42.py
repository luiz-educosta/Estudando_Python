"""
42. Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes
"""
r1 = float(input('Primeiro segmento:'))
r2 = float(input('Segundo segmento:'))
r3 = float(input('Terceiro segmento:'))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('Os segmentos podem formar um triângulo!', end='')
    if r1 == r2 == r3:
        print('Triângulo EQUILÁTERO!')
    elif r1 == r2 or r1 == r3 or r3 == r2:
        print('Triângulo ISOSCELES!')
    else:
        # Poderia colocar como elif r1 != r2 != r3 != r1
        print('Triângulo ESCALENO!')
else:
    print('Os segmentos acima não podem formar triângulo!')
