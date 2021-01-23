"""
44. Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar
subindo a escada. Calcule e mostre quantos degraus o usuário deverá subir para atingir
seu objetivo.
"""
altura = float(input('Digite a altura do degrau de uma escada em metros:'))
alturaSubir = int(input('Digite a altura em metros que você deseja subir:'))
objetivo = alturaSubir / altura
print(f'Para você subir {alturaSubir:.2f} metros, será necessário subir {objetivo} degraus')
