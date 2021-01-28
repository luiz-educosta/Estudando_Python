"""
Variáveis compostas:
Dicionários
São estruturas de dados semelhantes as tuplas e listas, porém consegue ter indices literais.
Tuplas () ou tuple()
listas [] ou list()
dicionários {} ou dict()

remover elementos del
"""
pessoas = {'nome': 'Luiz', 'sexo': 'M', 'idade': 24}
print('pessoas')
print(pessoas)
#  print(pessoas[0]) não funciona
print('Qualquer elemento do dicionário')
print(pessoas['nome'])  # ou qualquer outro elemento do dícionario
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')

print('Keys')
print(pessoas.keys())

print('Values')
print(pessoas.values())

print('Items')
print(pessoas.items())

print('for para keys')
for k in pessoas.keys():
    print(k)

print('for para values')
for v in pessoas.values():
    print(v)

print('for para items')
for i in pessoas.items():
    print(i)

print('Imprimindo a chave e o valor em um for')
for k, v in pessoas.items():
    print(f'{k} = {v}')

#  Apagando algo
#  del pessoas['sexo']

#  Alterando
pessoas['nome'] = 'Isaac'

#  Acrescentando
pessoas['peso'] = 69

#  Criando dicionario dentro de uma lista
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'Rj'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print('Dicionário dentro de uma lista')
print(brasil)
#  print(brasil[0]['uf'])

print('Adicionando três estados')
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado:'))
    #  Metodo sem fatiamento
    brasil.append(estado.copy())
print(brasil)

for e in brasil:
    print(e)

# for de fora é a lista, de dentro é do dicionário
print('Usando o for e items')
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')

print('Usando dois for')
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
