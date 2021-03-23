"""
8. Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius.
A fórmula de conversão é: C = K - 273.15 , sendo K a temperatura em Kelvin
e C a temperatura em Celsius.
"""
kelvin = float(input('Digite a temperatura em Kelvin:\n'))
celsius = kelvin - 273.15
print(f'A temperatura Kelvin {kelvin} corresponde a {celsius} graus Celsius')
