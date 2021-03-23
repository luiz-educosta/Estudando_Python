"""
POO - Classes

Em POO, classes nada mais são do que modelos dos objetos do mundo real sendo representados computacionalmente.

Imagine que você queira fazer um sistema para automatizar o controle das lâmpadas da sua casa.

objeto do mundo real: Lâmpada -> Não existe um tipo(str, int, float)

Classes podem conter:
    - Atributos -> Representam as características do objeto. Ou seja, pelos atributos conseguimos representar computacionalmente os estados de um objeto. No caso da lâmpada, possívelmente poderiamos querer saber se a lâmpada é 110 ou 220, se ela é branca, amarela, vermelha ou outra cor, qual é a luminosidade dela e etc.

    - Métodos (funções) -> Representam os comportamentos do objeto. Ou seja, as ações que este objeto pode realizar no seu sistema. No caso da lâmpada, por exemplo, um comportamento comum que muito provavelmente iríamos querer representar no nosso sistema é o de ligar e desligar a mesma.

Em python, para definir uma classe utilizamos a palavra: class.

OBS: Utilizamos a palavra 'pass' em Python quando temos um bloco de código que ainda não está implementado.

OBS: Quando nomeamos nossas classes em Python utilizamos o por conveção o nome inicial em maiúsculo. Se o nome for composto, as iniciais são maiúscula, todas juntas

OBS: Quando estamos planejando um software e definimos quais classes teremos que ter no sistema, chamamos estes objetos que serão mapeados para classes de entidade.
"""
idade = 32
print(type(idade))

#  criou um tipo de dado
class Lampada:
    pass

class ContaCorrente():
    pass


lamp = Lampada()

print(type(lamp))