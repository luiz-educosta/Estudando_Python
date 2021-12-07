"""
17. Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
Calcule e mostre o comprimento da hipotenusa.
"""
from math import sqrt,hypot
oposto = float(input('Digite o comprimento do cateto oposto:'))
adjacente = float(input('Digite o comprimento do cateto adjacente:'))
hipotenua = hypot(oposto, adjacente)
print(f'A hipotenusa vai medir {hipotenua:.2f}')
"""
Poderia utilizar calculando
oposto2 = pow(oposto,2)
adjacente2 = pow(adjacente,2)
hipotenusa = sqrt ((oposto2 + adjacente2))
"""
