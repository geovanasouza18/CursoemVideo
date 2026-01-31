from random import randint
import time
jogadores = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6), 'jogador3': randint(1, 6), 'jogador4': randint(1, 6),}

for k, v in jogadores.items():
    time.sleep(1)
    print(f'O jogador {k} tirou {v}')

print('Ranking dos jogadores')

for i, k in enumerate(sorted(jogadores, key=jogadores.get, reverse=True), 1):
    time.sleep(1)
    print(f'{i}º lugar: {k} com {jogadores[k]}.')