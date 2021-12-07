""" 
Variáveis Compostas [listas]
LISTAS: Uma váriavel que guarda varios valores
Os elementos são indicados por indices, começando a partir do 0 e por ai vai

lista.appende('item que quer adicionar') adiciona no final
lista.insert(0,'item que quer adicionar')

apagar elementos e refaz os indices, ou seja se apagar o 3, o 4 vai pro 3, o 5 por ai vai

del lista[coloca o numero do elemento ex: 3]
lista.pop(coloca o numero do elemento ex: 3)
lista.remove('nome do item')
lanche.pop() remove o último elemento


****** AS LISTAS SÃO MUTÁVEIS!!! ******
"""
valores = list(range(4, 11))
print(valores)

#  organiza os valores
valores.sort()

#  organiza de traz pra frente
valores.sort(reverse=True)

num = [2, 5, 9, 1]
num[2] = 88
num.append(7)
num.sort()
num.insert(0, 99)
num.pop(2)
print(num)
print(f'Essa lista tem {len(num)} elementos.')

valores = list()
valores.append(5)
valores.append(9)
valores.append(4)

for c in valores:
    print(f'{c}...', end='')
print('Cheguei ao final da lista')

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')

"""
valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print(valores)
"""
a = [2, 3, 4, 7]
b = a
#  se trocar o valor de b[2] = 8, o python linca as duas listas
#  dai o valor vai par as duas
#  Para criar a cópia tem que colocar [:]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
