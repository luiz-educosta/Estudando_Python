"""
18. Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
"""
from math import sin, cos, tan, radians

angulo = float(input('Digite o ângulo que você deseja:'))
angulor = radians(angulo)
print(f'O ângulo de {angulo:.1f} tem o SENO de {sin(angulor):.2f}')
print(f'O ângulo de {angulo:.1f} tem o COSSENO de {cos(angulor):.2f}')
print(f'O ângulo de {angulo:.1f} tem a TANGENTE de {tan(angulor):.2f}')
