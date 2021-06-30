from models.calcular import Calcular


def main() -> None:
    pontos: int = 0
    jogar(pontos)


def jogar(pontos: int) -> None:
    dificuldade: int = input(
        'Informe o nível da dificuldade desejado: 1, 2, 3 ou 4:')

    calc: Calcular = Calcular(dificuldade)

    print('Informe o resultado para a seguinte operação:')
    calc.mostrar_operacao()

    resultado: float = float(input())

    if calc.checar_resultado(resultado):
        pontos += 1
        print(f'Você tem {pontos} ponto(s).')

    continuar: int = int(input('Deseja continuar o jogo? [1 - sim, 0 - não]'))

    if continuar:
        jogar(pontos)
    else:
        print(f'Você finalizou com {pontos} ponto(s).\nAté a próxima!')


if __name__ == '__main__':
    main()
