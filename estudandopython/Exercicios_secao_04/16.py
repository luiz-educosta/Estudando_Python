"""
16. Leia um valor de comprimento em polegadas e apresente-o convertido em cintímetros.
A fórmula de conversã é: C = P * 2.54, sendo C o comprimento em centimetros e P o
comprimento em polegadas.
"""
polegadas = float(input('Digite um comprimento em polegadas:'))
centi = polegadas * 2.54
print(f'O valor em centimetros de {polegadas} é {centi} centimetros')
