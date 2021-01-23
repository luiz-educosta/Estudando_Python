"""
43. Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida
"""
peso = float(input('Digite o seu pedo em kg:'))
altura = float(input('Digite a sua altura em m:'))
IMC = peso / (altura ** 2)
print(f'A pessoa com a {altura}m e o pedo {peso}kg tem um IMC de {IMC:.1f}')

if IMC <= 18.5:
    print('A pessoa esta abaixo!')
elif IMC <= 25:
    print('A pessoa está em peso ideal!')
elif IMC <= 30:
    print('A pessoa está com sobrepeso!')
elif IMC <= 40:
    print('A pessoa está com Obesidade!')
else:
    print('A pessoa está com Obesidade Mórbida!')
