"""
7. Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.
A fórmula de conversão é: C = 5.0 * (F - 32.0)/9.0, sendo F a temperatura em Fahrenheit
e C a temperatura em Celsius.
"""
fahrenheit = float(input('Digite a temperatura em Fahrenheit:\n'))
celsius = 5.0 * (fahrenheit - 32.0) / 9.0
print(f'A temperatura {fahrenheit} graus Fahrenheit é o equivalente a {celsius} graus Celsius')
