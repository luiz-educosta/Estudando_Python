teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
"""
galera . append(teste) tem que se fazer uma cópia, se não, se mudar uma estrutura, muda a outra, exemplo embaixo

galera.append(teste)
print(galera)
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)
print(galera)  # fim do exemplo
"""
#  Caso ideal
galera.append(teste[:])
print(galera)
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print('Exemplo varrendo a lista de galera')
print(galera)
print(galera[0])
print(galera[0][0])
print('Exemplo for')
for pessoa in galera:
    #  print(pessoa) para a lista de forma uma em baixo da outra
    #  print(pessoa[0]) para só os nomes
    #  print(pessoa[1]) para a iade
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade')

galera = list()
dado = list()

for c in range(0, 3):
    dado.append(str(input('Nome:')))
    dado.append(int(input('Idade:')))
    galera.append(dado[:])
    dado.clear()
print(galera)
print('Verificando maior de idade:')
totmaior = totmenor = 0
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmenor += 1
print(f'Temos {totmaior} maiores e {totmenor} menores de idade')
