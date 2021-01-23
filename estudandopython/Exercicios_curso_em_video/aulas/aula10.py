"""
tempo = int(input('Quantos anos tem seu carro?'))
if tempo <= 3:
    print('Carro novo!')
else:
    print('Carro velho')
print('--Fim--')

ou então condição simplificada
tempo = int(input('Quantos anos tem seu carro?'))
print('Carro novo!' if tempo <=3 else 'carro velho')
print('--Fim--')
"""
"""
nome = str(input('Qual é seu nome?'))
if nome == 'Luiz':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print(f'Bom dia, {nome}!')
"""
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print(f'A sua média foi {m:.1f}')

if m >= 6.0:
    print('Sua média foi boa, parabéns!')
else:
    print('Sua média foi ruim!Estude mais!')
