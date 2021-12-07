"""
10. Conversor de dinheiro de R$ em US$.
"""
real = float(input('Quanto dinheiro você tem na carteira? R$ '))
print(f'Com R${real:.2f} você pode comprar US${(real / 3.27):.2f}')
