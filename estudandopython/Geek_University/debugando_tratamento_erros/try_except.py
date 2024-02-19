# Exemplo 1 - tratando um erro genérico
# Tente executar a função geek(), caso você encontre erros, imprima a mensagem de erro.
try:
    geek()
except: # capturar a exceção
    print('Deu algum problema')


# OBS: Tratar erro de forma genérica não é a melhor forma de tratamento de erros. O ideal é SEMPRE tratar de forma específica.
# Exemplo 2 - Tradando um erro específico
try:
    geek()
except NameError:
    print('Você está utilizando uma função inexistente')

# Exemplo 3 - Tratando um erro específico com detalhes do erro
try:
    len(5)
except TypeError as err:
    print(f'A aplicação gerou o seguinte erro: {err}')

# Exemplo 4 - Vários tratamentos de erros de uma vez.

try:
    # geek()
    print('geek'[9])
except NameError as erra:
    print(f'Deu NameError: {erra}')
except TypeError as errb:
    print(f'Deu TypeError: {errb}')
except:
    print('Deu um erro diferente')


def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None
    
dic = {1: "Geek"}

print(pega_valor(dic, "nome"))