dado = list()
galera = list()
for c in range(0, 3):
    dado.append(str(input('Nome:')))
    dado.append(int(input('Idade:')))
    galera.append(dado[:])
    dado.clear()
print(galera)
print('Verificando maior de idade:')
totmaior = totmenor = 0
for p in galera:
    print(len(galera))
    print(p[1])
    print(len(p))
    print(p)
    """if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmenor += 1"""
print(f'Temos {totmaior} maiores e {totmenor} menores de idade')
