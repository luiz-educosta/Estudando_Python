""" 
Variáveis Compostas (Tuplas)
Tupla: Uma váriavel que guarda varios valores
Os elementos são indicados por indices, começando a partir do 0 e por ai vai

[-1]mostra o ultimo item da lista, do negativo vai diminuindo

for c in lanche:
    print(c)

****** AS TUPLAS SÃO IMUTÁVEIS!!! ******
"""
# CRIANDO TUPLA
lanche = ('Hambúrger', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(lanche)
print(lanche[1])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[:-2])

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')

print(len(lanche))

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba!')

#  Lanche em ordem
print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b  # diferente de b + a
print(c)
print(c.count(5))  # quantas vezes aparece o número 5
#  print(c.index(3))  # Posição do número
print(c.index(5, 1))  # Vẽ o número 5 a partir da posição 1

pessoa = ('Gustavo', 39, 'M', 99.88)
del(pessoa)  # Apaga da memória
#  print(pessoa)
