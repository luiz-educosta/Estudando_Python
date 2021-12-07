"""
57. Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""
sexoValido = 1
while sexoValido != 0:
    # separando e pegando a primeira letra
    sexo = str(input('Informe seu sexo: [M/F]:')).strip()[0]
    if sexo in 'FfmM':
        sexoValido = 0
    else:
        print('Dados inválidos. Por favor, informe seu sexo corretamente!')
print(f'Sexo {sexo.upper()} registrado com sucesso!')
# exemplo do curso
sequiso = str(input('Informe seu sexo: [M/F]:')).strip().upper()[0]
while sexo not in 'MmFf':
    sequiso = str(
        input('Dados inválidos. Por favor, informe seu sexo:').strip().upper()[0])
print(f'Sexo {sexo.upper()} registrado com sucesso!')
