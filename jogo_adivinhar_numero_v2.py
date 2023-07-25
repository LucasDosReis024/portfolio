# Importação de bibliotecas.
import random, time

# Comando de replay do jogo.
def rejogar():

    # Abertura
    resposta = random.randint(0, 100)
    print('=-=-=' * 15)
    print('O computador pensou em um número de 0 a 100, você consegue adivinhar qual?')
    print('=-=-=' * 15)
    time.sleep(0.5)

    # Input para o chute.
    while True:
        time.sleep(1.5)
        chute = int(input('Tente adivinhar: '))

        # Resposta ao input, chute maior, menor e correto.
        if chute == resposta:
            print('Seu chute: ', chute)
            time.sleep(1)
            print('Parabéns, você acertou!')
            break
        elif chute < resposta:
            print('Seu chute: ', chute)
            time.sleep(1)
            print('Tente chutar mais alto.')
        else:
            print('Seu chute: ', chute)
            time.sleep(1)
            print('Tente chutar mais baixo.')

while True:
    rejogar()

    # Pergunta se o jogador deseja jogar novamente
    replay = input("Deseja jogar novamente? [s/n]: ")
    if replay.lower() != 's':
        break
