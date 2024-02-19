# try:
#     num = int(input('Informe um número: '))
# except ValueError:
#     print('Valor incorreto')
# else: # É executado somente se não ocorrer o erro.
#     print(f'Você digitou {num}')
# finally: # O bloco finally é SEMPRE executado. Independente se houve exceção ou não.
#     print('Executando o finally')

# # O finally, geralmente é utilizado para fechar ou desalocar recursos.

# Exemplo mais complexo ERRADO

# def dividir(a, b):
#     return a / b

# num1 = int(input('Informe o primeiro número: '))

# try:
#     num2 = int(input('Informe o segundo número: '))
# except ValueError:
#     print('O valor precisa ser numérico')

# try:
#     print(dividir(num1, num2))
# except NameError:
#     print('Valor incorreto')

# print(dividir(num1, num2))


# Exemplo mais complexo CERTO

#OBS: Você é responsável pelas entradas das suas funções. Então, trate-as

def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor incorreto'
    except ZeroDivisionError:
        return 'Não é possível realizar uma divisão por zero'

num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))


# Exemplo mais complexo GENÈRICO

def dividir(a, b):
    try:
        return int(a) / int(b)
    except:
        return 'Ocorreu um problema'

num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))


# Exemplo mais complexo Semi-GENÈRICO

def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'

num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))