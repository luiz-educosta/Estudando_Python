"""
3. Crie um classe denominada Elevador para armazenar as informações de um elevador dentro de um prédio. A classe deve armazenar o andar atual (térreo = 0), total de andares do prédio, excluindo o térreo, capacidade do elevador, e quantas pessoas estão presentes nele.
A Classe deve também disponibilizar os seguintes métodos:
    * Inicializa: que deve receber como parâmetros a capacidade do elevador e o total de andares no prédio (os elevadores sempre começam no térreo e vazio);
    * Entra: Para acrescentar uma pessoa no elevador (só deve acrescentar se ainda houver espaço);
    * Sai: para remover uma pessoa do elevador (só deve remover se houver alguém dentro dele);
    * Sobe: para subir um andar (não deve subir se já estiver no ultímo andar);
    * Desce: para descer um andar (não deve descer se já estiver no térreo);
    Encapsular todos os atributos da classe (criar os métodos set e get).
"""
class Elevador:
    def __init__(self, andar_atual, total_andares, capacidade, pessoas_presentes):
        self.__andar_atual = andar_atual
        self.__total_andares = total_andares
        self.__capacidade = capacidade
        self.__pessoas_presentes = pessoas_presentes