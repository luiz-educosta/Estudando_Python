"""
14. Leia um ângulo em graus e apresente-o convertido em radianos. A fórmula de conversão
é: R = G * Pi/180, sengo G o ângulo em graus e R em radianos e Pi = 3.14.
"""
graus = float(input('Digite um ângulo em Graus:'))
rad = graus * 3.14 / 180
print(f'O valo correspondente a {graus} graus em radianos é {rad}')
