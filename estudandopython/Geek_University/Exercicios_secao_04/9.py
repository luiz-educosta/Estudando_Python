"""
9. Leia uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin.
A fórmula de conversão é: K = C + 273.15, sendo K a temperatura em Kelvin
e C a temperatura em Celsius.
"""
celsius = float(input('Digite a temperatura em graus Celsius:\n'))
kelvin = celsius + 273.15
print(f'A temperatura {celsius} em graus celsius corresponde a {kelvin} graus Kelvin')
