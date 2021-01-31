""""
94. Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas 
B) A média de idade 
C) Uma lista com as mulheres 
D) Uma lista de pessoas com idade acima da média
"""
lista = list()
dados = dict()

tot = media = 0

while True:
    dados.clear()


    #  Nome
    dados['nome'] = str(input('Nome:'))


    #  Sexo
    dados['sexo'] = str(input('Sexo: [M/F]')).upper().split()[0]
    while dados['sexo'] not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F.')
        dados['sexo'] = str(input('Sexo: [M/F]')).upper().split()[0]

    """
    poderia ter feito para o sexo e para a pergunta de continuar:
    while true:
        dados['sexo'] = str(input('Sexo: [M/F]')).upper().split()[0]
        if dados['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    """
    #  Idade
    dados['idade'] = int(input("Idade:"))
    tot += dados['idade']

    lista.append(dados.copy())
    
    #  Dúvida
    continua = str(input('Quer continuar? [S/N]')).upper().split()[0]
    while continua not in 'SN':
        print('ERRO! Responda apenas S ou N.')
        continua = str(input('Quer continuar? [S/N]')).upper().split()[0]
    if continua == 'N':
        break


#  Média
media = tot / len(lista)


print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
print(f'B) A media de idade é de {media:.2f} anos')

print(f'C) As mulheres cadastradas foram ', end='')
for p in lista:
    if p['sexo'] == 'F':
        print(p['nome'], end=' ')
print()

print(f'D) Lista das pessoas que estão acima da média:')
for p in lista:
    if p['idade'] >= media:
        print(f'nome = {p["nome"]}; sexo = {p["sexo"]}; idade = {p["idade"]}')

"""
poderia ter usado também:
for p in lista:
    if p['idade'] >= media:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
"""
print('<< ENCERRADO >>')
   