"""
Manipulando cadeias de Texto

string ou cadeia de caracteres : 'Curso em Video Python'.
Uma lista de String é imutável, não conseguimos mexer nela
frase = 'Curso em Video Python'
| C | u | r | s | o |   | e | m |   | V | i | d | e | o |   | P | y | t | h | o | n |
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10| 11| 12| 13| 14| 15| 16| 17| 18| 19| 20|

**************************** Fatiamento de string ****************************
frase = 'Curso em Video Python'

frase[9] -> Escreve a letra que está com o Caracter 9. Saída: V

frase[9:13] -> Escreve de 9 a 13, o 'o'(13) não entra na lista ou seja o ultímo valor. Saída Vide o

frase[9:21] -> Vai do 9 até o 20. Saída: Video Python

frase[9:21:2] -> Começa no 9 e para no 21 e vai de 2 em 2. Saída: VdoPto

frase[:5] -> Antes do : é onde ele vai começar e termina até o 5,
mesmo que frase[0:5]. Saída: Curso

frase[15:] -> Indica o começo e vai até o final. Saída: Python

frase[9::3] -> Começa no 9 e vai até o final de 3 em 3. Saída: VePh



**************************** Análise ****************************
frase = 'Curso em Video Python'

len(frase) -> Mostra o comprimento da frase, Saída: 21

frase.count('o') -> Mostra o número de vezes que apareceu a letra 'o'. Saída: 3

frase.count('o', 0, 13) -> Contagem com fatiamento.

frase.find('deo') -> Quantas vezes encontrou 'deo', Saída monstra em que momento começou 'deo': 11

frase.find('Android') -> Se não existir, retorna o valor "-1"

'Curso' in frase -> Verifica se existe 'Curso' na frase Saída: True/False


**************************** Transformação ****************************
frase = 'Curso em Video Python'

frase.replace('Python', 'Android') -> Troca a palavra. Saída: Curso em Video Android

frase.upper() -> Todas as letras ficam em maiúscula. Saída: CURSO EM VÍDEO PYTHON

frase.lower() -> Todas as letras ficam minúsculas. Saída: curso em video python

frase.capitalize() -> Todos os caracteres para minúsculos e só o primeiro caractere fica em
maiúsculo. Saída: Cursoem video python.

frase.title() -> Analisa quantas palavras tem através dos espaços e deixa todas as primeiras
letras em maiúsculas. Curso Em Video Python.

frase = '   Aprenda Python  '

frase.strip() -> Remove todos os espaços inuteis no inicio e final da string.
Saída: 'Aprenda Python'

frase.rstrip() -> r de 'right', remove apenas o lado direito da string.
Saída: '   Aprensa Python'

frase.lstrip() -> l de 'left', remove apenas o lado esquerdo da string.
Saída: 'Aprensa Python  '

**************************** Divisão ****************************
frase = 'Curso em Video Python'

frase.split() -> Ocorre uma divisão dentro da string onde tem os espaços.
Gera uma lista com todas as plavras de uma cadeia de caracteres.
| C | u | r | s | o |   | e | m |   | V | i | d | e | o |   | P | y | t | h | o | n |
| 0 | 1 | 2 | 3 | 4 |   | 0 | 1 |   | 0 | 1 | 2 | 3 | 4 |   | 0 | 1 | 2 | 3 | 4 | 5 |
|         1         |   |   2   |   |         2         |   |           3           |

dividido = frase.split() -> Pega o dividido 2 que é video e mostra o terceiro caractere.
print(dividido[2][3])
Saída:e
**************************** Junção ****************************
frase = 'Curso em Video Python'

'-'.join(frase) -> Junta uma na outra. Saida: Curso-em-video-Python

*****************************************************************


"""
# print( """ para escrever um texto grande é só fazer colocando 3 aspas duplas (""") """)

frase = 'Curso em Video Python'
print('Curso' in frase)


