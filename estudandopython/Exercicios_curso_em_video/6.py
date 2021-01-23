"""
6 Digitar um número e mostrar o seu dobro, o seu triplo e a sua raiz quadrada
"""
num = int(input('Digite um número:'))
dobro = num*2
triplo = num*3
raizQuadrada = num**(1/2)  # ou então a função pow(base,expoente)
# ai ficaria pow(num,(1/2))

print(f'O dobro do número {num} é {dobro}.')
print(f'O triplo do número {num} é {triplo}.')
print(f'A raiz quadrada de {num} é {raizQuadrada:.2f}.')
