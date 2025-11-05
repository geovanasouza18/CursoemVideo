import random
import time

print('\033[33m===== JOKENPÔ =====\033[0m')
jogador = input('\033[35mEscolha sua jogada: Pedra, Papel ou Tesoura: \033[0m').lower()

print('Computador escolhendo...')
time.sleep(1)

opcao = ['pedra', 'papel', 'tesoura']
computador = random.choice(opcao)

print(f'Computador jogou: {computador}')

if jogador not in opcao:
    print('\033[31mOpção inválida! Tente novamente. ⚠️\033[0m')

elif jogador == computador:
    print('Empate! 😐\nJoguem novamente.')

elif jogador == 'pedra':
    if computador == 'tesoura':
        print('Você venceu! Pedra esmaga tesoura 🔥')
    else:
        print('Computador venceu! Papel cobre pedra 💥')

elif jogador == 'papel':
    if computador == 'pedra':
        print('Você venceu! Papel cobre pedra 🔥')
    else:
        print('Computador venceu! Tesoura corta papel 💥')

elif jogador == 'tesoura':
    if computador == 'papel':
        print('Você venceu! Tesoura corta papel 🔥')
    else:
        print('Computador venceu! Pedra quebra tesoura 💥')
