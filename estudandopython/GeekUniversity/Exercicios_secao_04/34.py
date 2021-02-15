"""
34. Leia o valor do raio de um circulo e calcule e imprima a área do círculo correspndente.
A área do circulo é Pi * raio², considere Pi = 3.141592.
"""
raio = int(input('Digite o raio para calcular a área do circulo:'))
area = 3.141592 * (raio ** 2)
print(f'A área do circulo cujo raio é {raio} é de {area}')
