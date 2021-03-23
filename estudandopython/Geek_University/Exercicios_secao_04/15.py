"""
15. Leia um ângulo em radianos e apresente-o convertido em graus. A fórmula de conversão
é: G = R * 180/Pi, sengo G o ângulo em graus e R em radianos e Pi = 3.14.
"""
rad = float(input('Digite um ângulo em radianos:'))
graus = rad * 180 / 3.14
print(f'O ângulo {rad} radianos corresponde a {graus} graus.')
