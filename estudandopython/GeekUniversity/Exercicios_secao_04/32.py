"""
32. Leia um número inteiro e imprima a soma do sucessor
de seu triplo com o antecessor de seu drobro.
"""
num = int(input('Digite um número:'))
sucessorDoTriplo = (num * 3) + 1
antecessorDoDobro = (num * 2) - 1
soma = sucessorDoTriplo + antecessorDoDobro
print(f'A soma do sucessor do triplo de {num} com o antecessor de seu dobro é: {soma}')
