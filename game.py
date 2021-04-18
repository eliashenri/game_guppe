from models.calcular import Calcular

def main() -> None:
    pontos: int = 0
    jogar(pontos)

def jogar(pontos = int) -> None:
    dificuldade: int = int(input('Informe o nivel de dificuldade [1, 2 ou 3]: '))

    calc: Calcular = Calcular(dificuldade)

    print('Informe o Resultado para a seguinte operação: ')
    calc.mostrar_operacao()

    resultado: int = int(input())

    if calc.checar_resultado(resultado):
        pontos += 1
        print(f'Você tem {pontos} Ponto(s).')

    continuar: int = int(input('Deseja continuar no jogo? [1 - SIM, 0 - NÂO]'))

    if continuar:
        jogar(pontos)
    else:
        print(f'Você finalizou com {pontos} ponto(s).')

if __name__ == '__main__':
    main()
