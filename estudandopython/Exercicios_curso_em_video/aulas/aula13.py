for c in range(0, 6):
    print('Oi')
print('FIM!')

for c in range(6, 0, -1):
    print(c)

for c in range(0, 7, 2):
    print(c)

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

for c in range(i, f + 1, p):
    print(c)
print('FIM!')
