def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor incorreto'
    except ZeroDivisionError:
        return 'Não é possível realizar uma divisão por zero'
    
print(dividir(7, 9))

"""
Comandos básicos do PDB
l - (listar onde estamos no código)
n - (próxima linha)
p - (imprime variável) ou p nome_da_variável para imprimir a variável
c - (continua a execução - finaliza o debugging)
"""
breakpoint() # Função built-in para usar como debug