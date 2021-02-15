"""
35. Faça um programa que receba os valores de a e b e calcule o valor da hipotenusa através da equação:
hipotenusa = raiz(((a²) + (b²)))
"""
a = int(input('Para calcular o valor da hipotenuza digite o valor de a:'))
b = int(input('Para calcular o valor da hipotenuza digite o valor de b:'))
a2 = a ** 2
b2 = b ** 2  # ou se não pode ser pow(b,2)
soma = a2 + b2
hipotenusa = soma ** (1/2)
print(f'O valor da hipotenusa de {a:.3f} com {b:.3f} é {hipotenusa:.3f}')  # Colocando limite para mostrar

