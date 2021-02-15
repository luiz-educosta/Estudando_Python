"""
52. Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser retartido proporcionalmente
ao valor que cada deu para a realização da aposta. Faça um programa que leia quanto cada apostador investiu,
o valor do prêmio, e imprima quanto cada um ganharia do prêmio com base no valor investido.
"""
premio = float(input('Digite o valo do prémio R$'))
amigo1 = float(input('Digite a procentagem (%) do primeiro amigo:'))
amigo2 = float(input('Digite a procentagem (%) do segundo amigo:'))
amigo3 = float(input('Digite a porcentagem (%) do terceiro amigo:'))

print(f'O primeiro amigo recebeu a porcentagem {amigo1}% do valor R${premio} e corresponde a R${amigo1 * premio / 100}')
print(f'O segundo amigo recebeu a porcentagem {amigo2}% do valor R${premio} e corresponde a R${amigo2 * premio / 100}')
print(f'O segundo amigo recebeu a porcentagem {amigo3}% o valor R${premio} e corresponde a R${amigo3 * premio / 100}')
