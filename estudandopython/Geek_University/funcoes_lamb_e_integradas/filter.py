"""
Filter

filter() -> Serve para filtrar dados de uma determinada coleção.

# Biblioteca para trabalhar com dados estastísticos
import statistics

# Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)

print(f'Média: {media}')
# OBS.: Assim como a função mean(), a filter() recebe dois parâmetros, sendo
# uma função e um iterável

res = filter(lambda x: x > media, dados)

print(res)
print(list(res))

paises = ['', 'Argentina', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

print(paises)

# res = filter(None, paises) # dica do None: '' is None

# Ou com lambda
# res = filter(lambda pais: len(pais) > 0, paises)
res = filter(lambda pais: pais != '', paises)

print(list(res))

# A diferença entre map() e filter() é:

# map() -> Recebe dois parâmetros, uma função e um interável e retorna um objeto mapeando a função para cada elemento do iterável.

# filter() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto filtrando apenas os elementos de acordo com função.

# Exemplo mais complexo

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": []},
]

# print(usuarios[0]['tweets'])

# Filtrar os usuários que estão inativos no Twitter (sem nenhum post)

# Forma 1
# inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))

# Forma 2
inativos = list(filter(lambda usuario: not usuario["tweets"], usuarios))
# Lista vázia em booleano é False, negar ela deixa em True

print(inativos)

# Detalhe tanto o map() quanto o filter() utilizam mascarado a "varredura, for"


"""


# Combinar filter() e map()

nomes = ['Vanessa', 'Ana', 'Maria', 'Gal']

# Devemos criar uma lista contendo 'Sua instrutora é' + nome, desde que cad nome tenha menos de 5 caracteres

lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))

# Se tiver dúvida, fazer cada parte separada: filter e depois map
print(lista)