"""
6. Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit.
A fórmula de conversão é: F = C*(9.0/5.0) + 32.0, sendo F a temperatura em Fahrenheit
e C a temperatura em Celsius.
"""
celsius = float(input('Digite a temperatura em Celsius:'))
fahrenheit = (celsius * (9.0/5.0)) + 32.0
print(f'A temperatura correspondente de {celsius} Celsius em Fahrenheint é: {fahrenheit}')
print(type(fahrenheit))
print(type(celsius))